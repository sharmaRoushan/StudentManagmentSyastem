from django.shortcuts import render,redirect,HttpResponse
from studentapp.EmailBackend import EmailBackEnd
from django.contrib.auth import authenticate,logout,login
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from studentapp.models import CoustamUser
def base(request):
    return render(request,'base.html')
def Login(request):
    return render(request,'login.html')
def dologin(request):
    if request.method == 'POST':
        user=EmailBackEnd.authenticate(request,
                                        username=request.POST.get('email'),
                                        password=request.POST.get('password'))
        if user!=None:
            login(request,user)
            user_type=user.user_type
            if user_type == '1':
                return redirect('hod')
            elif user_type == '2':
                 return redirect('staff_home')
            elif user_type == '3':
                return redirect ('student_home')

            else:
                messages.error(request,'Email and password are invaled')
                return redirect('login')
        else:
            messages.error(request,'Email and password are invaled')
    return redirect('login')
def dologout(request):
    logout(request)
    return redirect('login')
@login_required(login_url='/')
def pudate(request):
    user = CoustamUser.objects.get(id=request.user.id)
    # print(user)
    context={
        'user':user,
    }
    return render(request,'profile.html')
@login_required(login_url='/')
def updateprofile(request):
    if request.method == 'POST':
        # profile_pic=request.FILES['profile_pic']
        profile_pic=request.FILES.get('profile_pic')
        first_name=request.POST.get('first_name')
        last_name=request.POST.get('last_name')
        # email=request.POST.get('email')
        # username=request.POST.get('username')
        password=request.POST.get('password')
        # print(profile_pic)
        # print(profile_pic,first_name,last_name,email,username,password)
        try:
            coustamuser=CoustamUser.objects.get(id=request.user.id)
            coustamuser.first_name=first_name
            coustamuser.last_name=last_name
            # coustamuser.username=username
            coustamuser.profile_pic=profile_pic
            if password!=None and password!="":
                coustamuser.set_password(password)
            # if password!=None and password!="":
            #     coustamuser.set_password(password)
            if profile_pic!=None and profile_pic!="":
                coustamuser.profile_pic=profile_pic
            coustamuser.save()
            messages.success(request,'Your profile Update Successfully')
            redirect('hod')
        except:
            messages.error(request,'Failed To Update Your Profile pic')
    return render(request,'profile.html')

   