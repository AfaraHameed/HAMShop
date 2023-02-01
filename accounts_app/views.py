from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.
def signup(request):
    return render(request,'register.html')
def signin(request):
    return render(request,'login.html')
def signout(request):
    pass