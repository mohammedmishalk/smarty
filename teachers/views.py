from django.http.response import HttpResponse
from django.shortcuts import render, redirect
from django.contrib.auth.models import auth,User
from accounts.models import userprofile, usernameConvart
from students.models import contact

# Create your views here.
def dashboard(request, new_username):
    return render(request,"te_dash.html")

def userp(request, new_username):
    if request.method == 'GET':
        return render(request,'tea_acc.html')

def ask(request, new_username):
    if request.method == 'GET':
        return render(request,'te_ask.html')

def chat(request, new_username):
    if request.method == 'GET':
        return render(request,'te_chat.html')

def edit(request,new_username):
    if request.method =='GET':
        return render(request,"te_edit.html")
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
def nameconvert(n):
    u=usernameConvart.objects.filter(new_username=n)
    s=u[0]
    username = s.username
    return s.username

def userdata(username):
    user = userprofile.objects.get(pk=username)
    return(user)
    
def earnings(request, new_username):
    if request.method == 'GET':
        return render(request,'te_earn.html')

def logout(request , new_username):
    auth.logout(request)
    return redirect('/')

def  password_update(p,u):
    user = nameconvert(u)
    data = User.objects.get(username=user)
    data.set_password(p)
    data.save()
