from django.db import models
class Student_model(models.Model):
    roll_no=models.IntegerField(max_length=1000)
    name=models.CharField(max_length=15)
    marks=models.IntegerField(max_length=500)



