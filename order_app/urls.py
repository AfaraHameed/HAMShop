from django.urls import path,register_converter
from . import views
from order_app import converts

register_converter(converts.FloatUrlParameterConverter, 'float')
urlpatterns=[
    path('payment/<float:amount>/',views.payment,name='payment'),
    path('callback/', views.callback, name='callback'),

]
