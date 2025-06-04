from django.shortcuts import render,get_object_or_404,redirect
from .models import CartItem,Cart
from store.models import Product,ProductVariant,Color,Size
from django.contrib import messages
# Create your views here.
def _create_id(request):
  cart = request.session.session_key
  if not cart:
    cart = request.session.create()
  return cart


def add_cart(request,product_id):
  user = request.user
  if request.method == 'POST':
    product = Product.objects.get(id=product_id)
    color = request.POST.get('color')
    size = request.POST.get('size')
    price = request.POST.get('price')
    try:
      color = Color.objects.get(name=color)
    except Color.DoesNotExist:
      messages.error(request, "This Color variation does not exist.")
      return redirect('store')
      
    try:
      size = Size.objects.get(name=size)
    except Size.DoesNotExist:
      messages.error(request, "This Size variation does not exist.")
      return redirect('store')
    
    # create product variation for all auth and unauth user
    try:
      product_variation = ProductVariant.objects.get(product=product,color=color,size=size)
    except ProductVariant.DoesNotExist:
      messages.error(request, "This product variation does not exist.")
      return redirect('store')
      
    # if user is authenticated
    if user.is_authenticated:
      # if cart and cartItems are already exists
      try:
        cart = Cart.objects.get(user=user)  
      except Cart.DoesNotExist:
        cart = Cart.objects.create(user=user)
        
      cart_item,created = CartItem.objects.get_or_create(cart=cart,product_variant=product_variation)
      if not created:
        cart_item.quantity += 1
        cart_item.save()

    # THis is for unauth users.    
    else:
      session_id = _create_id(request)
      try:
        cart = Cart.objects.get(session_id=session_id)  
      except Cart.DoesNotExist:
        cart = Cart.objects.create(session_id=session_id)
        
      cart_item,created = CartItem.objects.get_or_create(cart=cart,product_variant=product_variation)
      if not created:
        cart_item.quantity += 1
        cart_item.save()
              
        
    return redirect('cartView')



def cartItems_view(request):
  user = request.user
  if user.is_authenticated:
    try:
      cart = Cart.objects.get(user=user)
      cartItems = CartItem.objects.filter(cart=cart)
    except:
      pass
  else:
    try:
      session_id = _create_id(request)
      cart = Cart.objects.get(session_id = session_id)
      cartItems = CartItem.objects.filter(cart=cart)
    except:
      pass
    
    
  
  
  context = {
    'cartItems':cartItems
  }
  
  return render(request,'cart/cart.html',context)



