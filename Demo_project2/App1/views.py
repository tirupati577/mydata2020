from django.shortcuts import render
from App1 import forms
def registration_view(request):
    myform=forms.Student_form()
    return render(request,'registration.html',context={'MyForm':myform})

def send_dataview(request):
    myform = forms.Student_form()
    if(request.method=='POST'):
        myform=forms.Student_form(request.POST)
        if myform.is_valid():
            uname=myform.cleaned_data['uname']
            password=myform.cleaned_data['password']

    return render(request,'success.html',context={'Username':uname,'Password':password})


