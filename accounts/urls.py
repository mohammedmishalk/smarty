from django.urls import path
from . import views

urlpatterns = [
    path("",views.home,name="home"),
    path("user",views.user,name="user"),
    path('logout',views.logout,name="logout"),
    path('about',views.about,name="about"),
    path('contact',views.contact,name="contact"),
    path('register',views.register,name="register"),
    path('login',views.login,name="login"),
]
