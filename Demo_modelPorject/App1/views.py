from django.shortcuts import render
from App1.models import studentReg_model
from django.http import HttpResponse
from App1.forms import studentReg_form

def registation_view(request):
    myform=studentReg_form()
    return render(request,'reg.html',context={'Myform':myform})

def Insert_data_model(request):
    if(request.method=='POST'):
        myform=studentReg_form(request.POST)
        if(myform.is_valid()):
            roll=myform.cleaned_data['roll_no']
            name=myform.cleaned_data['name']
            mark=myform.cleaned_data['marks']

            myfile=open(name+'.txt','w')

            myfile.write(str(roll)+'\n')
            myfile.write(name+'\n')
            myfile.write(str(mark)+'\n')
            myfile.close()


            studentReg_model.objects.create(roll_no=roll,name=name,marks=mark)
    return HttpResponse("<h1>data inserted successfully</h1>")

def Home_view(request):
    return render(request,'home.html')

