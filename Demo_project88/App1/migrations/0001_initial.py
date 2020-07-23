# Generated by Django 2.2.7 on 2020-07-23 06:15

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Student_model',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('roll_no', models.IntegerField(max_length=1000)),
                ('name', models.CharField(max_length=15)),
                ('marks', models.IntegerField(max_length=500)),
            ],
        ),
    ]
