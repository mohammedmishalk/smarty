from django.http.response import HttpResponse, JsonResponse
from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth.models import auth,User
from accounts.models import userprofile
from course.models import Videos, course, img_content,weeks,text_content
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
        return redirect(f"/te/mycourse")
    else:
        return render(request,"ac_forms.html")
def my_course(request):
    user= request.user.username
    courses= course.objects.filter(teacher_id=user)
    return render(request,"my_courses.html",({"courses":courses}))


def course_management(request,course_id):
    user=request.user.username
    data=course.objects.get(pk=course_id)
    return render(request,"st_manage.html",{"data":data})

def course_method(request,course_id,method):
    user= request.user.username
    if method == "U":
        if request.method =='POST':
            if weeks.objects.filter(course_id=course_id).exists():
                data = weeks.objects.get(pk=course_id)
            else:
                w = weeks.objects.get_or_create(pk=course_id)
            data = weeks.objects.get(pk=course_id)
            id = weekIdGenerater(course_id)
            weekList =data.week
            weekList.append(id)
            weekDis =request.POST['editor1']
            time =request.POST['time']
            content= data.content
            content[id]={"discription":weekDis,"time":time,"order":[]}
            week = weeks(course_id=course_id,week=weekList,content=content)
            week.save()
            return render(request,"add_content.html")
        else:
            return render(request,"add_content.html")
    elif method =="P":
        data=course.objects.get(pk=course_id)
        return render(request,"te_course_view.html",({"data":data,"skils":data.skils,"faq":data.Questions,}))
    elif method =="D":
        #deleteCourse(request)
        return redirect("/te/mycourse")
    elif method == "E":
        data=course.objects.get(pk=course_id)
        if request.method=='POST':
            skils=data.skils
            name = request.POST['cname']
            time = request.POST['time']
            dic =request.POST['editor1']
            qs={
            "q1":request.POST['tac1'],
            "q2":request.POST['tac2'],
            "q3":request.POST['tac3'],
            "q4":request.POST['tac4'],
            "q5":request.POST['tac5'],
        }
            u= request.user.username
            cs= course(course_id=course_id,teacher_id=u,name=name,time=time,discriptions=dic,skils=skils,Questions=qs)
            cs.save()
            return redirect("/te/mycourse")
        else:
            return render(request,"course_edit.html",({"data":data,"faq":data.Questions,}))

def add_content(request,ty,course_id):
    if request.method =='POST':
        user= request.user.username
        data = weeks.objects.get(pk=course_id)
        ac=len(data.week)-1
        if ac <0:
            messages.error(request, 'Add a Week before adding Content')
        else:
            active_week=data.week[ac]
            order=data.content[active_week]["order"]
            if ty=='text':    
                name = request.POST["title"]
                text= request.POST["editor1"]
                reference = request.POST["editor2"]
                time = request.POST["time"]
                id = contentIdGenerater(active_week,order)
                id=id+'T'
                course_data = text_content(id=id,name=name,content=text,reference=reference,time=time)
                course_data.save()
                data.content[active_week]["order"].append=[id]
                data.save()
            elif ty=='image':
                name = request.POST["title1"]
                text= request.POST["editor3"]
                reference = request.POST["editor4"]
                time = request.POST["time1"]
                id = contentIdGenerater(active_week,order)
                id=id+"I"
                course_data =img_content(id=id,name=name,text=text,Reference=reference,time=time,img=request.FILES["image"])
                course_data.save()
                data.content[active_week]["order"].append(id)
                data.save()
            elif ty=='video':
                name=request.POST["title3"]
                time=request.POST["time2"]
                id = contentIdGenerater(active_week,order)
                id=id+"V"
                course_data =Videos(id=id,name=name,time=time,video=request.FILES['video'])
                course_data.save()
                data.content[active_week]["order"].append(id)
                data.save()
    return redirect("/te/mycourse/58786/U")


def contentIdGenerater(n,c):
    while True:
        randum_id = random.randint(0,50)
        if randum_id in c:
            continue
        else:
            return n+str(randum_id)

 

def id_generator():
    while True:
        randum_id = random.randint(999,99999)
        if course.objects.filter(course_id=randum_id).exists():
            continue
        else:
            id = randum_id
            break
    return id

def deleteCourse(request):
    print("hallo")

def weekIdGenerater(c_id):
    while True:
        r_id = random.randint(99,999)
        randum_id= f"{c_id}W{r_id}"
        if course.objects.filter(course_id=randum_id).exists():
            continue
        else:
            id = randum_id
            break
    return id

def viewcourse(request,course_id):
    data=weeks.objects.get(pk=course_id)
    a=data.week
    c=data.content
    for item in a:
        d=c[item]["order"]
        m=d[0]
        print(m)
        if m.endswith('I'):
            s=img_content.objects.get(pk=m)
            return render(request,"view.html",{"data":s})
        return render(request,"view.html")