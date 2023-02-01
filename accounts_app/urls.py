from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path

from accounts_app import views

urlpatterns = [
    path('signup/', views.signup,name="signup"),
    path('signin/', views.signin,name="signin"),
    path('signout/', views.signout,name="signout"),
]
