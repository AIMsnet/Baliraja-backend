from django import forms
from django.contrib.auth import get_user_model
from django.core.exceptions import ValidationError
from django.contrib.auth.forms import UserCreationForm,AuthenticationForm
from .models import User
from django.contrib import auth
from django.contrib.auth import authenticate, login

class CustomerSignUpForm(UserCreationForm):
    error_css_class = 'error'
    username = forms.CharField(label='Mobile Number')
    class Meta:
        model = User
        fields = [
            
            'first_name',
            'last_name',
            'username',
            # 'mob_no',
            'email',
            'address',
            'post',
            'taluka',
            'district',
            'password1',
            'password2'
        ]

       

    def clean_username(self):
        print('inside form')
        username = self.cleaned_data['username']
        print(username)
        if User.objects.filter(username=username).exists():
            print('no already exist')
            raise forms.ValidationError("This mobile number already exist.")
        return username

    # def clean_mob_no(self):
    #     print('inside form')
    #     mob_no = self.cleaned_data['mob_no']
    #     print(mob_no)
    #     if User.objects.filter(mob_no=mob_no).exists():
    #         print('no already exist')
    #         raise forms.ValidationError("This mobile number already exist.")
    #     return mob_no

    def clean_email(self):
        print('inside email')
        email = self.cleaned_data['email']
        print(email)
        if User.objects.filter(email=email).exists():
            print('email already exist')
            raise forms.ValidationError("This email Id already exist.")
            
        if '@' not in email:
            print('INVALID email ')
            raise forms.ValidationError("This email Id is INVALID .")
        return email

    def clean_password2(self):
        print('inside password confirmation')
        password1=self.cleaned_data['password1']
        password2=self.cleaned_data['password2']
        print(password2)
        if password1!=password2:
            print('Password does not match')
            raise forms.ValidationError("Password does not match.Please re-enter password")
        return password2

    # def save(self):
    #     print('save')
    #     if username == '':
    #         self.username = self.cleaned_data['mob_no']
    #     super(CustomerSignUpForm, self).save()

# class CustomerSignInForm(AuthenticationForm):
#     error_css_class = 'error'
#     class Meta:
#         model = User
#         fields = [
#             'username',
#             'password'
#         ]

#     def clean_password(self):
#         username=self.cleaned_data['username']
#         password=self.cleaned_data['password']
        
#         user = auth.authenticate(username=username, password=password)
#         print(user)
#         if user is not None:
#             auth.login(self, user)
#         else:
#             raise forms.ValidationError( "Enter correct username and password")    
            