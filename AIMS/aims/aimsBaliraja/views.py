from django.shortcuts import render,redirect
from django.contrib.auth.models import User
from django.contrib.auth import get_user_model
from django.http import HttpResponse, HttpRequest, HttpResponseRedirect
from django.conf import settings
from django.contrib import messages
from django.contrib import auth
from .models import User, Categories
from .forms import CustomerSignUpForm

#For sendOTP
import http.client
import math, random
from django.http import JsonResponse


def home(request):

     
    cats    = Categories.objects.all()

    return render(request, 'HomeTwo.htm', {'cats': cats})

def SignUp(request):
    form = CustomerSignUpForm()
    form.is_bound
    return render(request, 'CustomerSignUp1.htm', {'form':form})

def CustomerSignUp(request):
    form = CustomerSignUpForm()
    form.is_bound
    #errors = form.errors
    if request.method == 'POST':
        form = CustomerSignUpForm(request.POST or None)
        if form.is_valid():
            print('form is valid')
            
            form.save()
            username = form.cleaned_data.get('first_name')
            messages.success(request, f'Your account has been created ! You are now able to login {username}!')
            print('saved')
            return redirect('login')
        
    else:
        form = CustomerSignUpForm()
    return render(request, 'CustomerSignUp1.htm',{'form': form} )



    

# def customerSignIn(request):
#     form = CustomerSignInForm()
#     if request.method=='POST':
#         form= CustomerSignInForm(request.POST)
#         if form.is_valid():
#             print('inside authentication')
#             return redirect('/')
#     else:
#         print('inside else')
#         print(form.errors)
#         form = CustomerSignInForm()
#     return render(request, 'CustomerLogin.htm',{'form': form} )


# def customerSignIn(request):
#     if request.method =='POST':

#         mobno =request.POST.get('mob_no')
#         password =request.POST.get('password')

#         user = auth.authenticate(username=mobno, password=password)
#         print(user)
#         if user is not None:
#             auth.login(request, user)
            
#             print('user logged in')
#             return redirect('/')
#         else:
#             messages.info(request, "invalid creadential")
#             return redirect('thankYou/')
    
#     else:
#         print('else part login')
#         return render(request, 'login.html') 

#     return HttpResponseRedirect('/customerSignIn/') 


def logout(request):
    auth.logout(request)
    return redirect('/')