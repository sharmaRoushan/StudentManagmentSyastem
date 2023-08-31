from django.shortcuts import render,redirect
from django.contrib.auth.decorators import login_required





@login_required(login_url='/')
def HodHome(request):
    return render(request,'hod/hodhome.html')