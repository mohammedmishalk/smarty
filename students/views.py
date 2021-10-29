from django.http import HttpResponse
from django.shortcuts import render, redirect
from django.contrib.auth.models import User, auth 
from accounts.models import userprofile
from .models import contact

# Create your views here.
def dashboard(request):
    if request.method =='GET' :
        user=request.user.username
        try:
            ud= userdata(user)
        except:
            return redirect('/user')
        if ud.ac_type == 0:
            return redirect(f'/te/dash')
    return render(request,'std_dash.html')


def userp(request):
    if request.method == "GET" :
        user = request.user.username
        user_data = userdata(user)
        return render(request,"std_acc.html",{"user":user_data}) 

def chat(request):
    if request.method == "GET" :
        return render(request,"std_chat.html")

def books(request):
    if request.method == "GET" :
        return render(request,"std_books.html")

def course(request):
    if request.method == "GET" :
        return render(request,"std_course.html")

def comp(request):
    if request.method == "GET" :
        return render(request,"std_comp.html")

def cert(request):
    if request.method == "GET" :
        return render(request,"std_certificate.html")

def ask(request):
    if request.method == "GET" :
        return render(request,"std_ask.html")    

def pay(request):
    if request.method == "GET" :
        return render(request,"std_pay.html")   

def logout(request):
    auth.logout(request)
    return redirect('/')


def userdata(username):
    user = userprofile.objects.get(pk=username)
    return(user)

def edit(request):
    user = request.user.username
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
        personal_data=userdata(user)
        userprof = userprofile(full_name =name,email =email,phone_number=phone,
                                address= address,DOB =dob,gender = gender,img = img,
                                ac_type=personal_data.ac_type,username=personal_data.username)
        userprof.save()
        return redirect(f'/st/userp')
    else:
        return redirect("/home")