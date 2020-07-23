from django.contrib import admin
from App1.models import studentReg_model

class Studentadmin(admin.ModelAdmin):
    list_display = ['roll_no','name','marks']

# Register your models here.
admin.site.register(studentReg_model,Studentadmin)
