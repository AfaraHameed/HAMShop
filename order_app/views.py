from django.shortcuts import render,redirect,get_object_or_404

from shop_app.models import *
from cart_app.models import *
from django.core.exceptions import ObjectDoesNotExist
import razorpay
from django.conf import settings
from .constants import PaymentStatus
from django.views.decorators.csrf import csrf_exempt
from razorpay.resources import order
from cart_app.views import c_id
import json

from .models import Order


# Create your views here.
def payment(request,amount):
    ct1=cartlist.objects.get(cart_id=c_id(request))
    ct = Order.objects.create(cartid=ct1)
    client = razorpay.Client(auth=(settings.KEY, settings.SECRET))
    tot_amount = int(amount * 100)
    payment1 = client.order.create({'amount': tot_amount, 'currency': 'INR', 'payment_capture': '1'})
    ct.razor_pay_order_id = payment1['id']
    ct.save()
    return render(
        request,
        'payment.html',
        {
            "callback_url": "http://" + "127.0.0.1:8000" + "/order/callback/",
            "razorpay_key": settings.KEY,
            'payment': payment1,
        },

    )


@csrf_exempt
def callback(request):
    def verify_signature(response_data):
        client = razorpay.Client(auth=(settings.KEY, settings.SECRET))
        return client.utility.verify_payment_signature(response_data)

    if "razorpay_signature" in request.POST:
        payment_id = request.POST.get("razorpay_payment_id", "")
        provider_order_id = request.POST.get("razorpay_order_id", "")
        signature_id = request.POST.get("razorpay_signature", "")
        order1 = Order.objects.get(razor_pay_order_id=provider_order_id)
        order1.razor_pay_payment_id = payment_id
        order1.razor_pay_payment_signature = signature_id

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
        order1 = Order.objects.get(razor_pay_order_id=provider_order_id)
        order1.payment_id = payment_id
        order1.status = PaymentStatus.FAILURE
        order1.save()
        return render(request, "callback.html", context={"status": order1.status})
