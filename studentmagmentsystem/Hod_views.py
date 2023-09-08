from django.shortcuts import render,redirect
from django.contrib.auth.decorators import login_required
from studentapp.models import Course,Session_Year,CoustamUser,Student
from django.contrib import messages

@login_required(login_url='/')
def HodHome(request):
    return render(request,'hod/hodhome.html')
@login_required(login_url='/')
def addstudent(request):
    course=Course.objects.all()
    session_year=Session_Year.objects.all()
    if request.method=="POST":
        first_name=request.POST['first_name']
        last_name=request.POST['last_name']
        username=request.POST['username']
        email=request.POST['email']
        password=request.POST['password']
        address=request.POST['address']
        course=request.POST['course']
        section_year_id=request.POST['section_year_id']
        gender=request.POST['gender']
        profile_pic=request.FILES['profile_pic']
        if CoustamUser.objects.filter(email=email).exists():
            # messages.error(request,'Email already Taken')
            return redirect('student')
        if CoustamUser.objects.filter(username=username).exists():
            # messages.error(request,'username already Taken')
            return redirect('student')
        else:# Data seve karne ka tarika 
            user=CoustamUser(
            first_name=first_name,
            last_name=last_name,
            username=username,
            email=email,
            profile_pic=profile_pic,
            user_type=3
            )
            user.set_password=password
            user.save()
            course=Course.objects.get(id=course)
            session_year=Session_Year.objects.get(id=section_year_id)

            student=Student(
                admin=user,
                address=address,
                session_Year_id=session_year,
                course_id=course,
                gender=gender,

            )
            student.save()
            messages.success(request,'Student are Succssully saved')
            return redirect('student')


        # print(first_name,last_name,username,email,password,address,course_id,section_year_id,gender,profile_pic)

    context={
        'course':course,
        'session_year':session_year,
    }

    return render(request,'hod/addstudent.html',context)