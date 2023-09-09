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
            messages.warning(request,'Email already Taken')
            return redirect('hod/student')
        if CoustamUser.objects.filter(username=username).exists():
            messages.warning(request,'username already Taken')
            return redirect('hod/student')
        else:# Data seve karne ka tarika 
            user=CoustamUser(
            first_name=first_name,
            last_name=last_name,
            username=username,
            email=email,
            profile_pic=profile_pic,
            user_type=3
            )
            user.set_password(password)
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
            messages.success(request,user.first_name+" "+user.last_name+"are Successfull Add Your acount")
            return redirect('hod/student')
        # print(first_name,last_name,username,email,password,address,course_id,section_year_id,gender,profile_pic)
    context={
        'course':course,
        'session_year':session_year,
    }
    return render(request,'hod/addstudent.html',context)
def view_student(request):
    student=Student.objects.all()
    # print(student)
    context={
        'student':student,
    }
    return render(request,'hod/view_student.html',context)
def edit_student(request ,pk):
    stu=Student.objects.get(id=pk)
    course=Course.objects.all()
    session_year=Session_Year.objects.all()

    context={
        'stu':stu,
        'course':course,
        'session_year':session_year,
    }
    return render(request,'hod/edit_student.html',context)
def Update_student(request):
    if request.method=="POST":
        student_id=request.POST['student_id']
        # print(student_id)
        first_name=request.POST['first_name']
        last_name=request.POST['last_name']
        username=request.POST['username']
        email=request.POST['email']
        password=request.POST['password']
        address=request.POST['address']
        course_id=request.POST.get('course_id')
        session_year_id=request.POST.get('session_year_id')
        gender=request.POST['gender']
        profile_pic=request.FILES['profile_pic']
        user=CoustamUser.objects.get(id=student_id)
        user.first_name=first_name
        user.last_name=last_name
        user.username=username
        user.email=email
        if password!=None and password!="":
            user.set_password(password)
        if profile_pic!=None and profile_pic!="":
                user.profile_pic=profile_pic
        user.save()
        student=Student.objects.get(admin=student_id)
        student.address=address
        student.gender=gender
        course=Course.objects.get(id=course_id)
        student.course_id=course 
        session_year=Session_Year.objects.get(id=session_year_id)
        student.session_year_id=session_year
        student.save()
        print(session_year)
        messages.success(request,'Recourd are successfully Updated')
        return redirect('hod/student')

    return render(request,'hod/edit_student.html')