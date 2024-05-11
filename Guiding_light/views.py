from django.shortcuts import render,redirect
from django.conf import settings
from django.core.mail import send_mail
from .models import *
# Create your views here.
def index(request):
    return render(request,'index.html')

def contact(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        email = request.POST.get('email')
        subject = request.POST.get('subject')
        message = request.POST.get('message')
        print(name,email,subject,message)
        Contact.objects.create(name=name,
email=email,
subject=subject,
message=message)
        from_email = settings.EMAIL_HOST_USER
        to_email = email
        # send mail to admin
        send_mail("Contact", "Thanks for Contact U.\n I hope you like your services and if you have any other feedback than please provide to us so, your team try to resolve this problem imedatelly.\nYou are successfully Creating a new account \n  We are appricating your step toward the make Digital India by usnig the application of our portal \n Thanks for Support .",
         from_email, [to_email],fail_silently = False)     
   
    return render(request,'contact.html')


def appointment(request):
    if request.method == 'POST':
        name= request.POST.get('name')
        email = request.POST.get('email')
        phone = request.POST.get('phone')
        chdoc= request.POST.get('chdoc')
        date= request.POST.get('date')
        time= request.POST.get('time')
        desc= request.POST.get('desc')
        print(name,email,phone,chdoc,date,time,desc)
        Appointment.objects.create(name=name,email=email,phone=phone,chdoc=chdoc,date=date,time=time,desc=desc)
        from_email = settings.EMAIL_HOST_USER
        to_email = email
        # send mail to admin
        send_mail("Appointment sent", "Hello, Nice to meet you... precation for health.",
         from_email, [to_email],fail_silently = False)
        return redirect('/appointment')
    return render(request,'appointment.html')

def features(request):
    return render(request,'features.html')

def testimonial(request):
    return render(request,'testimonial.html')

def about(request):
    return render(request,'about.html')

def service(request):
    return render(request,'service.html')

def team(request):
    return render(request,'team.html')
    