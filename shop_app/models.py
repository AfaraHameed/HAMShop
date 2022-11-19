from django.db import models
from django.template.defaultfilters import slugify
from django.urls import reverse


# Create your models here.
class categ(models.Model):

    def __str__(self):
        return '{}'.format(self.name)
    name = models.CharField(max_length=200,unique='true')
    slug = models.SlugField(max_length=200,unique='true')

    class Meta:
        ordering = ('name', )
        verbose_name = 'category'
        verbose_name_plural = 'categories'

    def get_url(self):
        return reverse('prod_cat',args=[self.slug])
class products(models.Model):
    def __str__(self):
        return '{}'.format(self.name)
    name = models.CharField(max_length=200,unique='true')
    slug = models.SlugField(max_length=200,unique='true')
    image = models.ImageField(upload_to='products')
    desc = models.TextField()
    stock = models.IntegerField()
    available = models.BooleanField()
    price = models.IntegerField()
    offer = models.BooleanField()
    offer_val = models.IntegerField()
    category_id = models.ForeignKey(categ,on_delete=models.CASCADE,default=1)

    def current_price(self):
        off = (self.price * self.offer_val) / 100
        return self.price-off