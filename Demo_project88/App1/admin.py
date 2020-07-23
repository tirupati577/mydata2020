from django.contrib import admin
from App1.models import Student_model

class Student_admin(admin.ModelAdmin):
    list_display = ['roll_no','name','marks']

# Register your models here.
admin.site.register(Student_model,Student_admin)
