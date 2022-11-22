from django import forms
from django.contrib.auth import get_user_model
from django.contrib.auth.forms import UserCreationForm
from blogApp.models import *
User=get_user_model()
class UserRegistration(UserCreationForm):
    class Meta:
        model=User
        fields=['username','first_name','last_name','email','password1','password2']
    # def password_verification(self):
    #     try:
              
class LoginForm(UserCreationForm):
    class Meta:
        model=User
        fields=['username','password1']       
class BlogForm(forms.ModelForm):
    class Meta:
        model=Blog
        fields='__all__'
        
class CommentForm(forms.ModelForm):
    class Meta:
        model=Comment
        fields=["comment_content",]     