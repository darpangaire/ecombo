from django.db import models
from django.contrib.auth.models import AbstractBaseUser,BaseUserManager

# Create your models here.

class AccountManager(BaseUserManager):
  def create_user(self,email,username,password=None):
    if not email:
      raise ValueError("User must have an email address")
    
    if not username:
      raise ValueError("user must have an unique username")
    
    user = self.model(
    email = self.normalize_email(email),
    username = username,
    password=password
    )
    
    user.set_password(password)
    user.save(using = self._db)
    return user
  
  def create_superuser(self,email,username,password):
    user = self.create_user(
      email = self.normalize_email(email),
      username = username,
      password=password

    )
    
    user.is_admin = True
    user.is_staff = True
    user.is_superadmin = True
    user.is_active = True
    user.save(using=self._db)
    return user
  
    
class Account(AbstractBaseUser):
  first_name = models.CharField(max_length=100,null=True)
  last_name = models.CharField(max_length=100,null=True)
  email = models.EmailField(max_length=250,unique=True)
  username = models.CharField(max_length=250,unique=True)
  phone_number = models.CharField(max_length=20,null=True,blank=True)
  
  date_joined = models.DateTimeField(auto_now_add=True)
  last_login = models.DateTimeField(auto_now=True)
  is_admin = models.BooleanField(default=False)
  is_staff = models.BooleanField(default=False)
  is_superadmin = models.BooleanField(default=False)
  is_active = models.BooleanField(default=True)
  
  
  objects = AccountManager()
  USERNAME_FIELD  = 'email'
  REQUIRED_FIELDS = ['username']
  
  def __str__(self):
    return self.username
  
  def has_perm(self,perm,obj=None):
    return self.is_admin
  
  def has_module_perms(self,app_label):
    return True
  

    
