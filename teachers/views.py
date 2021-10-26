from django.http.response import HttpResponse
from django.shortcuts import render, redirect
from django.contrib.auth.models import auth,User
from accounts.models import userprofile, usernameConvart
from course.models import course
from . import models
import random

# Create your views here.
def dashboard(request, new_username):
    print(request.user.username)
    return render(request,"card.html")

def userp(request, new_username):
    if request.method == 'GET':
        user = nameconvert(new_username)
        user_data = userdata(user)
        cv_data =cvdata(user)
        contact_data =contactdata(user)
        return render(request,'profile.html',{"user":user_data,"cv":cv_data,"contact":contact_data,})

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
        address = request.POST["add"]
        password=f"smarty{request.POST['pass']}"
        dob =request.POST['dob']
        user = nameconvert(new_username)
        personal_data=userdata(user)
        userprof = userprofile(full_name =name,email =email,
                                address= address,DOB =dob,img = img,
                                ac_type=personal_data.ac_type,username=personal_data.username)
        userprof.save()
        password_update(p=password ,u=new_username)
        return redirect(f'/te/{new_username}/userp')
    else:
        return redirect("/home")


def editc(request, new_username):
    if request.method == "POST":
        domain = request.POST["sub"]
        bio = request.POST["bio"]
        qu = request.POST["Qu"]
        ex = request.POST["Ex"]
        user = nameconvert(new_username)
        personal_data=userdata(user)
        cv = models.Quality(username=personal_data.username,domain=domain,bio=bio,qu=qu,ex=ex )
        cv.save()
        return redirect(f'/te/{new_username}/userp')
def edits(request, new_username):
    if request.method == "POST":
        facebook = request.POST["fb"]
        instagram = request.POST["insta"]
        twitter = request.POST["twit"]
        linked_in = request.POST["in"]
        youtube = request.POST["yt"]
        github = request.POST["hub"]
        gitlab = request.POST["lab"]
        website = request.POST["web"]
        user = nameconvert(new_username)
        personal_data=userdata(user)
        contact = models.contact(username=personal_data.username,facebook=facebook,instagram=instagram,twitter=twitter,linked_in=linked_in,youtube=youtube,github=github,gitlab=gitlab,website=website )
        contact.save()
        return redirect(f'/te/{new_username}/userp')
    else:
        return HttpResponse("not working")


def nameconvert(n):
    u=usernameConvart.objects.filter(new_username=n)
    s=u[0]
    username = s.username
    return s.username

def userdata(username):
    user = userprofile.objects.get(pk=username)
    return user

def cvdata(username):
    c_data =models.Quality.objects.get(pk=username)
    return c_data

def contactdata(username):
    codata =models.contact.objects.get(pk=username)
    return codata
    
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

def add_course(request,new_username):
    if request.method=='POST':
        name = request.POST.get('name')
        time = request.POST.get('time')
        duration= request.POST.get('dr')
        dic =request.POST.get('dis')
        sk =request.POST.get('skils')
        td=f"{time} {duration}"
        skils=sk.split(',')
        u=nameconvert(new_username)
        id = id_generator()
        cs= course(course_id=id,techer_id=u,name=name,time=td,desciptions=dic,skils=skils)
        cs.save()
        week=cs.week
        return redirect(f"acw/{id}/{week}")
    else:
        return render(request,"ac_forms.html")

def id_generator():
    while True:
        randum_id = random.randint(999,99999)
        if course.objects.filter(course_id=randum_id).exists():
            continue
        else:
            id = randum_id
            break
    return id

def acw(request,new_username,course_id,week):
    if request.method =='POST':
        pass
    else:
        return HttpResponse("ready") 

