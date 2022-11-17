from django.shortcuts import render
from .models import products,categ



# Create your views here.
def home(request):
    product = products.objects.all()
    category = categ.objects.all()
    return render(request,'index.html',{'product':product,'category':category})
