from django.contrib import admin
from django.urls import path
from django.conf import settings
from django.conf.urls.static import static
from .import views,Hod_views,Staff_views,Student_views

urlpatterns = [
    path('admin',admin.site.urls),
    path('base',views.base,name='base'),
    # path('singhup',views.singhup,name='singhup'),
    #  login path
    path('',views.Login,name='login'),
    path('dologin',views.dologin,name='dologin'),
    path('dologout',views.dologout,name='logout'),
    #  This is profile update url
    path('profile',views.pudate,name='profile'),
    path('updateprofile',views.updateprofile,name='update_profile'),
    #  This is hod page url
    path('hod',Hod_views.HodHome,name='hod'),
    # addstudent tag
    path('student',Hod_views.addstudent,name='student'),
    path('hod/student',Hod_views.view_student,name='hod/student'),
    path('student_edit/<int:pk>',Hod_views.edit_student,name='edit_student'),
    path('update_student',Hod_views.Update_student,name='update_student')

    




    

]+static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)
