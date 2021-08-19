from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User


class UserLoginForm(forms.Form):
    username = forms.CharField(label= "Username")
    password = forms.CharField(label= "Password",widget=forms.PasswordInput())

class UserRegisterForm(UserCreationForm):
    email = forms.EmailField()
    
    class Meta:
        model = User
        fields = ['username','email','password1','password2']



# class RegisterForm(forms.Form):
#     username = forms.CharField(label= "Username", max_length = 100, required=False)
#     password = forms.CharField(label = "Password" , max_length = 100, required=False)
#     confirm = forms.CharField(label= "Confirm Password" , max_length = 100, required=False)

#     def clean(self):
#         username =  self.cleaned_data.get("username")
#         password = self.cleaned_data.get("password")

#           #Bu hissede ValidationError gelmir option kimi buna gorede wrong password olanda exception vermir(  

#         if password and confirm  and password != confirm:
#             raise forms.ValidationError(" Incorrect password")
            
    
#         values = {
#             "username" : username,
#             "password" : password
#         }
        
#         return values
        