from django.shortcuts import render,redirect
from django.contrib.auth.decorators import login_required
from studentapp.models import Course,Session_Year,CoustamUser,Student,Staff,Subject,Staff_notification,Staff_leave,Feedback,Student_notification,Student_feedback,Student_leave,Attendance,Attendance_Report
from django.contrib import messages
@login_required(login_url='/')
def HodHome(request):
    student_count=Student.objects.all().count()
    satff_count=Staff.objects.all().count()
    course_count=Course.objects.all().count()
    subject_count=Subject.objects.all().count()
    student_gender_male=Student.objects.filter(gender='male').count()
    student_gender_female=Student.objects.filter(gender='female').count()
    # print(student_gender_male)
    # print(student_gender_female)

    context={
        'student_count':student_count,
        'satff_count':satff_count,
        'course_count':course_count,
        'subject_count':subject_count,
        'student_gender_male':student_gender_male,
        "student_gender_female":student_gender_female
    }
    # print(context)
    return render(request,'hod/hodhome.html',context)
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
            messages.success(request,user.first_name+" "+user.last_name+"   are Successfull Add Your acount")
            return redirect('hod/student')
        # print(first_name,last_name,username,email,password,address,course_id,section_year_id,gender,profile_pic)
    context={
        'course':course,
        'session_year':session_year,
    }
    return render(request,'hod/addstudent.html',context)
@login_required(login_url='/')
def view_student(request):
    student=Student.objects.all()
    # print(student)
    context={
        'student':student,
    }
    return render(request,'hod/view_student.html',context)
@login_required(login_url='/')
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
@login_required(login_url='/')

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
        session_Year_id=request.POST['session_Year_id']
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
        session_year=Session_Year.objects.get(id=session_Year_id)
        student.session_Year_id=session_year
        student.save()
        # print(session_year)
        messages.success(request,'Recourd are successfully Updated')
        return redirect('hod/student')

    return render(request,'hod/edit_student.html')
@login_required(login_url='/')
def Dilite_Student(request,pk):
    user=Student.objects.get(id=pk)
    user.delete()
    return redirect('hod/student')
@login_required(login_url='/')

def course_add(request):
    if request.method== "POST":
        course_add=request.POST.get('course_add')
        course=Course(
            course_name=course_add
        )
        course.save()
        return redirect('view_course')
        messages.success(request,'course are successfully created')

    return render(request,'hod/add_course.html')
@login_required(login_url='/')

def view_course(request):
    course=Course.objects.all()
    # print(course)
    context={
        'course':course
    }
    return render (request,'hod/view_course.html',context)
@login_required(login_url='/')

def edit_course(request,pk):
    course=Course.objects.get(id=pk)
    context={
        'course':course
    }

    return render(request,'hod/edit_course.html',context)
@login_required(login_url='/')

def update_course(request):
    if request.method=="POST":
        course_name=request.POST.get('course_name')
        course_id=request.POST.get('course_id')
        # print(course_name,course_id)
        course=Course.objects.get(id=course_id)
        course.course_name=course_name
        course.save()
        messages.success(request,'Course is successfull updated')
        return redirect('view_course')


    return render(request,'hod/edit_course.html')
@login_required(login_url='/')

def dilite_course(request,pk):
    course=Course.objects.get(id=pk)
    course.delete()
    messages.success(request,'Course are successfull delete')
    return redirect('view_course')
@login_required(login_url='/')
def add_Staff(request):
    if request.method== "POST":
        first_name=request.POST['first_name']
        last_name=request.POST['last_name']
        username=request.POST['username']
        email=request.POST['email']
        password=request.POST['password']
        address=request.POST['address'] 
        gender=request.POST['gender']
        profile_pic=request.FILES['profile_pic']
        # print(first_name,last_name,username,email,password,profile_pic)
        if CoustamUser.objects.filter(email=email).exists():# check the email
            messages.warning(request,'Email all ready Taken') 
            return redirect('view_staff')
        if CoustamUser.objects.filter(username=username).exists():# check the username address
            messages.warning(request,'Username alreay taken')
            return redirect('view_staff')
        else:
            user=CoustamUser(
            first_name=first_name,
            last_name=last_name,
            username=username,
            email=email,
            profile_pic=profile_pic,
            user_type=2
            )
            user.set_password(password)
            user.save()
            staff=Staff(
                admin=user,
                address=address,
                gender=gender
            )
            staff.save()
            messages.success(request,'staff are successfully Added')
            return redirect('view_staff')
    return render(request,'hod/add_staff.html')
@login_required(login_url='/')

def view_staff(request):
    staff=Staff.objects.all()
    context={
        'staff':staff,
    }
    return render(request,'hod/view_staff.html',context)
@login_required(login_url='/')

def edit_staff(request, pk):
    staff=Staff.objects.get(id=pk)
    context={
        'staff':staff,
    }
    return render(request,'hod/edit_staff.html',context)
@login_required(login_url='/')

def update_staff(request):
    if request.method=="POST":
        staff_id=request.POST['staff_id']
        # print(staff_id)
        first_name=request.POST['first_name']
        last_name=request.POST['last_name']
        username=request.POST['username']
        email=request.POST['email']
        password=request.POST['password']
        address=request.POST['address']
        gender=request.POST['gender']
        profile_pic=request.FILES['profile_pic']
        user=CoustamUser.objects.get(id=staff_id)
        user.username=username
        user.first_name=first_name
        user.last_name=last_name
        user.email=email
        if password!=None and password!="":
            user.set_password(password)
        if profile_pic!=None and profile_pic!="":
            user.profile_pic=profile_pic
        user.save()
        staff=Staff.objects.get(admin=staff_id)
        staff.address=address
        staff.gender=gender
        staff.save()
        messages.success(request,'Recourd are successfull updated')
        return redirect('view/staff')
    return render(request,'hod/edit_staff.html')
@login_required(login_url='/')

def dilite_staff(request,pk):
    staff=Staff.objects.get(id=pk)
    staff.delete()
    return redirect('view_staff')
@login_required(login_url='/')
def add_subject(request):
    course=Course.objects.all()
    staff=Staff.objects.all()
    if request.method == "POST":
        subject_name=request.POST['subject_name']
        course_id=request.POST['course_id']
        staff_id=request.POST.get('staff_id')

        course=Course.objects.get(id=course_id)
        staff=Staff.objects.get(id=staff_id)
       
        subject=Subject(
            subject_name=subject_name,
            course=course,
            staff=staff
        )
        subject.save()
        messages.success(request,'add  subject successfuly')
        return redirect('view_subject')
    context={
        'course':course,
        'staff':staff
    }

    return render(request,'hod/add_subject.html',context)
@login_required(login_url='/')
def view_subject(request):
    subject=Subject.objects.all()
    context={
        'subject':subject,
       
    }
    return render(request,'hod/view_subject.html',context)
@login_required(login_url='/')
def edit_subject(request,pk):
    subject=Subject.objects.get(id=pk)
    course=Course.objects.all()
    staff=Staff.objects.all()
    context={
        'subject':subject,
        'course':course,
        'staff':staff,
    }
    return render(request,'hod/edit_subject.html',context)
@login_required(login_url='/')
def update_subject(request):
    if request.method == "POST":
        subject_id=request.POST['subject_id']
        # print(subject_id)
        course_id=request.POST['course_id']
        staff_id=request.POST['staff_id']
        subject_name=request.POST['subject_name']
        course=Course.objects.get(id=course_id)
        staff=Staff.objects.get(id=staff_id)
        subject=Subject(
            id =subject_id,
            subject_name=subject_name,
            course=course,
            staff=staff
        )
        subject.save()
        messages.success(request,'Successfully updated')
        return redirect('view_subject')

    return render(request,'hod/edit_subject.html')
@login_required(login_url='/')
def subject_delete(request,pk):
    subject=Subject.objects.get(id=pk)
    subject.delete()
    return redirect('view_subject')
@login_required(login_url='/')
def add_session(request):
    if request.method == "POST":
        session_start=request.POST['session_start']
        session_end=request.POST['session_end']
        # print(session_start,session_end)
        session=Session_Year(
            session_start=session_start,
            session_end=session_end
        )
        session.save()
        messages.success(request,'Session Year successfully added')
        return redirect('view_session')
    return render(request,'hod/add_session.html')
@login_required(login_url="/")
def view_session(request):
    session=Session_Year.objects.all()
    context={
        'session':session,
    }
    return render(request,'hod/view_session.html',context)
@login_required(login_url="/")
def edit_session(request,pk):
    session=Session_Year.objects.get(id=pk)
    # print(session)
    context={
        'session':session,
    }
    return render(request,'hod/edit_session.html',context)
@login_required(login_url="/")
def update_session(request):
    if request.method == "POST":
        session_id=request.POST['session_id']
        session_start=request.POST['session_start']
        session_end=request.POST['session_end']
        session=Session_Year(
            id=session_id,
            session_start=session_start,
            session_end=session_end
        )
        session.save()
        messages.success(request,'session are Successfully Updated')
        return redirect('view_session')
    return render (request,'hod/edit_session.html')
@login_required(login_url="/")
def delete_session(request,pk):
    session=Session_Year.objects.get(id=pk)
    session.delete()
    return redirect('view_session')
@login_required(login_url="/")
def Send_notification(request):
    staff=Staff.objects.all()
    see_notification=Staff_notification.objects.all().order_by('-id')[0:5]
    context={
        'staff':staff,
        'see_notification':see_notification,
    }
    print(context)
    return render(request,'hod/send_notification.html',context)
@login_required(login_url="/")
def save_staff_notification(request):
    if request.method == "POST":
        staff_id=request.POST.get('staff_id')
        massage=request.POST.get('massage')
        staff=Staff.objects.get(admin=staff_id)
        notified=Staff_notification(
            staff_id=staff, 
            message=massage,
        )
        notified.save()
        messages.success(request,"notification's successfully sent")
        return redirect ('send_notification')
@login_required(login_url="/")
def Sataf_leave_view(request):
    staff_leave=Staff_leave.objects.all() 
    context={
      'staff_leave':staff_leave,                               

    }
    return render(request,'hod/staff_leave_view.html',context)
@login_required(login_url="/")
def Staff_approve_leave(request,pk):
    leave=Staff_leave.objects.get(id=pk)
    leave.status=1
    leave.save()
    return redirect('holiday_view')
@login_required(login_url="/")
def Staff_dissapprove_leave(request,pk):
    leave=Staff_leave.objects.get(id=pk)
    leave.status=2
    leave.save()
    return redirect('holiday_view')
@login_required(login_url="/")
def Staff_feedback(request):
    feedback=Feedback.objects.all()
    context={
        'feedback':feedback
    }
    return render(request,'hod/staff_feedback.html',context)
@login_required(login_url="/")
def staff_feedback_reply_save(request):
    if request.method=="POST":
        feedback_id=request.POST['feedback_id']
        feedback_reply=request.POST['feedback_reply']
        feedback=Feedback.objects.get(id=feedback_id)
        feedback.feedback_reply=feedback_reply
        feedback.status=1
        feedback.save()
        return redirect('staff_feedback')
@login_required(login_url="/")
def Send_student_notification(request):
    student= Student.objects.all()
    notification=Student_notification.objects.all()
    context={
        'student':student,
        'notification':notification
    }
    return render(request,'hod/send_student_notification.html',context)
@login_required(login_url="/")
def Save_student_notification(request):
    if request.method=="POST":
        massage=request.POST['massage']
        student_id=request.POST.get('student_id')
        # print(massage,student_id)
        student=Student.objects.get(admin=student_id)
        student_notification=Student_notification(
            student_id=student,
            message=massage
        )
        student_notification.save()
        messages.success(request,'Studnet notification successfuly sent ')
    return redirect('send_student_notification')
@login_required(login_url="/")
def Student_Feedback(request):
    student_feedback=Student_feedback.objects.all()
    feedback_history=Student_feedback.objects.all().order_by('-id')[0:5]
    context={
        'student_feedback':student_feedback,
        'feedback_history':feedback_history
    }
    return render(request,'hod/student_feedback.html',context)
def Student_save_feedback(request):
    if request.method=="POST":
        student_feedback_id=request.POST['student_feedback_id']
        student_feedback_reply=request.POST['student_feedback_reply']
        feedback=Student_feedback.objects.get(id=student_feedback_id)
        feedback.feedback_reply=student_feedback_reply
        feedback.status=1
        feedback.save()
        return redirect('student_feedback')
@login_required(login_url="/")
def Student_leave_save(request):
    student_leave=Student_leave.objects.all()
    context={
        'student_leave':student_leave
    }
    return render(request,'hod/student_leave_hod.html',context)
@login_required(login_url="/")
def Student_approve_leave(request,pk):
    student=Student_leave.objects.get(id=pk)
    student.status=1
    student.save()
    return redirect('student_leave')
@login_required(login_url="/")
def Student_dissapprove_leave(request,pk):
    student_leave=Student_leave.objects.get(id=pk)
    student_leave.status=2
    student_leave.save()

    return redirect('student_leave')
@login_required(login_url="/")
def Allview_attendance(request):
    # staff_id=Staff.objects.get(admin=request.user.id)
    subject=Subject.objects.all()
    session_year=Session_Year.objects.all()
    action=request.GET.get('action')
    get_subject= None
    get_seession_year=None
    attendance_date=None
    attendace_report=None
    if action is not None:
        if request.method=="POST":
            subject_id=request.POST.get('subject_id')
            session_year_id=request.POST['session_year_id']
            attendance_date=request.POST['attendance_date']
            get_subject=Subject.objects.get(id=subject_id)
            get_seession_year=Session_Year.objects.get(id=session_year_id)
            # print()
            attendance=Attendance.objects.filter(subject_id=get_subject,attendance_date=attendance_date)
            # print(attendance)
            for sub in attendance:
                attendance_id=sub.id
                attendace_report=Attendance_Report.objects.filter(attendance_id=attendance_id)
            # print(sub.id)
            # print(attendace_report)

    context={
        'subject':subject,
        'session_year':session_year,
        'action':action,
        'get_subject':get_subject,
        'get_seession_year':get_seession_year,
        'attendance_date':attendance_date,
        'attendace_report':attendace_report
    }
  
    return render(request,'hod/allview_attendance.html',context)