from django.urls import path
from . import views

urlpatterns = [
    path("dash",views.dashboard,name="dashboard"),
    path("userp",views.userp,name="user profile"),
    path('edit',views.edit,name="edit"),
    path('edits',views.edits,name="edit contact"),
    path('editc',views.editc,name="edit cv"),
    path("messages",views.chat,name="chats"),
    path("books",views.books,name="books"),
    path("course",views.course,name="course"),
    path("course/<int:course_id>/",views.course_preview,name="course preview"),
    path("comp",views.comp,name="competitions"),
    path("certificates",views.cert,name="Certificates"),
    path("pay",views.pay,name="Subscriptions"),
    path("ask",views.ask,name="Questions"),
    path('logout',views.logout,name="logout"),
    path('edit',views.edit,name="edit"),
    path('course/search',views.course_search,name="search course"),
]
