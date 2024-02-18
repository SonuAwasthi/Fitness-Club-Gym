from django.shortcuts import render,HttpResponse,redirect
from django.contrib.auth.models import User
from django.contrib.auth import authenticate,login,logout
from Gymapp.models import Membars
from django.contrib.auth.decorators import login_required
from django.contrib import messages


@login_required(login_url="loginpage")
def membarpage(request):
    if request.method=="POST":
        fullname=request.POST.get("fullname")
        number=request.POST.get("number")
        gmail=request.POST.get("gmail")
        packages=request.POST.get("packages")
        gender=request.POST.get("gender")
        membar=Membars(fullname=fullname,number=number,gmail=gmail,packages=packages,gender=gender)
        membar.save()
        messages.success(request, "Congratulation to Being Fitness Club Membar ")
    return render(request,"membarpage.html")


def index(request):
    return render(request,"index.html")


def ourgym(request):
    return render(request,"ourgym.html")

def about(request):
    return render(request,"about.html")



def signpage(request):
    if request.method=="POST":
        username=request.POST.get("username")
        gmail=request.POST.get("gmail")
        pass1=request.POST.get("password")
        pass2=request.POST.get("password2")
        if pass1!=pass2:
            messages.warning(request, "Your Password is not same!")
        else:
            user=User.objects.create_user(username,gmail,pass1)
            user.save()
            messages.success(request, "Your Account has been created")
    return render(request,"signpage.html")



def loginpage(request):
    if request.method=="POST":
        username=request.POST.get("username")
        pass1=request.POST.get("password")
        user=authenticate(username=username,password=pass1)
        if user is not None:
            login(request,user)
            return redirect("membarpage")
    
        else:
            messages.warning(request, "Your Password or username is incorrect!")
        
    return render(request,"loginpage.html")

def logoutpage(request):
    logout(request)
    return render(request,"loginpage.html")