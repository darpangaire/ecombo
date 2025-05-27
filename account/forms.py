from django import forms
from .models import Account
from django.core.exceptions import ValidationError

#######
from django.contrib.auth.forms import UserCreationForm

class RegistrationForm(UserCreationForm):
  password1 = forms.CharField(widget=forms.PasswordInput(attrs={
    'placeholder':'Enter Password',
    'class':'form-control'
  }))
  
  password2 = forms.CharField(widget=forms.PasswordInput(attrs={
    'placeholder':'Enter Confirm Password',
    'class':'form-control'
  }))
  
  class Meta:
    model = Account
    fields = ['first_name','last_name','email','phone_number','password1','password2']
    
  def __init__(self, *args, **kwargs):
    super(RegistrationForm,self).__init__(*args, **kwargs)
    self.fields['first_name'].widget.attrs.update({
      'placeholder':'Enter First Name',
    })
    
    self.fields['last_name'].widget.attrs.update({
      'placeholder':'Enter Last Name'
    })
    
    self.fields['phone_number'].widget.attrs.update({
      'placeholder':'Enter Phone Number'
    })
    
    self.fields['email'].widget.attrs.update({
      'placeholder':'Email Address'
    })
    
    
    for field in self.fields:
      self.fields[field].widget.attrs.update({'class':'form-control'})

  
  def clean_email(self):
    email = self.cleaned_data['email'].lower()
    try:
      email = Account.objects.get(email=email)
    except:
      return email
    
    raise ValidationError(f"Email {email} is already exists.")
  
  def clean_username(self):
    username = self.cleaned_data['username']
    try:
      username = Account.objects.get(username=username)
      
    except:
      return username
    
    raise ValidationError(f"UserName {username} is already Exists.")
  
  
      
                            