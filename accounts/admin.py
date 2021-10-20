from django.contrib import admin
from .models import userprofile

class profileAdmin(admin.ModelAdmin):
    list_display=('username','full_name','email','address','DOB','ac_type')
admin.site.register(userprofile,profileAdmin)
