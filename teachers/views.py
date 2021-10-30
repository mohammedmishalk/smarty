from django.http.response import HttpResponse, JsonResponse
from django.shortcuts import render, redirect
from django.contrib.auth.models import auth,User
from accounts.models import userprofile
from course.models import course
from . import models
import random

def dashboard(request):
    return render(request,"card.html")

def userp(request):
    if request.method == 'GET':
        user = request.user.username
        user_data = userdata(user)
        cv_data =cvdata(user)
        contact_data =contactdata(user)
        return render(request,'profile.html',{"user":user_data,"cv":cv_data,"contact":contact_data,})

def ask(request):
    if request.method == 'GET':
        return render(request,'te_ask.html')

def chat(request):
    if request.method == 'GET':
        return render(request,'te_chat.html')

def edit(request):
    user = request.user.username
    if request.method =='GET':
        return render(request,"te_edit.html")
    elif request.method == "POST":
        img=request.FILES['photo']
        name = request.POST["name"]
        email = request.POST["email"]
        address = request.POST["add"]
        password=f"smarty{request.POST['pass']}"
        dob =request.POST['dob']
        personal_data=userdata(user)
        userprof = userprofile(full_name =name,email =email,
                                address= address,DOB =dob,img = img,
                                ac_type=personal_data.ac_type,username=personal_data.username)
        userprof.save()
        return redirect(f'/te/userp')
    else:
        return redirect("/home")


def editc(request):
    user = request.user.username
    if request.method == "POST":
        domain = request.POST["sub"]
        bio = request.POST["bio"]
        qu = request.POST["Qu"]
        ex = request.POST["Ex"]
        personal_data=userdata(user)
        cv = models.Quality(username=user,domain=domain,bio=bio,qu=qu,ex=ex )
        cv.save()
        return redirect(f'/te/userp')
def edits(request):
    user = request.user.username
    if request.method == "POST":
        facebook = request.POST["fb"]
        instagram = request.POST["insta"]
        twitter = request.POST["twit"]
        linked_in = request.POST["in"]
        youtube = request.POST["yt"]
        github = request.POST["hub"]
        gitlab = request.POST["lab"]
        website = request.POST["web"]
        personal_data=userdata(user)
        contact = models.contact(username=user,facebook=facebook,instagram=instagram,twitter=twitter,linked_in=linked_in,youtube=youtube,github=github,gitlab=gitlab,website=website )
        contact.save()
        return redirect(f'/te/userp')
    else:
        return HttpResponse("not working")


def userdata(username):
    user = userprofile.objects.get(pk=username)
    return user

def cvdata(username):
    c_data =models.Quality.objects.get(pk=username)
    return c_data

def contactdata(username):
    codata =models.contact.objects.get(pk=username)
    return codata
    
def earnings(request):
    if request.method == 'GET':
        return render(request,'te_earn.html')

def logout(request):
    auth.logout(request)
    return redirect('/')


def add_course(request):
    if request.method=='POST':
        name = request.POST['cname']
        time = request.POST['time']
        duration= request.POST['duration']
        dic =request.POST['editor1']
        sk =request.POST['skils']
        td=f"{time} {duration}"
        skils=sk.split(',')
        qs={
            "q1":request.POST['tac1'],
            "q2":request.POST['tac2'],
            "q3":request.POST['tac3'],
            "q4":request.POST['tac4'],
            "q5":request.POST['tac5'],
        }
        u= request.user.username
        id = id_generator()
        cs= course(course_id=id,teacher_id=u,name=name,time=td,discriptions=dic,skils=skils,Questions=qs)
        cs.save()
        week=cs.week
        return redirect(f"/te/mycourse")
    else:
        return render(request,"ac_forms.html")
def my_course(request):
    user= request.user.username
    courses= course.objects.filter(teacher_id=user)
    return render(request,"my_courses.html",({"courses":courses}))

def id_generator():
    while True:
        randum_id = random.randint(999,99999)
        if course.objects.filter(course_id=randum_id).exists():
            continue
        else:
            id = randum_id
            break
    return id

