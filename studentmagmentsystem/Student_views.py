from django.shortcuts import render,redirect
from studentapp.models import Student_notification,Student,Student_feedback,Student_leave
from django. contrib import messages


def Student_home(request):
    return render(request,'student/student_home.html')



def Stud_notification(request):
    student=Student.objects.filter(admin=request.user.id)
    # print(staff)
    for stud in student:
        student_id=stud.id
        # print(s.id)
        notification=Student_notification.objects.filter(student_id=student_id)
        context={
            'notification':notification,
        }
        return render(request,'student/student_notification.html',context)
def Student_mark_done(request,status):
    notification=Student_notification.objects.get(id=status)
    notification.status=1
    notification.save()
    return redirect('student_notification')
def Send_student_feedback(request):
    student_id=Student.objects.get(admin=request.user.id)
    feedback_history=Student_feedback.objects.filter(student_id=student_id)
    context={
        'feedback_history':feedback_history,
    }
    return render(request,'student/send_student_feedback.html',context)
def student_Feedback_save(request):
    if request.method== "POST":
        stud_feedback=request.POST['stud_feedback']
        student=Student.objects.get(admin=request.user.id)
        stud=Student_feedback(
            student_id=student,
            feedback=stud_feedback,
            feedback_reply= ""
        )
        stud.save()
    return redirect('send_student_feedback')
def Student_leave_apply(request):
    student=Student.objects.filter(admin=request.user.id)
    for stud in student:
        student_id=stud.id
        student_leave_history=Student_leave.objects.filter(student_id=student_id)
        context={
            'student_leave_history':student_leave_history
        }
       
    return render(request,'student/student_leave.html',context)
def Student_leave_save(request):
    if request.method== "POST":
        leave_date=request.POST['leave_date']
        leave_message=request.POST['leave_message']
        student_id=Student.objects.get(admin=request.user.id)
        student_leave=Student_leave(
            student_id=student_id,
            data=leave_date,
            message=leave_message,
        )
        messages.success(request,'student leave are successfully sent')
        student_leave.save()
        return redirect('student_leave_apply')
