from django.shortcuts import render,redirect,get_object_or_404

from cart_app.models import *
from django.core.exceptions import ObjectDoesNotExist
import razorpay
from django.conf import settings


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
    context = {'ci': ct_items, 't': tot, 'co': count}
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


