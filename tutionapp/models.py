from django.db import models
from django.contrib.auth.models import AbstractUser
# Create your models here.
class CustomUser(AbstractUser):
    HOD = '1'
    STAFF = '2'
    STUDENT = '3'
    
    EMAIL_TO_USER_TYPE_MAP = {
        'hod': HOD,
        'staff': STAFF,
        'student': STUDENT
    }

    user_type_data = ((HOD, "HOD"), (STAFF, "Staff"), (STUDENT, "Student"))
    user_type = models.CharField(default=1, choices=user_type_data, max_length=10)
    
class departmenttable(models.Model):
    department=models.CharField(max_length=255,null=True)           
class course(models.Model):
    course_name=models.CharField(max_length=255,null=True)
    Course_fee=models.IntegerField(null=True)
    syallabus=models.FileField(upload_to='images/' ,null=True)
    course_duration=models.CharField(max_length=255,null=True)    

class teacher(models.Model):
    joindate=models.DateTimeField(auto_now_add=True,null=True)
    username=models.CharField(max_length=255,null=True)
    firstname=models.CharField(max_length=255,null=True)
    lastname=models.CharField(max_length=255,null=True)
    email=models.EmailField(null=True)
    age=models.IntegerField(null=True)
    contact=models.CharField(max_length=255,null=True)
    image=models.FileField(upload_to='images/' ,null=True)
    user=models.ForeignKey(CustomUser,on_delete=models.CASCADE,null=True)
    departmentid=models.ForeignKey(departmenttable,on_delete=models.CASCADE,null=True)
    courseid=models.ForeignKey(course,on_delete=models.CASCADE,null=True)
class student(models.Model):
    joindate=models.DateTimeField(auto_now_add=True,null=True)
    username=models.CharField(max_length=255,null=True)
    firstname=models.CharField(max_length=255,null=True)
    lastname=models.CharField(max_length=255,null=True)
    email=models.EmailField(null=True)
    age=models.IntegerField(null=True)
    contact=models.CharField(max_length=255,null=True)
    image=models.FileField(upload_to='images/' ,null=True)
    user=models.ForeignKey(CustomUser,on_delete=models.CASCADE,null=True)
    courseid=models.ForeignKey(course,on_delete=models.CASCADE,null=True)


class assigntable(models.Model):
    departmentid=models.ForeignKey(departmenttable,null=True,on_delete=models.CASCADE)
    courseid=models.ForeignKey(course,on_delete=models.CASCADE,null=True)
    teacherid=models.ForeignKey(teacher,on_delete=models.CASCADE,null=True)
    

class assignment(models.Model):
    userid=models.ForeignKey(CustomUser,on_delete=models.CASCADE,null=True)
    assignment_name=models.CharField(max_length=255,null=True)
    start_date=models.DateField(null=True)
    end_date=models.DateField(null=True)
    courseid=models.ForeignKey(course,on_delete=models.CASCADE)  
class assignmenttable(models.Model):
    userid=models.ForeignKey(CustomUser,on_delete=models.CASCADE,null=True)
    submit_on=models.DateField(auto_now=True)
    end_date=models.DateField(auto_now=True)
    username=models.CharField(max_length=255,null=True)
    assignment_name=models.CharField(max_length=255,null=True)
    image=models.FileField(null=True,upload_to='images/')
    status=models.IntegerField(null=True,default=0)
    courseid=models.ForeignKey(course,on_delete=models.CASCADE)
class notificationtable(models.Model):
    first_name=models.CharField(max_length=255,null=True)
    last_name=models.CharField(max_length=255,null=True)
    email=models.EmailField(max_length=255,null=True)
    age=models.IntegerField()
    image=models.FileField(null=True,upload_to='images')
    status=models.IntegerField(null=True)
    user_type=models.IntegerField(null=True)
    username=models.CharField(max_length=255,null=True)
    
class notification(models.Model):
    first_name=models.CharField(max_length=255,null=True)
    last_name=models.CharField(max_length=255,null=True)
    age=models.IntegerField()
    email=models.EmailField()
    image=models.ImageField(upload_to='images/',null=True)
    usertype=models.IntegerField()
    status=models.IntegerField(default=1,null=True)
    courseid=models.ForeignKey(course,on_delete=models.CASCADE,null=True)
    username=models.CharField(max_length=255,null=True)
    contact=models.IntegerField()
class teachernotification(models.Model):
    userid=models.ForeignKey(CustomUser,on_delete=models.CASCADE,null=True)
    messge=models.CharField(max_length=255,null=True)
class passtable(models.Model):
    password=models.CharField(max_length=255,null=True)
    userid=models.ForeignKey(notification,on_delete=models.CASCADE,null=True)    
class attendancetable(models.Model):
    date=models.DateField(null=True)
    userid=models.ForeignKey(CustomUser,on_delete=models.CASCADE,null=True)
    courseid=models.ForeignKey(course,on_delete=models.CASCADE,null=True)
    attendance=models.IntegerField(default=0,null=True)
class teacherattendancetable(models.Model):
    date=models.DateField(null=True)
    userid=models.ForeignKey(CustomUser,on_delete=models.CASCADE,null=True)
    attendance=models.IntegerField(default=0,null=True)
class attendancereport(models.Model):
    userid=models.ForeignKey(CustomUser,on_delete=models.CASCADE,null=True)
    courseid=models.ForeignKey(course,on_delete=models.CASCADE,null=True)
    status=models.IntegerField(null=True)
    date=models.DateField()
class leavenotification(models.Model):
    userid=models.ForeignKey(CustomUser,on_delete=models.CASCADE,null=True)
    status=models.IntegerField(default=1,null=True)
    date=models.DateField(null=True)
    reason=models.CharField(max_length=255,null=True)     
class studentleavetable(models.Model):
    userid=models.ForeignKey(CustomUser,on_delete=models.CASCADE,null=True)
    status=models.IntegerField(default=1,null=True)
    date=models.DateField(null=True)
    reason=models.CharField(max_length=255,null=True)    
class teacherleavetable(models.Model):
    
    userid=models.ForeignKey(CustomUser,on_delete=models.CASCADE,null=True)
    status=models.IntegerField(default=1,null=True)
    date=models.DateField(null=True)
    reason=models.CharField(max_length=255,null=True)  