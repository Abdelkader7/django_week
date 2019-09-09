from django.http import HttpResponse
from django.shortcuts import get_object_or_404,render,redirect
from django.urls import reverse



def home_page_view(request):
    return HttpResponse('Hello World')

def home_page_view_with_render(request):
    return render(request,"home_page.html")


def form(request):

    login_user = "" 
    password_user = ""   
    if request.method == "POST":
       # print(request.POST)
        login_user = request.POST["login"]
        password_user = request.POST["password"]
        print(login_user)

        print(password_user)
    return render(request, "form_page.html",{"login":login_user,"password":password_user})