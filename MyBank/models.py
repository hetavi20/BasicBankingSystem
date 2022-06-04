import email
from tkinter import CASCADE
from django.db import models

# Create your models here.
class customerDetail(models.Model):
    gender=(
        ("Male","Male"),("Female","Female"),("Other","Other")
    )
    name=models.CharField(max_length=50,default='')
    email=models.CharField(max_length=50,default='')
    gender=models.CharField(max_length=10,default='',choices=gender)
    birthDate=models.DateField(default='')
    phoneNo=models.CharField(max_length=50,default = '')
    aadharNo=models.CharField(max_length=50,default = '')
    address=models.CharField(max_length=500,default='')
    city=models.CharField(max_length=500,default='')
    state=models.CharField(max_length=500,default='')
    zip=models.CharField(max_length=50,default='')
    accountNo=models.IntegerField(default=0)
    currentBalence=models.IntegerField(default=0)
    def __str__(Self):
        return Self.name


class transaction(models.Model):
    amount=models.IntegerField(default=0)
    toTransfer=models.CharField(max_length=50,default='')
    fromTransfer=models.ForeignKey(customerDetail,on_delete=models.CASCADE)
    def __str__(Self):
        return Self.toTransfer