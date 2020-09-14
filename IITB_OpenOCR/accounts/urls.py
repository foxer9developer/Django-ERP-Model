from django.urls import path
from . import views
from django.contrib.auth import views as auth_views

app_name = "accounts"

urlpatterns = [
    path('register/', views.register, name ='register'),
    path('login/', views.loginPage, name ='login'),
    path('logout/', views.logoutLink, name ='logout'),

]
