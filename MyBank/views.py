from django.http import HttpResponse
from django.shortcuts import redirect, render
from django.contrib import messages
from MyBank.models import customerDetail

# Create your views here.


def home(request):
    return render(request,'home.html')

def allCustomer(request):
    allCustomer=customerDetail.objects.all()
    return render(request, 'allCustomer.html',{'customer':allCustomer})


def customerInfo(request):
    if request.method == "POST":
        accountId=request.POST.get('aid', '')
        dataInfo=customerDetail.objects.get(accountNo=accountId)
        print(dataInfo)
        # return redirect('customerInfo')
    return render(request,'customerInfo.html',{'data':dataInfo})


def transferMoney(request):
    if request.method == "POST":
        accountId=request.POST.get('aid', '')
        dataInfo=customerDetail.objects.get(accountNo=accountId)
    return render(request,'transferMoney.html',{'data':dataInfo})


def transfer(request):
    allCustomer=customerDetail.objects.all()
    return render(request,'transfer.html',{'customer':allCustomer})

def transferAmount(request):
    allCustomer=customerDetail.objects.all()
    if request.method == "POST":
        accountId=request.POST.get('aid', '')
        amount=request.POST.get('amount','')
        dataInfo=customerDetail.objects.get(name=accountId)
        dataInfo.currentBalence+=int(amount)
        dataInfo.save()
        messages.info(request, 'Money has been transferred. Kindly check your balance')
    return render(request,'allCustomer.html',{'data':dataInfo,'customer':allCustomer})

def contactUs(request):
    return render(request,'contactUs.html')

def aboutUs(request):
    return render(request,'aboutUs.html')
