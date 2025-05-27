from django.urls import path
from . import views

urlpatterns = [
  path('register/',views.view_register,name='register'),
  path('login/',views.view_login,name='login'),
  path('change-password/',views.change_password,name='change_password'),
]

