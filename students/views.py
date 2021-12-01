from django.http import HttpResponse
from django.shortcuts import render, redirect
from django.contrib.auth.models import User, auth 
from django.contrib import messages
from accounts.models import userprofile, contact, Quality
from course import models
from .models import StudentOverview
import datetime

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
        else:
            try:
               data = StudentOverview.objects.get(pk=user) 
            except:
                data = StudentOverview.objects.get_or_create(pk=user) 
            data = StudentOverview.objects.get(pk=user)
            dtls =[]
            for item in data.course_dtls:
                dtls.append(data.course_dtls[item]["teacher"])
    return render(request,'std_dash.html',{"dtls":dtls})


def userp(request):
    if request.method == 'GET':
        user = request.user.username
        user_data = userdata(user)
        cv_data = cvdata(user)
        contact_data = contactdata(user)
        return render(
            request,
            'std_acc.html',
            {"user": user_data,
             "cv": cv_data,
             "contact": contact_data, })

def edit(request):
    user = request.user.username
    if request.method == "POST":
        personal_data = userdata(user)
        userprof = userprofile(
            img= request.FILES["profile"],
            full_name=request.POST["name"],
            email=request.POST["email"],
            address=request.POST["add"],
            DOB=request.POST['dob'],
            ac_type=personal_data.ac_type,
            username=personal_data.username).save()
        return redirect(f'/st/userp')
    else:
        return redirect("/home")

def editc(request):
    user = request.user.username
    if request.method == "POST":
        personal_data = userdata(user)
        cv = Quality(
            username=user,
            domain=request.POST["sub"],
            bio=request.POST["bio"],
            qu=request.POST["Qu"],
            ex=request.POST["Ex"])
        cv.save()
        return redirect(f'/st/userp')

def edits(request):
    user = request.user.username
    if request.method == "POST":
        personal_data = userdata(user)
        cont = contact(
            username=user,
            facebook=request.POST["fb"],
            instagram=request.POST["insta"],
            twitter=request.POST["twit"],
            linked_in=request.POST["in"],
            youtube=request.POST["yt"],
            github=request.POST["hub"],
            gitlab=request.POST["lab"],
            website=request.POST["web"]).save()
        return redirect(f'/st/userp')
    else:
        return HttpResponse("not working")

def cvdata(username):
    c_data = Quality.objects.get(pk=username)
    return c_data


def contactdata(username):
    codata = contact.objects.get(pk=username)
    return codata

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



def course_search(request):
    keyword = request.GET["keyword"].lower()
    if request.GET["type"] == "1" :
        if models.course.objects.filter(course_id=keyword).exists():
            data = models.course.objects.get(pk=keyword)
            teacher = data.teacher_id
            teacher_pro = userprofile.objects.get(pk=teacher)
            return render(request,'std_course.html',{"data":data,"teacher":teacher_pro})
        else:
            messages.error(request, "no course with this ID")
            return redirect("/st/course")
    if request.GET["type"] == "2" :
        if models.course.objects.filter(name=keyword).exists():
            data = models.course.objects.get(name=keyword)
            return HttpResponse(data.discriptions)
        else:
            messages.error(request, "no course with this name")
            return redirect("/st/course")
    if request.GET["type"] == "3" :
        if models.course.objects.filter(name=keyword).exists():
            data = models.course.objects.get(name=keyword)
            return HttpResponse(data.discriptions)
        else:
            messages.error(request, "no course with this keyword")
            return redirect("/st/course")

    return HttpResponse(keyword)

def course_preview(request,course_id):
    data = models.course.objects.get(pk=course_id)
    return render(
        request,
        "std_course_view.html",
        ({"data": data,
        "skils": data.skils,
        "faq": data.Questions, }))

def course_enroll(request,course_id):
    user = request.user.username 
    if User.is_authenticated:
        try:
            overview = StudentOverview.objects.get(pk=user)
        except:
            overview = StudentOverview.objects.get_or_create(pk=user)
        overview = StudentOverview.objects.get(pk=user)
        if course_id in overview.course_dtls:
            messages.error(request,"Alredy enroled")
        else:
            date_obj = datetime.datetime.now()
            date_enroled=f"{date_obj.day}:{date_obj.month}:{date_obj.year}"
            data = models.course.objects.get(pk=course_id)
            teacher = data.teacher_id
            new_data = {
                course_id:{
                    "teacher": teacher,
                    "completed" : "0%",
                    "progress" : {},
                    "doe" :date_enroled,
                    "doc" :""
                }
            }
            overview.course_dtls.update(new_data)
            overview.std_skils=[]
            overview.save()

            return redirect("/st/dash")
    else:
        return redirect("/")