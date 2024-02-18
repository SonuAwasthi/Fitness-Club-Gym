from django.contrib import admin
from django.urls import path
from Gymapp import views

urlpatterns = [
    path("",views.index,name="index"),
    path("about/",views.about,name="about"),
    path("ourgym/",views.ourgym,name="ourgym"),
    path("signpage/",views.signpage,name="signpage"),
    path("loginpage/",views.loginpage,name="loginpage"),
    path("membarpage/",views.membarpage,name="membarpage"),
    path("logoutpage/",views.logoutpage,name="logoutpage")
]