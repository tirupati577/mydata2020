from django import forms
class Student_form(forms.Form):
    uname=forms.CharField(max_length=15)
    password=forms.CharField(max_length=10,widget=forms.PasswordInput)
