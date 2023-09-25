from django.shortcuts import render,redirect
from django.contrib.auth.decorators import login_required
from studentapp.models import Staff,Staff_notification,Staff_leave
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
            'notifi':notifi
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
        leave_date=request.POST['leave_date']
        leave_message=request.POST['leave_message']
        staff = Staff.objects.get(admin=request.user)
        # print(staff)
        leave_in=Staff_leave(
            staff_id=staff,
            data=leave_date,
            message=leave_message,
        )
        leave_in.save()
        messages.success(request,"Apply for leave")
    return redirect('staff_leave') 
def apply_feedback(request):
    return render(request,'staff/send_feedback.html') 