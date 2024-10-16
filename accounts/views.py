from django.shortcuts import render,redirect

from accounts.models import Accounts

from accounts.forms import AccountForm

def account(request):
    if(request.method=="POST"):
        form=AccountForm(request.POST)
        if(form.is_valid()):
            try:
                form.save()
                return redirect('/show')
            except:
                pass
    else:
        form=AccountForm()
    return render(request,'index.html',{'form':form})
       
def show(request):
    accounts=Accounts.objects.all()
    return render(request,'show.html',{'accounts':accounts})

def edit(request,id):
    account=Accounts.objects.get(id=id)
    return render(request,'edit.html',{'account':account})

def update(request,id):
    account=Accounts.objects.get(id=id)
    form=AccountForm(request.POST,instance=account)
    if form.is_valid():
        form.save()
        return redirect('/show')
    return render(request,'edit.html',{'account':account})

def dlt(request,id):
    account=Accounts.objects.get(id=id)
    account.delete()
    return redirect('/show')
