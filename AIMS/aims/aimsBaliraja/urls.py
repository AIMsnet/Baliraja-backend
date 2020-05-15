from django.urls import path
from django.conf.urls import url
from . import views
from django.contrib.auth import views as auth_views

urlpatterns = [

    path('', views.home, name='home'),
    
    path('login/SignUp/', views.CustomerSignUp, name='home'),
    path('login/SignUp/customerSignUp/', views.CustomerSignUp, name='CustomerSignUp'),
    path('login/SignUp/customerSignUp/customerSignUp/', views.CustomerSignUp, name='CustomerSignUp'),
    path('login/SignUp/customerSignUp/customerSignUp/customerSignUp/', views.CustomerSignUp, name='CustomerSignUp'),
    path('login/SignUp/customerSignUp/customerSignUp/customerSignUp/customerSignUp/', views.CustomerSignUp, name='CustomerSignUp'),
    path('login/SignUp/customerSignUp/customerSignUp/customerSignUp/customerSignUp/customerSignUp/', views.CustomerSignUp, name='CustomerSignUp'),

    path('login/', auth_views.LoginView.as_view(template_name='CustomerLogin.htm'), name='login'),
    path('login/login/', auth_views.LoginView.as_view(template_name='CustomerLogin.htm'), name='login'),
    path('login/login/login/', auth_views.LoginView.as_view(template_name='CustomerLogin.htm'), name='login'),
    path('login/login/login/login/', auth_views.LoginView.as_view(template_name='CustomerLogin.htm'), name='login'),
    path('login/login/login/login/login/', auth_views.LoginView.as_view(template_name='CustomerLogin.htm'), name='login'),

    
    path('logout/', views.logout),
]


    