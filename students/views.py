from django import http
from django.http import HttpResponse, request
from django.shortcuts import render, redirect
from django.contrib.auth.models import User, auth 
from django.contrib import messages
from django.db.models import Q
from accounts.models import userprofile, contact, Quality
from course import models
from .models import StdOverview, skilsNcourse, completed, studentScore

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
            data = StdOverview.objects.filter(std_id=user) 
            context = {"data":data}
    return render(request,'std_dash.html',context)


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
    data = models.course.objects.filter(Q(name__icontains= keyword) | Q(course_id=keyword) | Q(skils__icontains = keyword) )
    return render(request,'std_course.html',{"content":data})

def course_preview(request,course_id):
    if request.method =="POST":
        user = request.user.username 
        if User.is_authenticated:
            try:
                overview = skilsNcourse.objects.get(pk=user)
            except:
                overview = skilsNcourse.objects.get_or_create(pk=user)
            overview = skilsNcourse.objects.get(pk=user)
            if course_id in overview.courses:
                messages.error(request,"Alredy enroled")
                return redirect("/st/course")
            else:
                overview.courses.append(course_id)
                course_dtls = models.course.objects.get(pk=course_id)
                course_dtls.enroled +=1;
                course_dtls.save()
                data = models.course.objects.get(pk=course_id)
                overview.save()
                StdOverview(id=f"{user} {course_id}",std_id=user,cour_name=data.name,thr_id=data.teacher_id).save()
                return redirect("/st/dash")
        else:
            return redirect("/")
    else:
        data = models.course.objects.get(pk=course_id)
        return render(
            request,
            "std_course_view.html",
            ({"data": data,
            "skils": data.skils,
            "faq": data.Questions, }))

def Weeks_view(request,course_id):
    user = request.user.username
    cmplt = completed.objects.get_or_create(stud_id=user,course_id=course_id)
    cmplt = completed.objects.get(stud_id=user,course_id=course_id)
    cmplt_weeks = cmplt.completed_weeks
    cour_week = models.weeks.objects.get(pk=course_id)
    if cmplt.completed == True:
        return HttpResponse(cmplt.completed)
    elif len(cmplt_weeks)==0:
        active_week = cour_week.week[0]
        acw=0
    else:
        count=0
        for item in cour_week.week: 
            if cmplt_weeks[-1] ==item:
                if cour_week.week[-1]==item:
                    contents= models.contentOrder.objects.get(pk=item["week_id"]) 
                    if len(cmplt_weeks)==len(contents.order):
                        cmplt.completed=True
                        cmplt.save()
                        return HttpResponse("Course completed")
                    else:
                        c=0
                        for i in cour_week.week:
                            data = models.contentOrder.objects.get(pk=i['week_id'])
                            for j in data.order :
                                if j not in cmplt.completed_content:
                                    return redirect(f"/st/ls/{course_id}/{c}/{j}")
                                    c=c+1
                else:
                    active_week = cour_week.week[count+1]
                    acw=count+1
            count+=1
    order = models.contentOrder.objects.get(pk=active_week["week_id"])
    std_view = StdOverview.objects.get(std_id=user,cour_id=course_id)
    count=0
    for item in order.order :
        if std_view.progress["last"] == item:
            if order.order[-1]==item:
                data = completed.objects.get_or_create(stud_id=user,course_id=course_id)
                data = completed.objects.get(stud_id=user,course_id=course_id)
                week = data.completed_weeks
                week.append(cour_week.week[acw])
                data.save()
                messages.info(request,"This week successfully completed go for next week")
            else:
                return redirect(f"/st/ls/{course_id}/{acw}/{order.order[count+1]}")
        count+=1
    count=0
    return redirect(f"/st/ls/{course_id}/{acw}/{order.order[count]}")


def lesson(request,course_id,week,cont):
    if request.method == 'POST':
        if cont.endswith("Q"):
            content = models.Quiz.objects.get(pk=cont)
            answers =[]
            user_answer=[]
            for question in content.questions:
                answers.append(question["ans"])
            for item in request.POST:
                if item !="csrfmiddlewaretoken":
                    user_answer.append(request.POST[item])
            total_mark = 0
            for i in range(len(answers)):
                if user_answer[i] == answers[i]:
                    total_mark+=content.questions[i]["m"]
            if studentScore.objects.filter(course_id=course_id,stud_id = request.user.username ).exists():
                pass
            else:
                score = studentScore(course_id=course_id,stud_id = request.user.username).save()
            score = studentScore.objects.get(course_id=course_id,stud_id = request.user.username)
            for item in score.exam:
                if item["content_id"] == cont:
                    score.exam.remove(item)
                    score.save()
            passed = False
            messages = "Faild"
            if total_mark >= content.to_pass:
                passed = True
                messages = "Passed"
            exam = {"content_id":cont,
                    "mark" : total_mark,
                    "status" : passed
                    }
            score.exam.append(exam)
            score.save()
        return HttpResponse(f" you are scored {total_mark} <br> statuse {messages}")
    else:
        cour_week = models.weeks.objects.get(pk=course_id)
        active_week = cour_week.week[week]
        order = models.contentOrder.objects.get(pk=active_week["week_id"])
        if cont.endswith("T"):
            content = models.text_content.objects.get(pk=cont)
            return render(
                request,
                "text_content.html",
                {
                    "content":content,
                    "order":order,
                    "weeks":cour_week.week
                    })
        elif cont.endswith("I"):
            content = models.img_content.objects.get(pk=cont)
            return render(
                request,
                "image_content.html",
                {
                    "content":content,
                    "order":order,
                    "weeks":cour_week.week               })
        elif cont.endswith("V"):
            content = models.Videos.objects.get(pk=cont)
            return render(
                request,
                "video_content.html",
                {
                    "content":content,
                    "order":order,
                    "weeks":cour_week.week
                })
        elif cont.endswith("Q"):
            content = models.Quiz.objects.get(pk=cont)
            return render(
                request,
                "quiz_content.html",
                {
                    "content":content,
                    "order":order,
                    "weeks":cour_week.week
                }
            )
def choice(request,course_id,cont,week,choice):
    if choice==1:
        user = request.user.username
        data = completed.objects.get_or_create(stud_id=user,course_id=course_id)
        data = completed.objects.get(stud_id=user,course_id=course_id)
        content = data.completed_content
        if cont not in content:
            content.append(cont)
            data.save()
            std_view= StdOverview.objects.get(std_id=user,cour_id=course_id)
            std_view.progress={"last":cont}
            std_view.save()
            messages.info(request,"Marked as finished")
            return redirect(f"/st/ls/{course_id}/{week}/{cont}")
        else:
            messages.error(request,"alredy finished go for next topic")
            return redirect(f"/st/ls/{course_id}/{week}/{cont}")
    else :
        messages.error(request,"Unit skiped ")
        return redirect(f"/st/ls/{course_id}/{week}/{cont}")
    