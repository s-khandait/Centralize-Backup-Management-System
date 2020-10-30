from django.shortcuts import render, redirect
from django.contrib.auth.models import User, auth
from django.contrib import messages
# Create your views here.
def register(request): 
    if request.method=="POST": 
        first_name = request.POST['first_name']
        last_name = request.POST['last_name']
        username = request.POST['username']
        email = request.POST['email']
        password1 = request.POST['password1']
        password2 = request.POST['password2']
         
        if(password1==password2):
            if(User.objects.filter(username=username).exists()):
                messages.info(request,'Username Taken')
                return render(request, 'register.html') 
            elif(User.objects.filter(email=email).exists()):
                messages.info(request,'Email Taken')
                return render(request, 'register.html') 
            else:                
                user = User.objects.create_user(username=username, last_name=last_name,first_name=first_name,email=email,password =password1)
                user.save();
                print('user created')
                return redirect('login')
        else:
            messages.info(request,'Password Not match')
            return render(request, 'register.html') 
        return redirect('/')
    else:
        return render(request, 'register.html')

def login(request):
    if request.method=="POST": 

        username = request.POST['username']
        password2 = request.POST['password']
        
        user = auth.authenticate(username=username, password = password2)
        if (user is not None):
            auth.login(request, user)        
            return redirect('/')
        else:

            messages.info(request, 'Invalid credentials')
            return redirect('login.html')
    else:
        return render(request, 'login.html')

def backup(request):
    return render(request, 'backup.html')

def logout(request):
    auth.logout(request)
    return redirect('/')
