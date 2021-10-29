from django.urls import path
from . import views

urlpatterns = [
    path("dash",views.dashboard,name="dashboard"),
    path("userp",views.userp,name="user profile"),
    path("messages",views.chat,name="chats"),
    path("books",views.books,name="books"),
    path("course",views.course,name="course"),
    path("comp",views.comp,name="competitions"),
    path("certificates",views.cert,name="Certificates"),
    path("pay",views.pay,name="Subscriptions"),
    path("ask",views.ask,name="Questions"),
    path('logout',views.logout,name="logout"),
    path('edit',views.edit,name="edit"),
]
