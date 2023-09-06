from django.db import models
from django.contrib.auth.models import AbstractUser


class CoustamUser(AbstractUser):
    User=(
        (1,'HOD'),
        (2,'STAFF'),
        (3,'STUDENT'),

    )
    user_type=models.CharField(choices=User,max_length=50,default=1)
    profile_pic=models.ImageField(upload_to='Media/profile_pic')
    # profile_pic=models.ImageField(null=True,blank=True)
    # @property
    # def imageURL(self):
    #     url=""
    #     try:
    #         url=self.image.url
    #         # url=""
    #     except:
    #         url=""
    #     return url
class Course(models.Model):
    course_name=models.CharField(max_length=100)
    created_at=models.DateTimeField(auto_now_add=True)
    update_at=models.DateTimeField(auto_now_add=True)
    def __str__(self):
        return self.course_name
class Session_Year(models.Model):
    session_start=models.CharField(max_length=100)
    session_end=models.CharField(max_length=100)
    def __str__(self):
        return self.session_start+"to"+self.session_end
class Student(models.Model):
    admin=models.OneToOneField(CoustamUser,on_delete=models.CASCADE)
    address=models.TextField()
    gender=models.CharField(max_length=100)
    course_id=models.ForeignKey(Course,on_delete=models.DO_NOTHING)
    Session_Year_id=models.ForeignKey(Session_Year,on_delete=models.DO_NOTHING)
    created_at=models.DateTimeField(auto_now_add=True)
    update_at=models.DateTimeField(auto_now_add=True)
    def __str__(self):
        return self.admin.first_name+" "+self.admin.last_name

