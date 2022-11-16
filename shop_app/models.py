from django.db import models
from django.template.defaultfilters import slugify
# Create your models here.
class categ(models.Model):

    def __str__(self):
        return self.name
    name = models.CharField(max_length=200,unique='true')
    slug = models.SlugField(max_length=200,unique='true')

    class Meta:
        ordering = ('name', )
        verbose_name = 'category'
        verbose_name_plural = 'categories'

class products(models.Model):
    def __str__(self):
        return self.name
    name = models.CharField(max_length=200,unique='true')
    slug = models.SlugField(max_length=200,unique='true')
    image = models.ImageField(upload_to='products')
    desc = models.TextField()
    stock = models.IntegerField()
    available = models.BooleanField()
    price = models.IntegerField()
    category_id = models.ForeignKey(categ,on_delete=models.CASCADE,default=1)