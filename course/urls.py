from django.urls import path
from . import views

urlpatterns = [
    path("add",views.add_course,name="add course"),
]

