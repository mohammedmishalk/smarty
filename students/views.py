from django.http import HttpResponse
from django.shortcuts import render, redirect
from django.contrib.auth.models import User, auth 
from accounts.models import usernameConvart, userprofile
from .models import contact

# Create your views here.
def dashboard(request, new_username):
    if request.method =='GET' :
        user=nameconvert(new_username)
        try:
            ud= userdata(user)
        except:
            return redirect('/user')
        if ud.ac_type == 0:
            return redirect(f'/te/{new_username}/dash')
    return render(request,'std_dash.html')


def userp(request, new_username):
    if request.method == "GET" :
        user = nameconvert(new_username)
        user_data = userdata(user)
        return render(request,"std_acc.html",{"user":user_data}) 

def chat(request, new_username):
    if request.method == "GET" :
        return render(request,"std_chat.html")

def books(request, new_username):
    if request.method == "GET" :
        return render(request,"std_books.html")

def course(request, new_username):
    if request.method == "GET" :
        return render(request,"std_course.html")

def comp(request, new_username):
    if request.method == "GET" :
        return render(request,"std_comp.html")

def cert(request, new_username):
    if request.method == "GET" :
        return render(request,"std_certificate.html")

def ask(request, new_username):
    if request.method == "GET" :
        return render(request,"std_ask.html")    

def pay(request, new_username):
    if request.method == "GET" :
        return render(request,"std_pay.html")   

def logout(request , new_username):
    auth.logout(request)
    username=""
    return redirect('/')

def nameconvert(n):
    u=usernameConvart.objects.filter(new_username=n)
    s=u[0]
    username = s.username
    return s.username

def userdata(username):
    user = userprofile.objects.get(pk=username)
    return(user)

def edit(request,new_username):
    if request.method =='GET':
        return render(request,"std_edit.html")
    elif request.method == "POST":
        img=request.FILES['photo']
        name = request.POST["name"]
        email = request.POST["email"]
        phone = request.POST["ph"]
        address = request.POST["add"]
        password=f"smarty{request.POST['pass']}"
        dob =f"{request.POST['yy']}-{request.POST['dd']}-{request.POST['mm']}"
        gender = request.POST['gender']
        fb= request.POST['fb']
        insta = request.POST["insta"]
        twit = request.POST["twit"]
        lin = request.POST["in"]
        yt =request.POST['yt']
        hub =request.POST['hub']
        lab = request.POST['lab']
        web = request.POST['web']
        user = nameconvert(new_username)
        personal_data=userdata(user)
        userprof = userprofile(full_name =name,email =email,phone_number=phone,
                                address= address,DOB =dob,gender = gender,img = img,
                                ac_type=personal_data.ac_type,username=personal_data.username)
        userprof.save()
        password_update(p=password ,u=new_username)
        return redirect(f'/st/{new_username}/userp')
    else:
        return redirect("/home")

def  password_update(p,u):
    user = nameconvert(u)
    data = User.objects.get(username=user)
    data.set_password(p)
    data.save()