from django.http import HttpResponse
from django.shortcuts import render
def home_page_view(request):
    return HttpResponse('Hello World')

def home_page_view_with_render(request):
    return render(request,"home_page.html")