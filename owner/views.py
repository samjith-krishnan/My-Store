from django.shortcuts import render
from owner.forms import LoginForm,RegisterationForm,ProductForm

# Create your views here.

from django.views.generic import View


class HomeView(View):

    def get(self,request,*args,**kw):

        return render(request,"home.html")
    
class SignupView(View):
    def get(self,request,*args,**kw):
        form = RegisterationForm()
        return render(request,"register.html",{"form":form})
    
class SigninView(View):
    def get(self,request,*args,**kw):
        form =LoginForm()
        return render(request,"signin.html",{"form":form})
    
    def post(self,request,*args,**kw):
        print(request.POST)
        print(request.POST.get("username"))
        print(request.POST.get("password"))

        return render(request,"home.html")

class ProductAddView(View):

    def get(self,request,*args,**kw):
        form = ProductForm()

        return render(request,"products-add.html",{"form":form})


        
