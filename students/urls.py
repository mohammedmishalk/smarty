from django.urls import path
from . import views

urlpatterns = [
    path("<str:new_username>/dash",views.dashboard,name="dashboard"),
    path("<str:new_username>/userp",views.userp,name="user profile"),
    path("<str:new_username>/messages",views.chat,name="chats"),
    path("<str:new_username>/books",views.books,name="books"),
    path("<str:new_username>/course",views.course,name="course"),
    path("<str:new_username>/comp",views.comp,name="competitions"),
    path("<str:new_username>/certificates",views.cert,name="Certificates"),
    path("<str:new_username>/pay",views.pay,name="Subscriptions"),
    path("<str:new_username>/ask",views.ask,name="Questions"),
    path('<str:new_username>/logout',views.logout,name="logout"),
    path('<str:new_username>/edit',views.edit,name="edit"),
]
