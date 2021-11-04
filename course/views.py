from django.http.response import HttpResponse, ResponseHeaders
from django.shortcuts import redirect,render
from . import models

def course(request,course_id):
    data=models.course.objects.get(pk=course_id)
    print(data.skils)
    return render(request,"course.html",{"data":data})
