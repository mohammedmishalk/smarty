from django.http import HttpResponse
from django.shortcuts import render,redirect
from django.contrib.auth.models import auth, User
from django.contrib import messages
from .models import usernameConvart,userprofile
from teachers import models

# Create your views here.
def home(request):
    return render(request,"home.html")
def user(request):
    return render(request,"register.html")

def register(request):
    if request.method == 'POST':
        full_name = request.POST['name']
        username = request.POST['username']
        email = request.POST['email']
        img = "images/example3.jpg"
        password =f"smarty{request.POST['password']}"
        selection =request.POST['select']
        select = 0
        if selection == 1:
            select = 1
        else:
            select = 0
        # user validation and register
        if User.objects.filter(username=username).exists():
            messages.error(request, "username already taken")
            return redirect('user')
        elif User.objects.filter(email=email).exists():
            messages.error(request, "email already registerd")
        else:
            user = User.objects.create_user(username=username,password=password,email=email)
            user.save()
            userp =userprofile(username=username,full_name=full_name,email=email,ac_type=select,img=img)
            userp.save()

            # automatic login 
            user_log = auth.authenticate(username=username,password=password)
            c=""
            for i in username:
                c+=str(ord(i))
            new_username = hex(int(c))
            new_um = usernameConvart(username=username,new_username=new_username)
            new_um.save()
            co = models.contact.objects.get_or_create(pk=username)
            qu = models.Quality.objects.get_or_create(pk=username)
            if user_log is not None:
                auth.login(request, user_log)
                return redirect(f'st/{new_username}/dash')

            else:
                messages.error(request, "invalid submition")
    else:
        return redirect("user")

def login(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = f"smarty{request.POST['password']}" 
        user = auth.authenticate(username=username, password=password)
        if user is not None:
            n = usernameConvart.objects.get(pk=username)
            auth.login(request,user)
            return redirect(f'st/{n.new_username}/dash')

        else:
            msg = 'invalid username or password'
            return render(request,"register.html",{'error_msg':msg})
    else:
        return redirect('user')

def logout(request):
    auth.logout(request)
    return redirect('/')

def contact(request):
    return render(request,"contact.html")

def about(request):
    return render(request,"about.html")

def autologin(request):
    pass
