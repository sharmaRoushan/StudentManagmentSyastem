from django.contrib import admin
from .models import *
from django.contrib.auth.admin import UserAdmin

admin.site.register(CoustamUser,UserAdmin)
admin.site.register(Course)
admin.site.register(Session_Year)
admin.site.register(Student)
admin.site.register(Staff)
admin.site.register(Subject)
admin.site.register(Staff_notification)
admin.site.register(Staff_leave)
admin.site.register(Feedback)
admin.site.register(Student_notification)
admin.site.register(Student_feedback)
admin.site.register(Student_leave)
admin.site.register(Attendance)
admin.site.register(Attendance_Report)
admin.site.register(student_result)
class UserModel(UserAdmin):
    list_display=['username','user_type']

# Register your models here.
