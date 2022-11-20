from django.urls import path
from . import  views
urlpatterns=[
    path('',views.home,name='home'),
    path('<slug:c_slug>/',views.home,name='prod_cat'),
    path('details',views.product_details,name='details')
]