
from django.contrib import admin
from django.urls import path, include
from . import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path("",views.homefunction,name="home"),
    path("about",views.aboutfunction,name="about"),
    path("login",views.loginfunction,name="login"),
    path("contact",views.contactfunction,name="contact"),
    path("artlogin",views.artistloginfunction,name="artlogin"),
    path("userlogin",views.userloginfunction,name="userlogin"),
    path("artistsp",views.artistspfunction,name="artistsp"),
    path("usersp",views.userspfunction,name="usersp"),
    path("userprofile",views.userprofilefunction,name="userprofile"),
    path("pp",views.privacypolicy,name="pp"),
    path("suppliers",views.suppliersfunction,name="suppliers"),
    path("dood",views.doodfun,name="dood"),
    path("aesthe",views.aesthfun,name="aesthe"),
    path("sculp",views.sculpfun,name="sculp"),
    path("real",views.realfun,name="real"),
    path("pen",views.penfun,name="pen"),
    path("nature",views.naturefun,name="nature"),
    path("anime",views.animefun,name="anime"),
    path("trad",views.tradfun,name="trad"),

    path("",include("artistapp.urls")),

]
