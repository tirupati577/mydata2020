# Generated by Django 2.2.7 on 2020-07-20 11:21

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
                ('username', models.IntegerField()),
                ('password', models.CharField(max_length=10)),
            ],
        ),
    ]