from django.shortcuts import render,redirect
from django.shortcuts import HttpResponse
from .models import *
from django.contrib import messages
from .forms import MemberForm,LoginForm
from django.core.mail import send_mail
from django.contrib.auth import authenticate,login,logout
from django.shortcuts import get_object_or_404 
from django.contrib.auth.models import User

def intro(request):
    return render(request,'account/intro.html')

def Home(request):
    if not request.user.is_authenticated:
        return redirect('/accounts/login')
    else:
        print(request.user)
        form=MemberForm()
        error=""
        if request.method == "POST":
           form=MemberForm(request.POST,request.FILES) 
           if form.is_valid():
               member=form.save(commit=False)
               member.user = request.user
               member.save()
               error="no"
        context={'form':form,'error':error}
        return render(request,'home.html', context)
                
def Portfolio(request):
     if not request.user.is_authenticated:
        return redirect('accounts/login')
     else:
        print(request.user)
        member=Member.objects.get(user=request.user)
        error=""
        toemail=member.emailid
        
        if request.method == "POST":
            fromemail=request.POST['email']
            subject=request.POST['subject']
            message=request.POST['message']
            try:
                send_mail(subject,message,fromemail,[toemail])
                error="no"
            except:
                error="yes"

        d={'member':member,'error':error}
        return render(request,"portfolio.html",d)


