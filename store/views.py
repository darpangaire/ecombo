from django.shortcuts import render
from .models import Product,ProductVariant

# Create your views here.
def product(request):
  products = Product.objects.prefetch_related('variants__color','variants__size')
  context = {
    'products':products,
  }
  return render(request,'store/shop.html',context)

