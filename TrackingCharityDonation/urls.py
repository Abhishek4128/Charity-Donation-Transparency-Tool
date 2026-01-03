"""TrackingCharityDonation URL Configuration

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
from MainApp import views
urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.index),
    path('user',views.login),
    path('Register',views.Register),
    path('RegAction',views.RegAction),
    path('LogAction',views.LogAction),
    path('chome',views.chome),
    path('CreateCampaign',views.CreateCampaign),
    path('CamapignAction',views.CamapignAction),
    path('dlogin',views.dlogin),
    path('dRegister', views.dRegister),
    path('DRegAction',views.DRegAction),
    path('DLogAction',views.DLogAction),
    path('dhome',views.dhome),
    path('dBrowseCamp',views.dBrowseCamp),
    path('CheckTrust',views.CheckTrust),
    path('dDonationAction', views.dDonationAction),
    path('dviewmydonatoins',views.dviewmydonatoins),
    path('ViewReceiveFunds',views.ViewReceiveFunds),
    path('AddFundsUsage', views.AddFundsUsage),
    path('AddFUsedAction', views.AddFUsedAction),
    path('dviewdetails',views.dviewdetails),
    path('alogin',views.alogin),
    path('adminLogAction',views.adminLogAction),
    path('aTransaction', views.aTransaction),
    path('adminhome',views.adminhome),
    path('aDTransaction', views.aDTransaction),
]
