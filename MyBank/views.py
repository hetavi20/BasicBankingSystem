
from unicodedata import name
from django.http import HttpResponse
from django.shortcuts import redirect, render
from django.contrib import messages
from MyBank.models import customerDetail,transaction

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
        # print(dataInfo)
    # return redirect('customerInfo')
    return render(request,'customerInfo.html',{'data':dataInfo})



def transferMoney(request):
    transactions=transaction.objects.all()
    return render(request,'transferMoney.html',{'transactions':transactions})


def transfer(request):
    
    if request.method == "POST":
        userId=request.POST.get('aid', '')
        myAccount=customerDetail.objects.get(name=userId)
        allCustomer=customerDetail.objects.all()
    return render(request,'transfer.html',{'customer':allCustomer,'myUser':myAccount})

def transferAmount(request):
    # allCustomer=customerDetail.objects.all()
    if request.method == "POST":
        myAccountId=request.POST.get('transferBy', '')
        toAccount=request.POST.get('transferTo','')
        amount=request.POST.get('amount','')
        dataInfo=customerDetail.objects.get(name=myAccountId)
        toTransfer=customerDetail.objects.get(name=toAccount)
        toTransferName=toTransfer.name
        if int(amount)<=dataInfo.currentBalence:
            toTransfer.currentBalence+=int(amount)
            toTransfer.save()
            dataInfo.currentBalence-=int(amount)
            dataInfo.save()
            myTransaction=transaction(amount=amount, toTransfer=toTransferName,fromTransfer=dataInfo) 
            myTransaction.save()
            messages.success(request, 'Money has been transferred. Kindly check your balance.')
            print("hi")
            return redirect('allCustomer')
            # return render(request,'allCustomer.html')   
        else:
            messages.success(request, 'No sufficient Money is available. Kindly check your balance.')
            return redirect('allCustomer')
        # return render(request,'allCustomer.html',{'data':dataInfo,'customer':allCustomer})
    

def contactUs(request):
    return render(request,'contactUs.html')

def aboutUs(request):
    return render(request,'aboutUs.html')
