from django.shortcuts import render, redirect
from django.views.generic import View
from django.contrib.auth import login, logout, get_user_model
from django.db import transaction
from django.contrib import messages
import re

User = get_user_model()
EMAIL_REGEX = r'\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Z|a-z]{2,7}\b'


class Login(View):

    def get(self, request):
        if request.user.is_authenticated:
            return redirect('home')
        return render(request,'login.html')
    
    def post(self, request):
        phone = request.POST.get('phone')
        password = request.POST.get('password')

        if not phone or not password:
            messages.error(request,"All Fields are Mendatory!")
            print('All Fields are Mendatory')

        # if not (re.fullmatch(EMAIL_REGEX, email)):
        #     messages.error(request,"Enter Valid Email Address!")

        user=User.objects.filter(phone=phone).first()
        
        if user is None:
            messages.error(request,"You are not registered Please create account first!")
            return redirect('login')

        if user.check_password(password):
            login(request,user)
            messages.info(request,"Login Successful!")
            return redirect('home')
        else:
            messages.error(request," Incorrect Password!")
            print("Incorrect Password")

        return render(request,'login.html')
    

class Register(View):

    def get(self, request):
        if request.user.is_authenticated:
            return redirect('home')
        return render(request,'register.html')
    
    def post(self, request):
        phone = request.POST.get('phone')
        password1 = request.POST.get('password1')
        password2 = request.POST.get('password2')

        # if not (re.fullmatch(EMAIL_REGEX, email)):
        #     messages.error(request,"Enter Valid Email Address!")

        if User.objects.filter(phone=phone).exists():
            messages.error(request,"Phone Already Registered")
            return redirect('home')

        if password1 != password2:
            messages.error(request,"Both Password Don't Match")
            return redirect('home')
        
        with transaction.atomic():
            user = User.objects.create_user(phone,password1)

        if user:
            messages.info(request,"User Registered Successfully!")
            login(request,user)
            return redirect('home')

        return redirect('home')
    
    
class Logout(View):

    def get(self, request):
        logout(request)
        messages.info(request,"Logout Successful!")

        return redirect('login')
    