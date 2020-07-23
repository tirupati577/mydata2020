from django.shortcuts import render
from datetime import datetime
from App1 import forms
from django.http import HttpResponse
import pickle

def home_view(request):
    date=datetime.now()#it will gives current date and time of the system
    return render(request,'home.html',context={'Date':date})

def registration_view(request):

    return render(request,'registration.html',)

def login_view(request):
    return render(request,'login.html')

def getdata_view(request):
    #reading the data which is send by registration
    id=request.GET.get('rollno')
    name= request.GET.get('sname')
    marks=request.GET.get('marks')
    dob=request.GET.get('date')
    gender=request.GET.get('gender')
    checkbox1=request.GET.get('checkbox1')
    checkbox2 = request.GET.get('checkbox2')
    checkbox3 = request.GET.get('checkbox3')
    city=request.GET.get('city')
    address=request.GET.get('address')

    return render(request,'success.html',context={
                                                   'Id':id,
                                                   'Name':name,
                                                    'Marks':marks,
                                                    'DOB':dob,
                                                    'Gender':gender,
                                                    'Checkbox1':checkbox1,
                                                    'Checkbox2': checkbox2,
                                                    'Checkbox3': checkbox3,
                                                     'City':city,
                                                    'Address':address
                                           })

def getdatapost_view(request):
    # reading the data which is send by registration
    id = request.POST.get('rollno')
    name = request.POST.get('sname')
    marks = request.POST.get('marks')
    dob = request.POST.get('date')
    gender = request.POST.get('gender')
    checkbox1 = request.POST.get('checkbox1')
    checkbox2 = request.POST.get('checkbox2')
    checkbox3 = request.POST.get('checkbox3')
    city = request.POST.get('city')
    address = request.POST.get('address')

    return render(request, 'success.html', context={
        'Id': id,
        'Name': name,
        'Marks': marks,
        'DOB': dob,
        'Gender': gender,
        'Checkbox1': checkbox1,
        'Checkbox2': checkbox2,
        'Checkbox3': checkbox3,
        'City': city,
        'Address': address
    })

def readLogin_view(request):
    user_name=request.GET.get('uname')
    password=request.GET.get('pname')

    if(user_name=='sonu' and password=='monu'):
        s='welcome '+user_name+ 'user!!!'
    else:
        s='invalid Login Credentials!!!'

    return render(request,'success_login.html',context={'data':s})

def Student_formview(request):
    myform=forms.Student_loginform()#creating the object
    return render(request,'studentlogin.html',context={'Myform':myform})

def stdform_login_view(request):
    user_name = request.POST.get('username')
    password = request.POST.get('password')

    if (user_name == 'sonu' and password == 'monu'):
        s = 'welcome ' + user_name + 'user!!!'
    else:
        s = 'invalid Login Credentials!!!'

    return render(request,'success_login.html',context={'data':s})

def senddata_fileview(request):

    myfile=open('ravisharama.txt','w')
    myfile.write('name')
    myfile.write('user-name')


    return HttpResponse("<h1> file is Created...")
