from django.db import models

from order_app.constants import PaymentStatus
from cart_app.models import cartlist


# Create your models here.
class Order(models.Model):
    cartid = models.ForeignKey(cartlist,on_delete=models.CASCADE,)
    date = models.DateField(auto_now_add='true')
    razor_pay_order_id = models.CharField(max_length=100,null=True,blank=True)
    razor_pay_payment_id = models.CharField(max_length=100,null=True,blank=True)
    razor_pay_payment_signature = models.CharField(max_length=100,null=True,blank=True)
    status = models.CharField(default=PaymentStatus.PENDING, max_length=254,blank=False,null=False,)

    def __str__(self):
        return self.razor_pay_order_id
