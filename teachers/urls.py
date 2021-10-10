from django.urls import path
from . import views

urlpatterns = [
    path('<str:new_username>/dash',views.dashboard,name="dashboard"),
    path('<str:new_username>/user',views.userp,name="user profile"),
    path('<str:new_username>/ask',views.ask,name="smarty ask"),
    path('<str:new_username>/chat',views.chat,name="smarty chat"),
    path('<str:new_username>/earnings',views.earnings,name="earnings"),
    path('<str:new_username>/logout',views.logout,name="logout"),
    path('<str:new_username>/edit',views.edit,name="edit"),
    path('<str:new_username>/addcourse',views.add_course,name="add course")

]
