from django.shortcuts import render

# Create your views here.
def home(request):
    print("hai")
    return render(request,'index.html')