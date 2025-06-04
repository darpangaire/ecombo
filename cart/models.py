from django.db import models
from store.models import Product,ProductVariant
from django.conf import settings

# Create your models here.
class Cart(models.Model):
  user = models.ForeignKey(settings.AUTH_USER_MODEL,null=True,blank=True,on_delete=models.CASCADE)
  session_id = models.CharField(max_length=255,null=True,blank=True)
  created_at = models.DateTimeField(auto_now_add=True)
  
  def __str__(self):
    return f"Cart ({self.user or self.session_id})"
  
class CartItem(models.Model):
  cart = models.ForeignKey(Cart,on_delete=models.CASCADE,related_name="items")
  product_variant = models.ForeignKey(ProductVariant, on_delete=models.CASCADE)
  quantity = models.PositiveIntegerField(default=1)
  
  def __str__(self):
    return f" {self.product_variant} x {self.quantity}"
  
  def total_price(self):
    return self.product_variant.price*self.quantity
  
