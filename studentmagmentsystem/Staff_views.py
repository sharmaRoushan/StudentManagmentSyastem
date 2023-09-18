from django.shortcuts import render,redirect
from django.contrib.auth.decorators import login_required
from studentapp.models import Staff,Staff_notification
@login_required(login_url="/")
def staff_home(request):
    return render(request,'staff/staffhome.html')
def Notification(request):
    staff=Staff.objects.filter(admin=request.user.id)
    # print(staff)
    for staf in staff:
        # print(staf.pk)
        staf_id=staf.pk
        notification=Staff_notification.objects.filter(staff_id=staf_id)
        context={
            'notification':notification
        }
    return render(request,'staff/notification.html',context)