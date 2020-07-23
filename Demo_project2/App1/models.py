from django.db import models
class Student_model(models.Model):
    username=models.IntegerField()
    password=models.CharField(max_length=10)



