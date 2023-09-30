from django.shortcuts import render,redirect
from studentapp.models import Student_notification,Student,Student_feedback

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
    return render(request,'student/student_leave.html')
