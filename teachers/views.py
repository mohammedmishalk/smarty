from django.http.response import HttpResponse, JsonResponse
from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth.models import auth, User
from accounts.models import userprofile, contact, Quality
from course.models import Quiz, Videos, course, img_content, weeks, text_content, regularclass, contentOrder
import random

def dashboard(request):
    return render(request, "card.html")


def userp(request):
    if request.method == 'GET':
        user = request.user.username
        user_data = userdata(user)
        cv_data = cvdata(user)
        contact_data = contactdata(user)
        return render(
            request,
            'profile.html',
            {"user": user_data,
             "cv": cv_data,
             "contact": contact_data, })


def ask(request):
    if request.method == 'GET':
        return render(request, 'te_ask.html')


def chat(request):
    if request.method == 'GET':
        return render(request, 'te_chat.html')


def edit(request):
    user = request.user.username
    if request.method == 'GET':
        return render(request, "te_edit.html")
    elif request.method == "POST":
        personal_data = userdata(user)
        profileData = userprofile.objects.get(pk=user)
        userprof = userprofile(
            img=request.FILES["profile"],
            full_name=request.POST["name"],
            email=request.POST["email"],
            address=request.POST["add"],
            DOB=request.POST['dob'],
            ac_type=personal_data.ac_type,
            username=personal_data.username)
        userprof.save()
        return redirect(f'/te/userp')
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
        return redirect(f'/te/userp')


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
        return redirect(f'/te/userp')
    else:
        return HttpResponse("not working")


def userdata(username):
    user = userprofile.objects.get(pk=username)
    return user


def cvdata(username):
    c_data = Quality.objects.get(pk=username)
    return c_data


def contactdata(username):
    codata = contact.objects.get(pk=username)
    return codata


def earnings(request):
    if request.method == 'GET':
        return render(request, 'te_earn.html')


def logout(request):
    auth.logout(request)
    return redirect('/')


def add_course(request):
    if request.method == 'POST':
        time = request.POST['time']
        duration = request.POST['duration']
        sk = request.POST['skils']
        td = f"{time} {duration}"
        skils = sk.split(',')
        qs = {
            "q1": request.POST['tac1'],
            "q2": request.POST['tac2'],
            "q3": request.POST['tac3'],
            "q4": request.POST['tac4'],
            "q5": request.POST['tac5'],
        }
        u = request.user.username
        id = id_generator(1)
        cs = course(
            course_id=id,
            teacher_id=u,
            name=request.POST['cname'].capitalize(),
            time=td,
            discriptions=request.POST['editor1'],
            skils=skils,
            Questions=qs).save()
        return redirect(f"/te/mycourse")
    else:
        return render(request, "ac_forms.html")


def regular_class(request):
    user = request.user.username
    if request.method == "POST":
        id = id_generator(2)
        hash = hash_generator(id)
        data = regularclass(
            hash=hash,
            class_id=id,
            teacher_id=user,
            name=request.POST["name"],
            institution=request.POST["institution"],
            classDiv=request.POST["class"],
            students=request.POST["students"],
        ).save()
        return redirect("/te/mycourse")

def my_course(request):
    user = request.user.username
    courses = course.objects.filter(teacher_id=user)
    regularClass = regularclass.objects.filter(teacher_id=user)
    return render(
        request,
        "my_courses.html",
        ({"courses": courses,
        "rclass":regularClass}))


def course_management(request, course_id):
    user = request.user.username
    data = course.objects.get(pk=course_id)
    return render(request, "st_manage.html", {"data": data})


def course_method(request, course_id, method):
    user = request.user.username
    if method == 1 :
        if request.method == 'POST':
            w = weeks.objects.get_or_create(pk=course_id)
            data = weeks.objects.get(pk=course_id)
            id = weekIdGenerater(course_id)
            weekList = data.week
            new_week={
                "week_id":id,
                "overview":request.POST['editor1'],
                "time":request.POST['time']
            }
            weekList.append(new_week)
            data.save()
            order = contentOrder(week=id,order=[]).save()
            data = weeks.objects.get(pk=course_id)
            return render(request, "add_content.html", {"data":data})
        else:
            try:
                data = weeks.objects.get(pk=course_id)
            except:
                data = weeks.objects.get_or_create(pk=course_id)
            data = weeks.objects.get(pk=course_id)
            return render(request, "add_content.html",{"data":data})
    elif method == 3:
        data = course.objects.get(pk=course_id)
        return render(request,
                      "te_course_view.html",
                      ({"data": data,
                        "skils": data.skils,
                        "faq": data.Questions, }))
    elif method == 4:
        # deleteCourse(request)
        return redirect("/te/mycourse")
    elif method == 2:
        data = course.objects.get(pk=course_id)
        if request.method == 'POST':
            skils = data.skils
            name = request.POST['cname']
            time = request.POST['time']
            dic = request.POST['editor1']
            qs = {
                "q1": request.POST['tac1'],
                "q2": request.POST['tac2'],
                "q3": request.POST['tac3'],
                "q4": request.POST['tac4'],
                "q5": request.POST['tac5'],
            }
            u = request.user.username
            cs = course(course_id=course_id, teacher_id=u, name=name,
                        time=time, discriptions=dic, skils=skils, Questions=qs)
            cs.save()
            return redirect("/te/mycourse")
        else:
            return render(request, "course_edit.html", ({"data": data, "faq": data.Questions, }))


def week_content_view(request,course_id,week):
    if request.method =='POST':
        order=contentOrder.objects.get_or_create(pk=week)
        order=contentOrder.objects.get(pk=week)
        content_selection = request.POST["content"]
        if content_selection == "1":
            id = contentIdGenerater(week,order.order)
            id = id+'T'
            order.order.append(id)
            course_data = text_content(
                    id=id,
                    course_id=course_id,
                    name=request.POST["title"],
                    content=request.POST["editor1"],
                    reference=request.POST["editor2"],
                    time=request.POST["time"])
            course_data.save()
            order.save()
        elif content_selection == "2":
            id = contentIdGenerater(week,order.order)
            id = id+'I'
            order.order.append(id)
            course_data = img_content(
                    id=id,
                    course_id=course_id,
                    name=request.POST["title1"],
                    text=request.POST["editor3"],
                    Reference=request.POST["editor4"],
                    time=request.POST["time1"],
                    img=request.FILES["image"])
            course_data.save()
            order.save()
        elif content_selection=="3":
            id = contentIdGenerater(week,order.order)
            id = id+'V'
            order.order.append(id)
            course_data = Videos(
                    id=id,
                    course_id=course_id,
                    name=request.POST["title3"],
                    time=request.POST["time2"],
                    video=request.FILES['video'])
            course_data.save()
            order.save()
        elif content_selection=="4":
            pass
        else:
            id = contentIdGenerater(week,order.order)
            id = id+"Q"
            order.order.append(id)
            course_data = Quiz(
                    id=id,
                    name= request.POST["quiz"],
                    totel_point = request.POST["tp"],
                    to_pass = request.POST["ts"],
                    time = request.POST["quiz_time"]
                ).save()
            order.save()
        return redirect(f"/te/mycourse/{course_id}/{week}")
    else:
        q = request.GET.get('id') if request.GET.get('id') != None else ""
        if q =="":
            data = weeks.objects.get(pk=course_id)
            content_order = contentOrder.objects.get_or_create(pk=week)
            content_order = contentOrder.objects.get(pk=week)
            content=[]
            for items in content_order.order:
                if items.endswith("T"):
                    temp = text_content.objects.get_or_create(pk=items)
                    temp = text_content.objects.get(pk=items)
                    content.append(temp)
                elif items.endswith("I"):
                    temp = img_content.objects.get_or_create(pk=items)
                    temp = img_content.objects.get(pk=items)
                    content.append(temp)
                elif items.endswith("V"):
                    temp = Videos.objects.get_or_create(pk=items)
                    temp = Videos.objects.get(pk=items)
                    content.append(temp)
                elif items.endswith("Q"):
                    temp = Quiz.objects.get(pk=items)
                    content.append(temp)
            context = {"data":data,"content":content}

            return render(request, "week_item.html",context)
        else :
            if q.endswith("Q"):
                data = Quiz.objects.get(pk=q) 
                return render(request,"Quiz_update_form.html",{"data":data})
            elif q.endswith("T"):
                data = text_content.objects.get(pk=q) 
                return render(request,"text_content_view.html",{"data":data})
            elif q.endswith("I"):
                data = img_content.objects.get(pk=q) 
                return render(request,"image_content_view.html",{"data":data})
            elif q.endswith("V"):
                data = Videos.objects.get(pk=q) 
                return render(request,"video_content_view.html",{"data":data})


def quiz_update(request,id):
    if request.method =='POST':
        question = Quiz.objects.get(pk=id)
        data={
            "qus": request.POST.get("qus"),
            "opta": request.POST.get("opta"),
            "optb": request.POST.get("optb"),
            "optc": request.POST.get("optc"),
            "optd": request.POST.get("optd"),
            "ans" : request.POST.get("ans")
        }
        question.questions.append(data)
        question.save()
    return HttpResponse("added")

def contentIdGenerater(n, c):
    while True:
        randum_id = random.randint(0, 50)
        temp = n+str(randum_id)
        if temp in c:
            continue
        else:
            return temp

def id_generator(n):
    while True:
        randum_id = random.randint(999, 99999)
        if n == 1:
            if course.objects.filter(course_id=randum_id).exists():
                continue
            else:
                id = randum_id
                break
        else:
            if regularclass.objects.filter(class_id=randum_id).exists():
                continue
            else:
                id = randum_id
                break
    return id

def hash_generator(id):
    hash_code=""
    hash_list=['@','!','$','%','#','&','?','1','2','3','4','5','6','7','8','9','0',
        'q', 'w', 'e', 'r', 't', 'y', 'u', 'i', 'o', 'p', 'a',
        's', 'd', 'f', 'g', 'h', 'j', 'k', 'l', 'z', 'x', 'c',
        'v', 'b', 'n', 'm', 'Q', 'W','E', 'R', 'T', 'Y', 'U',
        'I', 'O', 'P', 'A', 'S', 'D', 'F', 'G', 'H', 'J', 'K',
        'L', 'Z', 'X', 'C', 'V', 'B', 'N', 'M']
    for i in range(12):
        item = random.randint(0,68)
        hash_code += hash_list[item] 
    return hash_code

def deleteCourse(request):
    print("hallo")


def weekIdGenerater(c_id):
    while True:
        r_id = random.randint(99, 999)
        randum_id = f"{c_id}W{r_id}"
        if course.objects.filter(course_id=randum_id).exists():
            continue
        else:
            id = randum_id
            break
    return id


def viewcourse(request, course_id):
    data = weeks.objects.get(pk=course_id)
    a = data.week
    c = data.content
    for item in a:
        d = c[item]["order"]
        m = d[0]
        print(m)
        if m.endswith('I'):
            s = img_content.objects.get(pk=m)
            return render(request, "view.html", {"data": s})
        return render(request, "view.html")
