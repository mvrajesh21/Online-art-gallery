from django.db.models import Q
from django.http import HttpResponse
from django.shortcuts import render

def homefunction(request):
    return render(request,"index.html")
def aboutfunction(request):
    return render(request,"about.html")
def loginfunction(request):
    return render(request,"login.html")
def contactfunction(request):
    return render(request,"contact.html")
def artistloginfunction(request):
    return render(request,"artlogin.html")
def userloginfunction(request):
    return render(request,"userlogin.html")
def artistspfunction(request):
    return render(request,"artsp.html")
def userspfunction(request):
    return render(request,"usersp.html")
def userprofilefunction(request):
    return render(request,"userprofile.html")
def privacypolicy(request):
    return render(request,"pp.html")
def suppliersfunction(request):
    return render(request,"suppliers.html")
def doodfun(request):
    return render(request,"learn/doodle.html")
def aesthfun(request):
    return render(request,"learn/aesthetic.html")
def sculpfun(request):
    return render(request,"learn/sculpture.html")
def realfun(request):
    return render(request,"learn/reallife.html")
def penfun(request):
    return render(request,"learn/pen.html")
def naturefun(request):
    return render(request,"learn/nature.html")
def animefun(request):
    return render(request,"learn/anime.html")
def tradfun(request):
    return render(request,"learn/traditional.html")

