from django.shortcuts import render,redirect
from django.contrib.auth.models import User,auth
from django.contrib import messages

# Create your views here.

def login(request):
    if request.method=='POST':
        username = request.POST['username']
        password = request.POST['password']
        user = auth.authenticate(username=username,password=password)
        if user is not None:
            auth.login(request,user)
            return redirect('/')
        else:
            messages.info(request,"Invalid User Credentials")
            return redirect('login')
    else:
        return render(request,"login.html")

def register(request):
    if request.method=="POST":
        username = request.POST['username']
        first_name = request.POST['first_name']
        email = request.POST['email']
        password1 = request.POST['password1']
        password2 = request.POST['password2']

        if password1==password2:
            if User.objects.filter(username=username).exists():
                messages.info(request,"Username already exist")
                return redirect('register')
            elif User.objects.filter(email=email).exists():
                messages.info(request,"Email already exist")
                return redirect('register')
            else:
                user=User.objects.create_user(username=username,password=password1,first_name=first_name,email=email)
                user.save();
                print("User created")
        else:
            print("Password not match")
            return redirect('register')
        return redirect('/')

    else:

        return render(request,'registration.html')


def logout(request):
    auth.logout(request)
    return redirect('/')