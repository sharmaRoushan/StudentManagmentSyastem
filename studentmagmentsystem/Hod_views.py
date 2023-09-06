from django.shortcuts import render,redirect
from django.contrib.auth.decorators import login_required
from studentapp.models import Course, Session_Year





@login_required(login_url='/')
def HodHome(request):
    return render(request,'hod/hodhome.html')
@login_required(login_url='/')
def addstudent(request):
    course=Course.objects.all()
    session_year=Session_Year.objects.all()
    # print(course)
    # print(session_year)
    context={
        'course':course,
        'session_year':session_year,
    }

    return render(request,'hod/addstudent.html',context)