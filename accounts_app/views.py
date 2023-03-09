from django.contrib.auth import authenticate, login, logout
from django.http import HttpResponse
from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from  django.contrib import messages
# Create your views here.
def signup(request):
    if request.method == "POST":
        fname = request.POST['firstname']
        lname = request.POST['lastname']
        username = request.POST['username']
        email = request.POST['email']
        password = request.POST['password']
        cpassword = request.POST['cpassword']


        if User.objects.filter(username=username):
            messages.error(request,"user name already exists")
            return redirect('signup')
        if User.objects.filter(email=email):
            messages.error(request,"email already registered")
            return redirect('signup')
        if len(username)>10:
            messages.error(request,"username must be under 10 charecters")
            return redirect('signup')
        if password != cpassword:
            messages.error(request,"password didn't match")
            return redirect('signup')
        if not username.isalnum():
            messages.error(request,"user name must be alpha-numeric")
            return redirect('signup')
        myuser = User.objects.create_user(username,email,password)
        myuser.first_name = fname
        myuser.last_name = lname
        myuser.save()

        messages.success(request,"Your account has been successfully created")
        return redirect('signin')

    return render(request,'register.html')
def signin(request):
    if request.method == 'POST':
        username = request.POST['username']
        pass1=request.POST['password']
        user = authenticate(username=username,password=pass1)

        if user is not None:
            login(request,user)
            username = user.username
            messages.success(request, "LoggedIn Successfully")
            return render(request,'index.html',{'username':username})

        else:
            messages.error(request,"Bad credentials")
            return redirect('signin/')
    return render(request,'login.html')
def signout(request):
    logout(request)
    messages.success(request,"Logged Out Successfully")
    return redirect('/')