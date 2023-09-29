from django.shortcuts import render,redirect 

def Student_home(request):
    return render(request,'student/student_home.html')
