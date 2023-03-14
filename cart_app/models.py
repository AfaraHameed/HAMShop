from importlib.resources import _

from django.db import models

from cart_app.constants import PaymentStatus
from shop_app.models import *


# Create your models here.

class cartlist(models.Model):
    cart_id = models.CharField(max_length=200,unique='true')
    date = models.DateField(auto_now_add='true')
    razor_pay_order_id = models.CharField(max_length=100,null=True,blank=True)
    razor_pay_payment_id = models.CharField(max_length=100,null=True,blank=True)
    razor_pay_payment_signature = models.CharField(max_length=100,null=True,blank=True)
    status = models.CharField(default=PaymentStatus.PENDING, max_length=254,blank=False,null=False,)
    provider_order_id = models.CharField(_("Order ID"),max_length=40, null=False, blank=False)
    def __str__(self):
        return self.cart_id

class items(models.Model):
    prdct = models.ForeignKey(products,on_delete=models.CASCADE)
    cart = models.ForeignKey(cartlist,on_delete=models.CASCADE)
    quantity = models.IntegerField()
    active = models.BooleanField(default=True)

    def __str__(self):
        return str(self.prdct)
    def totalprice(self):
        return self.prdct.current_price()*self.quantity

