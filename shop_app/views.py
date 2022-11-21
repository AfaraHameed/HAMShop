from django.shortcuts import render, get_object_or_404
from .models import products,categ



# Create your views here.
def home(request,c_slug=None):
    c_page = None
    product = None
    if c_slug != None:
        c_page = get_object_or_404(categ,slug=c_slug)
        product = products.objects.filter(category=c_page,available=True)
    else:
        product = products.objects.all().filter(available=True)
    category = categ.objects.all()
    return render(request,'index.html',{'product':product,'category':category})
def product_details(request,c_slug,product_slug):
    try:
        product = products.objects.get(category__slug = c_slug,slug = product_slug)
    except Exception as e:
        raise e
    return render(request,'single-product.html',{'product':product})