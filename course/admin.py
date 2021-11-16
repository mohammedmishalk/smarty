from django.contrib import admin
from . import models

class courseAdmin(admin.ModelAdmin):
    list_display=('course_id','teacher_id','name','week','unit','enroled','time','rating','skils')

class regularclassAdmin(admin.ModelAdmin):
    list_display = ('class_id','teacher_id','name','institution','classDiv','students')

class textContentAdmin(admin.ModelAdmin):
    list_display=('id','name','time')

class imgContentAdmin(admin.ModelAdmin):
    list_display=('id','name','time')


admin.site.register(models.course,courseAdmin)
admin.site.register(models.regularclass,regularclassAdmin)

admin.site.register(models.weeks)


admin.site.register(models.text_content,textContentAdmin)
admin.site.register(models.img_content)



