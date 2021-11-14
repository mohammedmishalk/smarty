from django.contrib import admin
from . import models

class courseAdmin(admin.ModelAdmin):
    list_display=('course_id','teacher_id','name','week','unit','enroled','time','rating','skils')

class textContentAdmin(admin.ModelAdmin):
    list_display=('id','name','time')

class imgContentAdmin(admin.ModelAdmin):
    list_display=('id','name','time')


admin.site.register(models.course,courseAdmin)
admin.site.register(models.weeks)


admin.site.register(models.text_content,textContentAdmin)
admin.site.register(models.img_content)



