from django.shortcuts import render,redirect,get_object_or_404

from shop_app.models import *
from cart_app.models import *
from django.core.exceptions import ObjectDoesNotExist
import razorpay
from django.conf import settings
from .constants import PaymentStatus
from django.views.decorators.csrf import csrf_exempt
from razorpay.resources import order
import json

# Create your views here.
def cartdetails(request,tot=0,count=0,ct_items=None):
    try:
        ct=cartlist.objects.get(cart_id=c_id(request))
        ct_items=items.objects.filter(cart=ct,active=True)
        for i in ct_items:
            tot += (i.prdct.current_price() * i.quantity)
            count += i.quantity
    except ObjectDoesNotExist:
        pass
    client = razorpay.Client(auth=(settings.KEY, settings.SECRET))
    amount=int(tot*100)
    payment = client.order.create({'amount':amount,'currency':'INR','payment_capture':'1'})
    ct.razor_pay_order_id = payment['id']
    ct.save()
    print('*******')
    print(payment)

    print('*******')
    context={'ci':ct_items,'t':tot,'co':count,'payment':payment}
    # return render(
    #     request,
    #     'cart.html',
    #     {
    #         "callback_url": "http://" + "127.0.0.1:8000" + "/callback/",
    #         "razorpay_key": settings.KEY,
    #         'ci': ct_items, 't': tot, 'co': count, 'payment': payment
    #     },
    #
    # )
    return  render(request,'cart.html',context)

def c_id(request):
    ct_id = request.session.session_key
    if not ct_id:
        ct_id = request.session.create()
    return ct_id
def add_cart(request,product_id):
    prod = products.objects.get(id=product_id)
    try:
        ct=cartlist.objects.get(cart_id=c_id(request))
    except cartlist.DoesNotExist:
        ct = cartlist.objects.create(cart_id=c_id(request))
        ct.save()
    try:
        c_items = items.objects.get(prdct=prod,cart=ct)
        if c_items.quantity < c_items.prdct.stock:
            c_items.quantity+=1
        c_items.save()
    except items.DoesNotExist:
        c_items= items.objects.create(prdct=prod,quantity=1,cart=ct)
        c_items.save()
    return redirect('cartdetails')
def min_cart(request,product_id):
    ct=cartlist.objects.get(cart_id=c_id(request))
    prod=get_object_or_404(products,id=product_id)
    c_items=items.objects.get(prdct=prod,cart=ct)
    if c_items.quantity>1:
        c_items.quantity-=1
        c_items.save()
    else:
        c_items.delete()
    return  redirect("cartdetails")
def cart_delete(request,product_id):
    ct=cartlist.objects.get(cart_id=c_id(request))
    prod=get_object_or_404(products,id=product_id)
    c_items=items.objects.get(prdct=prod,cart=ct)
    c_items.delete()
    return  redirect("cartdetails")

# def checkout(request):
#     client = razorpay.Client(auth = (settings.razor_pay_key_id , settings.key_secret))
#     payment = client.order.create()

def payment(request,amount):
    ct = cartlist.objects.get(cart_id=c_id(request))
    client = razorpay.Client(auth=(settings.KEY, settings.SECRET))
    tot_amount = int(amount * 100)
    payment = client.order.create({'amount': tot_amount, 'currency': 'INR', 'payment_capture': '1'})
    ct.razor_pay_order_id = payment['id']
    ct.save()
    print('*******')
    print(payment)

    print('*******')
    return render(
        request,
        'payment.html',
        {
            "callback_url": "http://" + "127.0.0.1:8000" + "/cartdetails/callback/",
            "razorpay_key": settings.KEY,
            'payment': payment
        },

    )


@csrf_exempt
def callback(request):
    def verify_signature(response_data):
        client = razorpay.Client(auth=(settings.KEY, settings.SECRET))
        print(request.POST)
        return client.utility.verify_payment_signature(response_data)

    if "razorpay_signature" in request.POST:
        payment_id = request.POST.get("razorpay_payment_id", "")
        provider_order_id = request.POST.get("razorpay_order_id", "")
        signature_id = request.POST.get("razorpay_signature", "")
        order1 = cartlist.objects.get(razor_pay_order_id=provider_order_id)
        print(order1)
        order1.payment_id = payment_id
        order1.signature_id = signature_id
        order1.save()
        if verify_signature(request.POST):
            order1.status = PaymentStatus.SUCCESS
            order1.save()
            print('order status'+order1.status)
            return render(request, "callback.html", context={"status": order1.status})
        else:
            order1.status = PaymentStatus.FAILURE
            order1.save()
            print('order status' + order1.status)
            return render(request, "callback.html", context={"status": order1.status})
    else:
        payment_id = json.loads(request.POST.get("error[metadata]")).get("payment_id")
        print('*******'+payment_id)
        provider_order_id = json.loads(request.POST.get("error[metadata]")).get(
            "order_id"
        )
        order1 = cartlist.objects.get(provider_order_id=provider_order_id)
        order1.payment_id = payment_id
        order1.status = PaymentStatus.FAILURE
        order1.save()
        return render(request, "callback.html", context={"status": order1.status})
