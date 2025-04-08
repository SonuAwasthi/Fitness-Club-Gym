from django.contrib import admin
from django.urls import path
from Gymapp import views

urlpatterns = [
    # path("",views.index,name="index"),
    path("",views.pindex,name="pindex"),
    path("about/",views.about,name="about"),
    path("ourgym/",views.ourgym,name="ourgym"),
    path("signpage/",views.signpage,name="signpage"),
    path("loginpage/",views.loginpage,name="loginpage"),
    path("membarpage/",views.membarpage,name="membarpage"),
    path("logoutpage/",views.logoutpage,name="logoutpage"),
    path("quickview/<int:p_id>",views.quickview,name="quickview"),
    path("search/",views.search,name="search"),
    path("forverify/<slug:username>",views.forverify,name="forverify"),
    path("forgetp",views.forgetp,name="forgetp"),
    path("confirmpass/<slug:username>",views.confirmpass,name="confirmpass"),
    path("myplan/",views.myplan,name="myplan"),
    path("notmyplan",views.notmyplan,name="notmyplan"),
]