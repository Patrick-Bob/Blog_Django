from django import forms
from django.forms import ModelForm
from blog_app.models import Blog

class ArticleForm(forms.ModelForm):
    
    class Meta:
        model = Blog
        fields = ("name","content","article_image")


    
  