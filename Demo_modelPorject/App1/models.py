from django.db import models
class studentReg_model(models.Model):
    #we can write here attributes as a column
    roll_no=models.IntegerField()
    name=models.CharField(max_length=15)
    marks=models.IntegerField()

class Meta:
    db_table='studentReg_model'

