from django.urls import path
from .views import add_cart,cartItems_view

urlpatterns = [
  path('<int:product_id>/',add_cart,name='addCart'),
  path('cartView/',cartItems_view,name='cartView'),
]