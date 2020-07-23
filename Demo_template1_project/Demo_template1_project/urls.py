"""Demo_template1_project URL Configuration

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
from App1 import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.home_view),
    path('home/', views.home_view,name='home'),
    path('reg/', views.registration_view, name='reg'),
    path('login/', views.login_view, name='login'),
    path('data/', views.getdata_view, name='data'),
    path('datapost/', views.getdatapost_view, name='datapost'),
    path('readlogin/', views.readLogin_view, name='readlogin'),
    path('stdlogin/', views.Student_formview, name='stdlogin'),
    path('stdformlogin/', views.stdform_login_view, name='stdformlogin'),
    path('myfile/',views.senddata_fileview)


]