from django.shortcuts import render,redirect
from django.contrib.auth.decorators import login_required
from studentapp.models import Staff,Staff_notification,Staff_leave,Feedback,Subject,Session_Year,Student,Attendance,Attendance_Report,student_result
from django. contrib import messages
@login_required(login_url="/")
def staff_home(request):
    return render(request,'staff/staffhome.html')
@login_required(login_url="/")
def staff_notification(request):
    staff=Staff.objects.filter(admin=request.user.id)
    # print(staff)
    for s in staff:
        staff_id=s.id
        # print(s.id)
        notifi=Staff_notification.objects.filter(staff_id=staff_id)
        context={
            'notifi':notifi,
        }

        # print(context)    
        return render(request,'staff/notification.html',context)
@login_required(login_url="/")
def staff_mark_done(request,status):
    notification=Staff_notification.objects.get(id=status)
    notification.status=1
    notification.save()

    return redirect('notification')
@login_required(login_url="/")
def staff_leave(request):
        staff=Staff.objects.filter(admin=request.user.id)
        for sl in staff:
            staff_id=sl.id
        # print(sl.id)
        # print(staff)
        staff_leave_history=Staff_leave.objects.filter(staff_id=staff_id)
        context={
            'staff_leave_history':staff_leave_history,
        }
        # print(context)
        return render (request,'staff/staff_leave.html',context)

@login_required(login_url="/")
def staff_apply_save(request):
    if request.method =="POST":
        leave_date=request.POST.get('leave_date')
        leave_message=request.POST['leave_message']
        staff = Staff.objects.get(admin=request.user.id)
        # print(staff)
        leave_in=Staff_leave(
            staff_id=staff,
            data=leave_date,
            message=leave_message,
        )
        leave_in.save()
        messages.success(request,"Apply for leave")
        return redirect('staff_leave')
@login_required(login_url="/") 
def apply_feedback(request):
    staff_id=Staff.objects.get(admin=request.user.id)
    feedback_history=Feedback.objects.filter(staff_id=staff_id)
    context={
        'feedback_history':feedback_history
    }
    return render(request,'staff/send_feedback_staff.html',context)
@login_required(login_url="/")
def Save_Feedback(request):
    if request.method=="POST":
        feedback=request.POST['feedback']
        # staff=Staff.objects.get(admin=request.user.id)
        staff=Staff.objects.get(admin=request.user.id)
        # print(staff)
        feedback=Feedback(
            staff_id=staff,
            feedback=feedback,
            feedback_reply="",
        )
        # print(feedback) 
        feedback.save()   
        messages.success(request,'Sent feedback successfully')        
    return redirect('send_feedback')
@login_required(login_url="/")
def Take_Attendance(request):
    staff_id=Staff.objects.get(admin=request.user.id)
    subject=Subject.objects.filter(staff=staff_id)
    session_year=Session_Year.objects.all()
    action=request.GET.get('action')
    students=None
    get_subject=None
    get_session_year=None
    if action is not None:
        if request.method == "POST":
            subject_id=request.POST['subject_id']
            session_year_id=request.POST['session_year_id']
            get_subject=Subject.objects.get(id=subject_id)
            get_session_year=Session_Year.objects.get(id=session_year_id)
            # print(get_subject,get_session_year)
            subject=Subject.objects.filter(id=subject_id)
            for sub in subject:
                student_id=sub.course.id
                students=Student.objects.filter(course_id=student_id)
    context={
        'subject':subject,
        'session_year':session_year,
        'get_subject':get_subject,
        'get_session_year':get_session_year,
        'action':action,
        'students':students,
    }
    # print(context)
    return render(request,'staff/take_attendance.html',context)
@login_required(login_url="/")
def Save_attendance(request):
    if request.method== "POST":
        subject_id=request.POST['subject_id']
        session_year_id=request.POST.get('session_year_id')
        attendance_date=request.POST['attendance_date']
        student_id=request.POST.getlist('student_id')
        get_subject=Subject.objects.get(id=subject_id)
        get_session_year=Session_Year.objects.get(id=session_year_id)
        attendance=Attendance(
            subject_id=get_subject,
            attendance_date=attendance_date,
            session_year_id=get_session_year

        )
        attendance.save()
        for stud in student_id:
            stu_id=stud
            int_stud=int(stu_id)
            p_student=Student.objects.get(id=int_stud)
            attendance_report=Attendance_Report(
                student_id=p_student,
                attendance_id=attendance
            )
            attendance_report.save()

    return redirect('take_attendance')
@login_required(login_url="/")
def View_staff_attendance(request):
    staff_id=Staff.objects.get(admin=request.user.id)
    subject=Subject.objects.filter(staff_id=staff_id)
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
    return render(request,'staff/view_staff_attendance.html',context)
@login_required(login_url="/")
def Add_Result(request):
    staff=Staff.objects.get(admin=request.user.id)
    # print(staff)
    subject=Subject.objects.filter(staff_id=staff)
    session_year=Session_Year.objects.all()
    action=request.GET.get('action')
    get_subject=None
    get_session_year=None
    students=None
    if action is not None:
        if request.method=="POST":
            subject_id=request.POST.get('subject_id')
            session_year_id=request.POST.get('session_year_id')
            # print(subject_id)
            # print(session_year_id)
            get_subject=Subject.objects.get(id=subject_id)
            get_session_year=Session_Year.objects.get(id=session_year_id)
            subjects=Subject.objects.filter(id=subject_id)
            for sub in subjects:
                student_id=sub.course.id
                students=Student.objects.filter(course_id=student_id)


        
    context={
        'subject':subject,
        'session_year':session_year,
        'action':action,
        'get_subject':get_subject,
        'get_session_year':get_session_year,
        'students':students
    }
    return render(request,'staff/add_result.html',context)
@login_required(login_url="/")
def Staff_save_result(request):
    if request.method=="POST":
        subject_id=request.POST.get('subject_id')
        session_year_id=request.POST.get('session_year_id')
        student_id=request.POST.get('student_id')
        assigment_marks=request.POST.get('assigment_marks')
        exam_marks=request.POST.get('exam_marks')
        get_student=Student.objects.get(admin=student_id)
        get_subject=Subject.objects.get(id=subject_id)
        check_exists=student_result.objects.filter(subject_id=get_subject,student_id=get_student).exists()
        if check_exists:
            result=student_result.objects.get(subject_id=get_subject,student_id=get_student)
            result.assignment_mark=assigment_marks
            result.exam_mark=exam_marks
            result.save()
            messages.success(request,'successfully updated result')
            return redirect('add_result')
        else:
            result=student_result(
                student_id=get_student,
                subject_id=get_subject,
                exam_mark=exam_marks,
                assignment_mark=assigment_marks    
            )
            result.save()
            messages.success(request,'successfully added result')
        

    return redirect('add_result')