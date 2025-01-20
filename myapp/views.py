from django.shortcuts import render,redirect,HttpResponse
from .models import UserRegister
# Create your views here.
def data(request):
    return render(request,'page.html')
    

from django.core.mail import send_mail
from django.conf import settings
def reg(request):
    if request.method == 'POST':
        regdata = UserRegister()
        regdata.name = request.POST['name']
        regdata.password = request.POST['password']
        regdata.email = request.POST['email']
        regdata.mob = request.POST['phone']
        regdata.add = request.POST['add']
        
        useralready = UserRegister.objects.filter(email = request.POST['email'])
        # if useralready:
        if len(useralready) > 0:  
            return render(request, 'reg.html', {'already':'Email already exists!!!'})
        else:
            if request.POST['password']==request.POST['Confirmpassword']:
                regdata.save()
                send_mail(
                    'welcome message from our website',
                    'This is an authication email',
                    'settings.EMAIL_HOST_USER',
                    [regdata.email],
                    fail_silently=False 
                )
            else:
                return render(request, 'reg.html', {'cp':'try again'})

        return render(request, 'reg.html', {'store':'Data has been entered successfully!'})
    else:
        return render(request, 'reg.html')
import random
def login(request):
    if request.method == 'POST':
        try:
            useremail = UserRegister.objects.get(email = request.POST['email'])
            if useremail.password == request.POST['password']:
                request.session['s_email'] = useremail.email
                otp =random.randint(100000,999999)
                request.session['otp']=otp
                send_mail(
                    'welcome',
                    f'Your OTP for login of ecommerce is {otp}',
                    'rudrampanchal@gmail.com',
                    [useremail.email],
                    fail_silently=False 
                )
                return redirect('otp')
                # return redirect('second')
            else:
                return render(request,'login.html', {'password': 'Incorrect password!'})
        except:
            return render(request,'login.html', {'email': 'Email does not exist!'})    
    else:
        return render(request, 'login.html')
    
def logout(request):
    del request.session['s_email']
    return redirect('second')