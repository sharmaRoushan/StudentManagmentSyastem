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
    path('add_staff',Hod_views.add_Staff,name='add_staf'),
    path('view/staff',Hod_views.view_staff,name='view_staff'),
    path('edit_staff/<int:pk>',Hod_views.edit_staff,name='edit_staff'),
    path('update_staff',Hod_views.update_staff,name='update_staff'),
    path('dilite_staff/<int:pk>',Hod_views.dilite_staff,name='dilite_staff'),


    # add student url
    path('student',Hod_views.addstudent,name='student'),
    path('hod/student',Hod_views.view_student,name='hod/student'),
    path('student_edit/<int:pk>',Hod_views.edit_student,name='edit_student'),
    path('update_student',Hod_views.Update_student,name='update_student'),
    path('dilite_student/<int:pk>',Hod_views.Dilite_Student,name='dilite_student'),
    path('add_course',Hod_views.course_add,name='add_course'),
    path('view_course',Hod_views.view_course,name='view_course'),
    path('edit_course/<int:pk>',Hod_views.edit_course,name='edit_course'),
    path('update_course',Hod_views.update_course,name='update_course'),
    path('dilite_course/<int:pk>',Hod_views.dilite_course,name='dilite_course'),

    #  add subject url
    path('add_subject',Hod_views.add_subject,name='add_subject'),
    path('view_subject',Hod_views.view_subject,name='view_subject'),
    path('edit_subject/<int:pk>',Hod_views.edit_subject,name='edit_subject'),
    path('update_subject',Hod_views.update_subject,name='update_subject'),
    path('subject_delete/<int:pk>',Hod_views.subject_delete,name='subject_delete'), 

    # add  session url
    path('add_session',Hod_views.add_session,name='add_session'),
    path('view_session',Hod_views.view_session,name='view_session'),
    path('edit_session/<int:pk>',Hod_views.edit_session,name='edit_session'),
    path('update_session',Hod_views.update_session,name='update_session'),
    path('delete_session/<int:pk>',Hod_views.delete_session,name='delete_session'),

    # This is staff urls
    path('staff_home',Staff_views.staff_home,name='staff_home')
    

    




    

]+static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)
