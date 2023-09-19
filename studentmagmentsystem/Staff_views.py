from django.shortcuts import render,redirect
from django.contrib.auth.decorators import login_required
from studentapp.models import Staff,Staff_notification
@login_required(login_url="/")
def staff_home(request):
    return render(request,'staff/staffhome.html')
def Notification(request):
    staff=Staff.objects.filter(admin=request.user.id)
    # print(staff)
    for s in staff:
        staff_id=s.id
        # print(s.id)
        Rk=Staff_notification.objects.filter(staff_id=staff_id)
        context={
          'Rk':Rk
        }
        
    return render(request,'staff/notification.html',context)
def staff_mark_done(request,status):
    notification=Staff_notification.objects.get(id=status)
    notification.status=1
    notification.save()

    return redirect('notification')