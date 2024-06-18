from django import forms
from django.contrib.auth.models import User
from api.models import Products

class LoginForm(forms.Form):

    username = forms.CharField()
    password = forms.CharField()

class RegisterationForm(forms.ModelForm):

    class Meta:
        model = User
        fields = ["first_name","last_name","email","username","password"]

class ProductForm(forms.ModelForm):
    class Meta:
        model = Products
        fields = "__all__"

        


