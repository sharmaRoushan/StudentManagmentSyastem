from django.shortcuts import render,redirect
from django.contrib.auth.decorators import login_required
@login_required(login_url="/")
def staff_home(request):
    return render(request,'staff/staffhome.html')