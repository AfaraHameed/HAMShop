from django.urls import path
from . import views
urlpatterns=[
    path('',views.cartdetails,name='cartdetails'),
    path('addcart/<int:product_id>/',views.add_cart,name='addcart'),
    path('cartdec/<int:product_id>/', views.min_cart, name='mincart'),
    path('cartdel/<int:product_id>/', views.cart_delete, name='delcart')

]
