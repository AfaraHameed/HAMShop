from django.urls import path,register_converter
from . import views,converts
register_converter(converts.FloatUrlParameterConverter, 'float')
urlpatterns=[
    path('',views.cartdetails,name='cartdetails'),
    path('addcart/<int:product_id>/',views.add_cart,name='addcart'),
    path('cartdec/<int:product_id>/', views.min_cart, name='mincart'),
    path('cartdel/<int:product_id>/', views.cart_delete, name='delcart'),
    path('payment/<float:amount>/',views.payment,name='payment'),
    path('callback/', views.callback, name='callback'),

]
