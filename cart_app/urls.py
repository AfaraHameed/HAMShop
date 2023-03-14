from django.urls import path,register_converter
from . import views
from order_app import converts

register_converter(converts.FloatUrlParameterConverter, 'float')
urlpatterns=[
    path('',views.cartdetails,name='cartdetails'),
    path('addcart/<int:product_id>/',views.add_cart,name='addcart'),
    path('cartdec/<int:product_id>/', views.min_cart, name='mincart'),
    path('cartdel/<int:product_id>/', views.cart_delete, name='delcart'),

]
