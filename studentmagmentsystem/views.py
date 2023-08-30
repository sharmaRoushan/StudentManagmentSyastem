from django.shortcuts import render ,redirect,HttpResponse
from studentapp.EmailBackend import EmailBackEnd
from django.contrib.auth import authenticate,logout,login
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
                return HttpResponse('This is Hod panal')
            elif user_type == '2':
                 return HttpResponse('This is staff panal')
            elif user_type == '3':
                return HttpResponse('This is student panal')

            else:
                # massage
                return redirect('login')
        else:
            # massage
            return redirect('login')


   