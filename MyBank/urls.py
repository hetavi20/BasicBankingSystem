from . import views
from django.contrib import admin
from django.urls import path

urlpatterns = [
    path('',views.home,name="home"),
    path('allCustomer',views.allCustomer,name="allCustomer"),
    path('contactUs',views.contactUs,name="contactUs"),
    path('aboutUs',views.aboutUs,name="aboutUs"),
    path('customerInfo',views.customerInfo,name="customerInfo"),
    # path('customerInformation',views.customerInformation,name="customerInformation"),
    path('transferMoney',views.transferMoney,name="transferMoney"),
    path('transferAmount',views.transferAmount,name="transferAmount"),
     path('transfer',views.transfer,name="transfer"),


]
