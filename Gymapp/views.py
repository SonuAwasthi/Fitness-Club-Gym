from django.shortcuts import render,redirect
from django.contrib.auth.models import User
from django.contrib.auth import authenticate,login,logout
from Gymapp.models import Membars,Product,userverify,gymplan
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from datetime import datetime,timedelta
from django.core.mail import send_mail
# from dateutil.relativedelta import relativedelta
import random


@login_required(login_url="loginpage")
def membarpage(request):
    if request.method=="POST":
        pusername=request.POST.get("username")
        number=request.POST.get("number")
        gmail=request.POST.get("gmail")
        packages=request.POST.get("packages")
        gender=request.POST.get("gender")
        mainuser=User.objects.get(username=pusername)
        
        # if not gymplan.objects.filter(userplan=mainuser).exists():
        #     messages.success(request, "ee na chalbe")
        #     return redirect("membarpage")
        if gymplan.objects.filter(userplan=mainuser).exists():
            messages.success(request, "duplicate not allowed ")
            return redirect("membarpage")
        
        muser=gymplan.objects.create(userplan=mainuser,number=number,gmail=gmail,packages=packages,gender=gender)

        if muser:
            muser.save()
            messages.success(request, "Congratulation to Being Fitness Club Membar ")
            return redirect("/", pusername=pusername)
    return render(request,"membarpage.html")


def myplan(request):
    usernam=User.objects.get(username=request.user)
    bb=gymplan.objects.filter(userplan=usernam).values()
    now=[]
    after=[]
    if not bb:
        return render(request,"notmyplan.html")
    else:
        for i in bb:
            after=int(i['packages'])
        for iy in bb:
            now=iy['datetime']
        expiry=now+timedelta(days=after*30)
        return render(request,"myplan.html",{"bb":bb[0],"expiry":expiry})
    # tom=now+relativedelta(month=after)
    return render(request,"myplan.html")

def notmyplan(request):
    return render(request,"notmyplan.html")





def loginpage(request):
    if request.method=="POST":
        username=request.POST.get("username")
        pass1=request.POST.get("password")
        user=authenticate(username=username,password=pass1)
        if user is not None:
            login(request,user)
            return redirect('membarpage')
    
        else:
            messages.warning(request, "Your Password or username is incorrect!")
        # return redirect('login')
    return render(request,"loginpage.html")


def pindex(request):
    product=Product.objects.values("category")
    setprod={item["category"] for item in product}   

    for categorywise in setprod:
        home=Product.objects.filter(category="Home Exercise").values()
        chest=Product.objects.filter(category="Chest Exercise").values()
        bicep=Product.objects.filter(category="Bicep Exercise").values()
        shoulder=Product.objects.filter(category="Shoulder Exercise").values()
        lowerbody=Product.objects.filter(category="Lower Body Exercise").values()
        abc=request.user
        context={
            "abc":abc,
            "home":home,
            "chest":chest,
            "bicep":bicep,
            "shoulder":shoulder,
            "lowerbody":lowerbody,

        }
    return render(request,"pindex.html",context)

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

        
        if User.objects.filter(username=username).exists():
            messages.warning(request, "USERNAME is allready exists")
            return redirect("signpage")

        if pass1 != pass2:
            messages.warning(request, "Your Password is not same!")
            return redirect("signpage")
        else:
            userotp=random.randint(1001,9999)
            user=User.objects.create_user(username,gmail,pass1)
            addtoverify=userverify.objects.create(user=user,otp=userotp)
            addtoverify.save()
            send_mail(f'Helloo {username}', f"your otp is:{userotp}", 'sonuawasthi880@gmail.com', [gmail])
            return redirect('forverify',username=username)
    return render(request,"signpage.html")


def forverify(request,username):
    if request.method=="POST":
        u_otp=request.POST.get("otp")
        usernam=User.objects.get(username=username)
        userver=userverify.objects.filter(user=usernam,otp=u_otp).last()

        if userver:
            userver.is_verified=True
            userver.save()
            messages.success(request,f" Helo {username} your account has been verified")
            return redirect("loginpage")
        else:
            messages.warning(request,"your otp is wrong")
            return redirect("forverify",username=username)
        
    return render(request,"forverify.html",{"usern":username})

def forgetp(request):
    if request.method=="POST":
        username=request.POST.get("username")
        gmail=request.POST.get("gmail")
        uuu=User.objects.get(username=username)
        www=userverify.objects.filter(user=uuu).last()
        if www:
            u_otp=random.randint(1001,9999)
            www.otp=u_otp
            www.save()
            send_mail(f'Helloo {username}', f"your otp for changing password: {u_otp}", 'sonuawasthi880@gmail.com', [gmail])
            return redirect("confirmpass",username=username)
        
        else:
            messages.error(request,"username did not exist")
            return redirect("forgetp")
              
    return render(request,'forgetp.html')


def confirmpass(request,username):
    if request.method=="POST":
        pass1=request.POST.get("password")
        pass2=request.POST.get("password2")
        u_otp=request.POST.get("otp")
        uuu=User.objects.get(username=username)
        check=userverify.objects.filter(user=uuu,otp=u_otp).last()
    

        if pass1 != pass2:
            messages.error(request,"not matched password")
            return redirect("confirmpass")
        
        if check:
            uuu.set_password(pass1)
            uuu.save()
            messages.success(request,"Succsessfully Password changed")
            return redirect("loginpage")
        
        else:
            messages.error(request,"somthing wrong")
            return redirect("confirmpass",username=username)

    
    return render(request,'confirmpass.html',{"usern":username})



def logoutpage(request):
    logout(request)
    return redirect('pindex')

def quickview(request,p_id):
    now=datetime.today()
    tom=now+timedelta(days=3)
    pd=Product.objects.filter(p_id=p_id).values()
    contex={"now":tom,
            "pd":pd[0]
             }

    
    return render(request,"quickview.html",contex)


def search(request):
    query=request.GET["query"]
    sname=Product.objects.filter(name__icontains=query)
    scate=Product.objects.filter(category__icontains=query)
    sprice=Product.objects.filter(price__icontains=query)
    searchall=sname | scate | sprice
    para={
        "searchall":searchall
    }
    return render(request,"search.html",para)

