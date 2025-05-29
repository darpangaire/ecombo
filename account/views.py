from django.shortcuts import render
from django.shortcuts import render, redirect
from .forms import RegistrationForm
from django.contrib import messages
from .models import Account
from django.contrib.auth import login,authenticate,logout
from django.contrib.auth.models import auth
from django.contrib.auth.decorators import login_required
# Create your views here.

def view_register(request):
  context = {}
  if request.method == 'POST':
    form = RegistrationForm(request.POST)
    if form.is_valid():
      email = form.cleaned_data['email'].lower()
      password = form.cleaned_data['password1']
      username = email.split('@')[0]
        
      first_name = form.cleaned_data['first_name']
      last_name = form.cleaned_data['last_name']
      phone_number = form.cleaned_data['phone_number']
      try:
        user = Account.objects.create_user(email=email,username=username,password=password)
        user.first_name = first_name
        user.last_name = last_name
        user.phone_number = phone_number
        return redirect('login')
      except Exception as e:
        messages.error(request,f"registration unsuccessful")

      
  else:
    form = RegistrationForm()
    
  context = {
    'form':form
  }

  return render(request, 'account/register.html',context)
  
  
def view_login(request):
  if request.method == 'POST':
    email = request.POST.get('email')
    password = request.POST.get('password')
    user = auth.authenticate(email=email,password=password)
    if user:
      login(request,user)
      messages.success(request,'Login successful')
      return redirect('home')
    else:
      messages.error(request,'Login unsuccessful')
      # return redirect('login')
      
  return render(request,'account/login.html')


def change_password(request):
  if request.method == 'POST':
    email = request.POST['email']
    try:
      user = Account.objects.get(email=email)
    except:
      messages.error(request,"email not valid")
      return redirect('change_password')
    
    
    new_password = request.POST.get('new-password')
    confirm_password = request.POST.get('confirm-password')
    if new_password != confirm_password:
      messages.error(request,"Password doesnot Match!")
      return redirect('change_password')
    
    user.set_password(new_password)
    user.save()
    
    messages.success(request,'Password changed successfully! please login...')
    return redirect('login')
  
@login_required(login_url='login')
def logout(request):
  auth.logout(request)
  messages.success(request,"You are logged out")
  return redirect('login')

  

  
  
  

      
    
    
    
      
      
      
  
  return render(request,'account/change_password.html')
