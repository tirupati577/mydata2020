from django import forms



class Student_loginform(forms.Form):
    username=forms.CharField(label="Enter the user-name",max_length=15)
    password = forms.CharField(max_length=10, widget=forms.PasswordInput)