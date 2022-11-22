from django.db.models import Q
from django.shortcuts import render, get_object_or_404
from .models import products,categ
from django.core.paginator import Paginator,EmptyPage,InvalidPage


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
    paginator = Paginator(product,2)
    try:
        page=int(request.GET.get('page','1'))
    except:
        page=1
    try:
        pro=paginator.page(page)
    except(EmptyPage,InvalidPage):
        pro=paginator.page(paginator.num_pages)
    return render(request,'index.html',{'product':product,'category':category,'pg':pro})
def product_details(request,c_slug,product_slug):
    try:
        product = products.objects.get(category__slug = c_slug,slug = product_slug)
    except Exception as e:
        raise e
    return render(request,'single-product.html',{'product':product})

def searching(request):
    product=None
    query=None
    if 'q' in request.GET:
        query = request.GET.get('q')
        product = products.objects.all().filter(Q(name__contains=query)|Q(desc__contains=query))
    return  render(request,'search.html',{'product':product,'qr':query})