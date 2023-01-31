from django.db import models
from shop_app.models import *


# Create your models here.

class cartlist(models.Model):
    cart_id = models.CharField(max_length=200,unique='true')
    date = models.DateField(auto_now_add='true')

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

