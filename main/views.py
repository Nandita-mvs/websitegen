from django.shortcuts import render,redirect
from .models import *
from django.contrib import messages
from .forms import MemberForm
from django.core.mail import send_mail

def Home(request):
        form=MemberForm()
        error=""
        if request.method == "POST":
           form=MemberForm(request.POST,request.FILES) 
           if form.is_valid():
               form.save()
               error="no"
        context={'form':form,'error':error}
        return render(request,'home.html', context)
                
def Portfolio(request):
    error=""
    member=Member.objects.all()
    size=len(Member.objects.all())-1
    toemail=member[size].emailid
    
    if request.method == "POST":
        fromemail=request.POST['email']
        subject=request.POST['subject']
        message=request.POST['message']
        try:
            send_mail(subject,message,fromemail,[toemail])
            error="no"
        except:
            error="yes"

    d={'member':member[size],'error':error}
    return render(request,"portfolio.html",d)