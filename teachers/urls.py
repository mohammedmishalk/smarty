from django.urls import path
from . import views

urlpatterns = [
    path('dash',views.dashboard,name="dashboard"),
    path('user',views.userp,name="user profile"),
    path("userp",views.userp,name="user profile"),
    path('ask',views.ask,name="smarty ask"),
    path('chat',views.chat,name="smarty chat"),
    path('earnings',views.earnings,name="earnings"),
    path('logout',views.logout,name="logout"),
    path('edit',views.edit,name="edit"),
    path('addcourse',views.add_course,name="add course"),
    path('regular',views.regular_class,name="add regular class"),
    path("mycourse",views.my_course,name="course dashbord"),
    path("mycourse/<int:course_id>/",views.course_management,name="course view"),
    path("mycourse/<int:course_id>/<int:method>",views.course_method,name="course method"),
    path("mycourse/<int:course_id>/<str:week>",views.week_content_view,name="week content"),
    path('editc',views.editc,name="edit cv"),
    path('mycourse/<int:course_id>/add/<str:ty>',views.add_content,name="add course content"),
    path('edits',views.edits,name="edit contact"),
    path('view/<int:course_id>',views.viewcourse,name="view content"),

]
