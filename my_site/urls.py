"""my_site URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from django.contrib.auth import views as auth_views

from .views import home_page_view_with_render,carte, graph,subscribe, redirection, user_liste

urlpatterns = [
    path('admin/', admin.site.urls),
    path('home_page',home_page_view_with_render, name="home_render"),
    path('carte/', carte, name='carte'),
    path('graph/', graph, name='graph'),
    path('subscribe/', subscribe, name='subscribe'),
    path('login/', auth_views.LoginView.as_view(), name='login'),
    path('', auth_views.LoginView.as_view(), name='login'),
    path('logout/', auth_views.LogoutView.as_view(), name='logout'),
    path('passwordreset/', auth_views.PasswordResetView.as_view(), name='passwordreset'),
    path('password-reset/done/', auth_views.PasswordResetDoneView.as_view(), name='password_reset_done'),
    path('reset/<uidb64>/<token>/', auth_views.PasswordResetConfirmView.as_view(), name='password_reset_confirm'),
    path('reset/done/', auth_views.PasswordResetCompleteView.as_view(), name='password_reset_complete'),
    #path('restaurant_registration/', restaurant_registration, name="restaurant_registration"),
    #path('restaurant_liste/', restaurant_liste, name="restaurant_liste"),
    path('redirection/', redirection, name="redirection"),
    path('user_liste/', user_liste, name="user_liste")
]
