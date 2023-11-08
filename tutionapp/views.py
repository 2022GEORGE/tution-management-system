from django.shortcuts import render,redirect
from django.contrib.auth import  authenticate, login as a_login
from django.contrib import messages
from django.contrib.auth.models import User,auth
from .models import CustomUser,teacher,student,course,departmenttable,assigntable,passtable,assignment,assignmenttable,notification
from django.contrib.auth.decorators import login_required
from django.conf import settings
from django.core.mail import send_mail
from .models import attendancetable,teacherattendancetable,attendancereport,studentleavetable,teacherleavetable,leavenotification,teachernotification
import random,datetime,os
# Create your views here.
@login_required(login_url='login1')
def adminhome(request):
    x=notification.objects.all()
    c=0
    for i in x:
        c=c+1
    y=leavenotification.objects.all()
    c2=0
    for i in y:
        c2=c2+1    
    return render(request,'adminhome.html',{'c':c,'c2':c2})
@login_required(login_url='login1')
def studenthome(request):
    return render(request,'studenthome.html')
@login_required(login_url='login1')
def teacherhome(request):
    current=request.user.id
    data=teachernotification.objects.all()
    c=0
    for i in data:
        if i.userid.id == current:
            c=c+1
    return render(request,'teacherhome.html',{'data':data,'co':c,'current':current})
@login_required(login_url='login1')
def addcourse(request):
    return render(request,'addcourse.html')
def doaddcourse(request):
    if request.method == 'POST':
        coursename=request.POST['course']
        coursefee=request.POST['fee']
        sy=request.FILES.get('syllabus')
        dura=request.POST['START_DATE']
        if sy == '':
            messages.info(request,'pls select a file type/pdf')
            return redirect('addcourse')
        data_exists=course.objects.filter(course_name=coursename).exists()
        if data_exists:
            messages.info(request,'course already exists')
            return redirect('addcourse')
        data=course(course_name=coursename,Course_fee=coursefee,syallabus=sy,course_duration=dura)
        data.save()
        return redirect('managecourse')
@login_required(login_url='login1')
def department(request):
    return render(request,'department.html')
@login_required(login_url='login1')
def assign(request):
    c=course.objects.all()
    d=departmenttable.objects.all()
    t=teacher.objects.all()
    st=student.objects.all()
    return render(request,'assign.html',{'course':c,'dep':d,'teacher':t,'student':st})
def sregistration(request):
    data=course.objects.all()
    return render(request,'sregistration.html',{'data':data})

def login1(request):
    return render(request,'login.html')
def doRegistration(request):
    if request.method == 'POST':
        first_name=request.POST['fname']
        last_name=request.POST['lname']
        email_id=request.POST['email']
        age=request.POST['age']
        contact=request.POST['contact']
        courseid=request.POST['course']
        image=request.FILES.get('image')
        password =str(random.randint(100000,999999))
        print(password)
        print(first_name[0])
        x=first_name[0]
        y=last_name[0]
        if x>='a' and x<='z'  and  y>='a' and y<='z':
            messages.info(request,'FISRT LETTER MUST BE A CAPITAL')
            return redirect('sregistration')
        if not (email_id and age and image and first_name and last_name ):
            messages.info(request, 'Please provide all the details!!')
            return redirect('sregistration')
        is_user_exists2 = notification.objects.filter(email=email_id).exists()
        if is_user_exists2:
            messages.info(request,'User with this email id already exists. Please proceed to login!!') 
            return redirect('sregistration')
            
        
        is_user_exists = CustomUser.objects.filter(email=email_id).exists()
        if is_user_exists:
            messages.info(request,'User with this email id already exists. Please proceed to login!!') 
            return redirect('sregistration')
        user_type=3
        x=str(random.randint(10000,99999))
        user_name=first_name+x
        data=notification()
        data.first_name=first_name
        data.last_name=last_name
        data.contact=contact
        data.username=user_name
        data.age=age
        data.email=email_id
        data.usertype=user_type
        data.courseid=course.objects.get(id=courseid)
        data.image=image
        data.save()
        userpass2=passtable()
        userpass2.password=password
        userpass2.userid=data
        userpass2.save()
        subject="ADMIN APPROVED"
        message="username: "+str(user_name)+"\n"+"password: "+str(password)+"\n"+"email: "+str(email_id)
        send_mail(subject,message,settings.EMAIL_HOST_USER,[data.email])
        messages.info(request,'Registertion successfull,please check your mail for username and password')       
        return redirect('sregistration')
def syallabus(request):
    current=request.user.id
    data=student.objects.get(user=current)
    courseid=data.courseid.id
    data2=course.objects.get(id=courseid)
    return render(request,'coursesyallabus.html',{'data':data2})
def doteacherregistration(request):
    if request.method == 'POST':
        first_name=request.POST['fname']
        last_name=request.POST['lname']
        email_id=request.POST['email']
        age=request.POST['age']
        contact=request.POST['contact']
        image=request.FILES.get('image')
        password =str(random.randint(100000,999999))
        print(password)
        print(first_name[0])
        x=first_name[0]
        y=last_name[0]
        if x>='a' and x<='z' and  y>='a' and y<='z':
            messages.info(request,'FISRT LETTER MUST BE A CAPITAL')
            return redirect('teacherregistration')
        if not (email_id and age and image and first_name and last_name ):
            messages.info(request, 'Please provide all the details!!')
            return redirect('teacherregistration')
        
        
        is_user_exists = CustomUser.objects.filter(email=email_id).exists()
        if is_user_exists:
            messages.info(request,'User with this email id already exists. Please proceed to login!!') 
            return redirect('sregistration')
        user_type=2
        x=str(random.randint(10000,99999))
        user_name=first_name+x
        data=notification()
        data.first_name=first_name
        data.last_name=last_name
        data.contact=contact
        data.username=user_name
        data.age=age
        data.email=email_id
        data.usertype=user_type
        data.image=image
        data.save()
        userpass2=passtable()
        userpass2.password=password
        userpass2.userid=data
        userpass2.save()
        subject="ADMIN APPROVED"
        message="username: "+str(user_name)+"\n"+"password: "+str(password)+"\n"+"email: "+str(email_id)
        send_mail(subject,message,settings.EMAIL_HOST_USER,[data.email])
        messages.info(request,'Registertion successfull,please check your mail for username and password')       
        return redirect('teacherregistration')
def doLogin(request):
    user_name=request.GET.get('username')
    email_id=request.GET.get('email')
    password1=request.GET.get('password')
    if not (email_id and password1):
        messages.info(request,'fill all the feilds')
        return redirect('login1')
    user=auth.authenticate(username=user_name, email=email_id,password=password1)
    if not user:
        messages.info(request,'Invalid Login Credentials!!')
        return redirect('login1')
    a_login(request,user)
    if user.user_type == CustomUser.STUDENT:
        messages.info(request,f'welcome '+str(user_name))
        return redirect('studenthome')
    elif user.user_type == CustomUser.STAFF:
        messages.info(request,f'welcome '+str(user_name))
        return redirect('teacherhome')
    elif user.user_type == CustomUser.HOD:
        messages.info(request,'welcome '+str(user_name))
        return redirect('adminhome')
    return redirect('login1')
@login_required(login_url='login1')
def managecourse(request):
    data=course.objects.all()
    return render(request,'managecourse.html',{'key':data}) 
def adddepartment(request):
    if request.method =='POST':
        dep=request.POST['dep']
        check=departmenttable.objects.filter(department=dep).exists
        if check is None:
            messages.info(request,'department exists')
            return redirect('department')
        else:
            data=departmenttable(department=dep)
            data.save()
            messages.info(request,'department added')
            return redirect('department')
           
def addassign(request):
    if request.method =='POST':
        dep=request.POST['department']
        co=request.POST['course']
        tea=request.POST['teacher']
       
        dep1=departmenttable.objects.get(id=dep)
        co1=course.objects.get(id=co)
        tea1=teacher.objects.get(id=tea)
        user=tea1.user.id
        try:
            data=assigntable.objects.get(teacherid=tea1)
            if data:
                messages.info(request,'course already assigned')
                return redirect('assign')
        except:
            data=assigntable(departmentid=dep1,courseid=co1,teacherid=tea1)
            data.save()
            data3=teacher.objects.get(id=tea)
            data3.departmentid=departmenttable.objects.get(id=dep)
            data3.courseid=co1
            data3.save()
            data4=teachernotification()
            data4.userid=CustomUser.objects.get(id=user)
            y=co1.course_name  + 'course assigned for you'
            data4.messge=y
            data4.save()
            
    return redirect('adminhome')
@login_required(login_url='login1')
def tableassign(request):
    data=assigntable.objects.all()
    return render(request,'assigntable.html',{'key':data})
@login_required(login_url='login1')
def teachertableassign(request):
    return render(request,'teacherassigntable.html')
@login_required(login_url='login1')
def teacherviewstudentatten(request):
    if request.method == 'POST':
        current=request.user.id
        date=request.POST['date']
        stdata=teacher.objects.get(user=current)
        courseid=stdata.courseid.id
        data=attendancereport.objects.filter(courseid=courseid,date=date)
        return render(request,'teacherpageforstatten.html',{'data':data})
@login_required(login_url='login1')
def teacherviewst(request):
    current=request.user.id
    tedata=teacher.objects.get(user=current)
    courseid=tedata.courseid.id
    data=student.objects.filter(courseid=courseid)
    return render(request,'teacherviewst.html',{'data':data})
       
def deleteassign(request,pk):
    data=assigntable.objects.get(id=pk)
    data.delete()
    return redirect('tableassign')
@login_required(login_url='login1')
def studentprofile(request):
    current=request.user.id
    data=student.objects.get(user_id=current)
    return render(request,'studentprofile.html',{'data':data})
@login_required(login_url='login1')
def teacherprofile(request):
    current=request.user.id
    data1=teacher.objects.get(user=current)
    return render(request,'teacherprofile.html',{'data':data1})
@login_required(login_url='login1') 
def studentatendance(request):
    current=request.user.id
    teacherdata=teacher.objects.get(user=current)
    value=student.objects.filter(courseid=teacherdata.courseid)
    return render(request,'studentatendance.html',{'data':value})
@login_required(login_url='login1')
def studentatendancedata(request):
    if request.method =='POST':
        value=request.POST['course']
        value1=course.objects.get(id=value)
        data=attendancetable.objects.all()
        return render(request,'attendancetable.html',{'data':data,'data2':value1})
    return redirect('studentatendance')
     
          
def present(request):
    if request.method =='POST':
        a=request.POST['username']
        b=request.POST['date']
        c=request.POST['attendance']
        user=CustomUser.objects.get(id=a)
        if a =='' and b =='' and c =='':
            messages.info(request,'fill all the fileds')
            return redirect('studentatendancedata')
        try:
            if attendancereport.objects.get(userid=user,date=b):
                messages.info(request,'ATTENDANCE ALREADY TAKEN FOR THE TEACHER FOR THE SAME DATE')
                return redirect('studentatendancedata')
        except:
           
            studentdata=student.objects.get(user=user)
            cid=studentdata.courseid.id
            coursedata=course.objects.get(id=cid)
            data=attendancereport(userid=user,date=b,status=c,courseid=coursedata)
            data.save()
            messages.info(request,'ATTENDANCE MARKED')
            return redirect('studentatendancedata')
    return redirect('studentatendancedata')
@login_required(login_url='login1')
def assignmentst(request):
    current=request.user.id
    tea=teacher.objects.get(user=current)
    c=tea.courseid_id
    data=course.objects.get(id=c)
    stu=student.objects.filter(courseid=data.id)
    return render(request,'assignment.html',{'data':stu}) 
def doassignment(request):
    if request.method=='POST':
        current=request.user.id
        a=request.POST['assignment']
        b=datetime.datetime.now()
        c=request.POST['edate']
        d=request.POST['student']
        teacherid=teacher.objects.get(user=current)
        co=course.objects.get(id=teacherid.courseid.id)
        current=request.user.id
        user=CustomUser.objects.get(id=d)
        if a =='' and c == '' and d == '':
            messages.info(request,'fill all the field')
            return redirect('assignmentst')
        try:
            if assignment.objects.get(userid=user,start_date=b,end_date=c):
                messages.info(request,'ASSIGNMENT already ASSIGNED FOR THSI STUDENT FOR SAME DATE')
                return redirect('assignmentst')
        except:
            data=assignment()
            data.userid=user
            data.assignment_name=a
            data.start_date=b
            data.end_date=c
            data.courseid=co
            data.save()
            messages.info(request,'assignment added')
            return redirect('assignmentst')   
@login_required(login_url='login1')       
def studentpage(request):
    current=request.user.id
    data=assignment.objects.filter(userid=current)
    return render(request,'studentpageassignment.html',{'data':data})
def submitassignmet(request,pk):
    data=assignment.objects.get(id=pk)
    return render(request,'submitassignmetform.html',{'data':data})
@login_required(login_url='login1')
def teacherdetails(request):
    data=teacher.objects.all()
    return render(request,'teacherdetails.html',{'data':data})    
def delteacher(request,pk):
    data1=teacher.objects.get(user=pk)
    data1.delete()
    data=CustomUser.objects.get(id=pk)
    data.delete()
    return redirect('teacherdetails')
def delstudent(request,pk):
    # data0=passtable.objects.get(userid=pk)
    # data0.delete()
    # # assign=assignmenttable.objects.get(userid=pk)
    # # assign.delete()
    # noti=notification.objects.get(userid=pk)
    # noti.delete()
    # lea=attendancetable.objects.get(userid=pk)
    # lea.delete()
    # lea2=attendancereport.objects.get(userid=pk)
    # lea2.delete()
    # leav=studentleavetable.objects.get(userid=pk)
    # leav.delete()
    data=student.objects.get(user=pk)
    data.delete()
    data1=CustomUser.objects.get(id=pk)
    data1.delete()
    return redirect('studentdetails')
@login_required(login_url='login1')
def logout(request):
    auth.logout(request)
    return redirect('login1')
@login_required(login_url='login1')
def studentdetails(request):
    data=student.objects.all()
    return render(request,'studentdetails.html',{'data':data})
@login_required(login_url='login1')
def viewuser(request):
    data=notification.objects.all()
    return render(request,'approve.html',{'data':data})
def approve(request,pk):
    data=notification.objects.get(id=pk)
    password=passtable.objects.get(userid=pk)
    if data.usertype == 2:
        data.status='2'
        data.save()
        usermain=CustomUser()
        usermain.username=data.username
        usermain.set_password(password.password)
        usermain.first_name=data.first_name
        usermain.last_name=data.last_name
        usermain.email=data.email
        usermain.user_type=data.usertype
        usermain.save()
        teacherdata=teacher()
        teacherdata.username=data.username
        teacherdata.email=data.email
        teacherdata.firstname=data.first_name
        teacherdata.lastname=data.last_name
        teacherdata.age=data.age
        teacherdata.contact=data.contact
        teacherdata.image=data.image
        teacherdata.user=usermain
        teacherdata.save()
        atn=teacherattendancetable()
        atn.userid=usermain
        atn.date=datetime.datetime.now()
        atn.save()
        noti=notification.objects.get(id=pk)
        noti.delete()
        return redirect('viewuser')
    if data.usertype == 3:
        data.status='2'
        data.save()
        usermain=CustomUser()
        usermain.username=data.username
        usermain.set_password(password.password)
        usermain.first_name=data.first_name
        usermain.last_name=data.last_name
        usermain.email=data.email
        usermain.user_type=data.usertype
        usermain.save()
        teacherdata=student()
        teacherdata.username=data.username
        teacherdata.email=data.email
        teacherdata.firstname=data.first_name
        teacherdata.lastname=data.last_name
        teacherdata.age=data.age
        teacherdata.contact=data.contact
        teacherdata.courseid=course.objects.get(id=data.courseid.id)
        teacherdata.image=data.image
        teacherdata.user=usermain
        teacherdata.save()
        data4=attendancetable()
        data4.userid=usermain
        data4.courseid=course.objects.get(id=data.courseid.id)
        data4.save()
        data5=assignmenttable()
        data5.userid=usermain
        data5.courseid=course.objects.get(id=data.courseid.id)
        data5.status=0
        data5.save()
        noti=notification.objects.get(id=pk)
        noti.delete()
    return redirect('viewuser') 
def disapprove(request,pk):
    data=notification.objects.get(id=pk)
    # if data.usertype == 2:
    #     user=notification.objects.get(userid=pk)
    #     user.delete()
    #     return redirect('viewuser')
    # if data.usertype == 3:
    user=notification.objects.get(id=pk)
    user.delete()
    return redirect('viewuser')
    # return redirect('viewuser')
@login_required(login_url='login1')
def stattendanceview(request):
    Current=request.user.id
    data=attendancereport.objects.all()
    return render(request,'stviewattendance.html',{'data':data,'current':Current})
    
@login_required(login_url='login1')
def teacherattendanceview(request):
    Current=request.user.id
    data=teacherattendancetable.objects.all()
    x=datetime.datetime.now()
    return render(request,'teacherattendance.html',{'data':data})
@login_required(login_url='login1')
def teviewattendance(request):
    current=request.user.id
    data=attendancereport.objects.all()
    return render(request,'teviewattendance.html',{'data':data,'current':current})
def present1(request):
    if request.method =='POST':
        a=request.POST['username']
        b=request.POST['date']
        c=request.POST['attendance']
        user=CustomUser.objects.get(id=a)
        try:
            if attendancereport.objects.get(userid=a,date=b):
                messages.info(request,'ATTENDANCE ALREADY TAKEN FOR THE TEACHER FOR THE SAME DATE')
                return redirect('teacherattendanceview')
        except:
           
            data=attendancereport(userid=user,date=b,status=c)
            data.save()
            messages.info(request,'ATTENDANCE MARKED')
            return redirect('teacherattendanceview')
    return redirect('teacherattendanceview')
def absent1(request,pk):
    data=teacherattendancetable.objects.get(id=pk)
    data.date=datetime.datetime.now()
    data.attendance=0
    data.save()
    user=data.userid.id
    user1=CustomUser.objects.get(id=user)
    x=datetime.datetime.now()
    data2=attendancereport(userid=user1,status=data.attendance,date=x)
    data2.save()
    return redirect('teacherattendanceview')
@login_required(login_url='login1')
def studentleave(request):
    return render(request,'studentleave.html')
def dostudentleave(request):
    if request.method == 'POST':
        date=request.POST['date']
        reason=request.POST['reason']
        current=request.user.id
        user=CustomUser.objects.get(id=current)
        data=studentleavetable(userid=user,date=date,reason=reason)
        data.save()
        data2=leavenotification(userid=user,date=date,reason=reason)
        data2.save()
      
        return redirect('viewstudentleave')
@login_required(login_url='login1')    
def viewstudentleave(request):
    current=request.user.id
    data=studentleavetable.objects.all()  
    return render(request,'viewstudentleave.html',{'data':data,'current':current})

       
@login_required(login_url='login1')
def studentleaveaction(request):
    data=leavenotification.objects.all()  
    return render(request,'studentleaveaction.html',{'data':data}) 
    
def leaveapprove(request,pk):
    date=datetime.datetime.now()
    data1=leavenotification.objects.get(id=pk)
    user=data1.userid.id
    date=data1.date
    data=studentleavetable.objects.get(userid=user,date=date)
    data.status=2
    data.save()
    data1.delete()
    return redirect('studentleaveaction')
def leavedisapprove(request,pk):
  
    data1=leavenotification.objects.get(id=pk)
    date=data1.date
    data=studentleavetable.objects.get(userid=data1.userid,date=date)
    data.status=0
    data.save()
    data1.delete()
    return redirect('studentleaveaction')
@login_required(login_url='login1')
def viewteacherleave(request):
    current=request.user.id
    data=studentleavetable.objects.all()  
    return render(request,'viewteacherleave.html',{'data':data,'current':current})
   
@login_required(login_url='login1')
def teacherleave(request):
    return render(request,'teacherleave.html')
def doteacherleave(request):
    if request.method == 'POST':
        date=request.POST['date']
        reason=request.POST['reason']
        current=request.user.id
        user=CustomUser.objects.get(id=current)
        data=studentleavetable(userid=user,date=date,reason=reason)
        data.save()
        data2=leavenotification(userid=user,date=date,reason=reason)
        data2.save()
        return redirect('viewteacherleave')
def pushassignment(request,pk):
    if request.method =='POST':
        image=request.FILES.get('image')
        if image == '':
            messages.info('pls select a file')
            return redirect('studentpage')
        current=request.user.id
        user=CustomUser.objects.get(id=current)
        user2=student.objects.get(user=current)
        asii=assignment.objects.get(id=pk)
        date=datetime.datetime.now()
        data=assignmenttable()
        data.userid=user
        data.submit_on=date
        data.end_date=asii.end_date
        data.username=user.username
        data.assignment_name=asii.assignment_name
        data.courseid=user2.courseid
        data.image=image
        data.status=1
        data.save()
        asii.delete()
        return redirect('studentpage')
def viewassignmentform(request):
    return render(request,'viewassignmentform.html')   
@login_required(login_url='login1')
def viewassignment(request):
    if request.method == 'POST':
        date=request.POST['date']
        if date == '':
            messages.info(request,'pls enter a date')
        current= request.user.id
        teacherdata=teacher.objects.get(user=current)
        try:
            data=assignmenttable.objects.filter(end_date=date,courseid=teacherdata.courseid)
            return render(request,'viewassignment.html',{'data':data}) 
        except:
            return redirect('viewassignmentform')
@login_required(login_url='login1')
def editteacher(request):
    current=request.user.id
    data=CustomUser.objects.get(id=current)
    data2=teacher.objects.get(user=data)
    return render(request,'editteacher.html',{'data':data,'data2':data2}) 
@login_required(login_url='login1')
def editstudent(request):
    current=request.user.id
    data=CustomUser.objects.get(id=current)
    data2=student.objects.get(user=data)
    return render(request,'editstudent.html',{'data':data,'data2':data2}) 
def studentupdate(request):
      if request.method == 'POST':
        pk=request.user.id
        username=request.POST['username']
        first_name=request.POST['fname']
        last_name=request.POST['lname']
        email_id=request.POST['email']
        age=request.POST['age']
        contact=request.POST['contact']
        data=CustomUser.objects.get(id=pk)
        data.first_name=first_name
        data.last_name=last_name
        data.email=email_id
        data.username=username
        data.save()
        udata=student.objects.get(user=data)
        if len(request.FILES)!=0:
            if len(udata.image)>0:
                os.remove(udata.image.path)
                udata.image=request.FILES.get('image')
        udata.age=age
        udata.contact=contact
        udata.save()
        return redirect('studentprofile')        
def teacherupdate(request):
      if request.method == 'POST':
        pk=request.user.id
        username=request.POST['username']
        first_name=request.POST['fname']
        last_name=request.POST['lname']
        email_id=request.POST['email']
        age=request.POST['age']
        contact=request.POST['contact']
        data=CustomUser.objects.get(id=pk)
        data.first_name=first_name
        data.last_name=last_name
        data.email=email_id
        data.username=username
        data.save()
        udata=teacher.objects.get(user=data)
        if len(request.FILES)!=0:
            if len(udata.image)>0:
                os.remove(udata.image.path)
                udata.image=request.FILES.get('image')
        udata.age=age
        udata.contact=contact
        udata.save()
        return redirect('teacherprofile') 
@login_required(login_url='login1')    
def resetpassword(request):
    return render(request,'studentpasswordreset.html')
@login_required(login_url='login1')
def teacherreset(request):
    return render(request,'teacherreset.html')
def dogeneration(request):
    if request.method =='POST':
        username=request.POST['username']
        email=request.POST['email']
        x=str(random.randint(100000,999999))
        data=CustomUser.objects.get(username=username,email=email)
        if data.user_type == '2':
            data.set_password(x)
            data.save()
            subject="PASSWORD GENERATED"
            message="username: "+str(username)+"\n"+"password: "+str(x)+"\n"+"email: "+str(email)
            send_mail(subject,message,settings.EMAIL_HOST_USER,[data.email])
            return redirect('login1')
        if data.user_type == '3':
            data.set_password(x)
            data.save()
            subject="PASSWORD GENERATED"
            message="username: "+str(username)+"\n"+"password: "+str(x)+"\n"+"email: "+str(email)
            send_mail(subject,message,settings.EMAIL_HOST_USER,[data.email])
            return redirect('login1') 
    return redirect('resetpassword')   
@login_required(login_url='login1')
def adminstudentattendance(request):
    value=course.objects.all()
    return render(request,'adminstudentattendance.html',{'data':value})
@login_required(login_url='login1')
def adminstudentatendancedata(requsest):
    if requsest.method =='POST':
        value=requsest.POST['course']
        date=requsest.POST['date']
        data=attendancereport.objects.filter(courseid=value,date=date)
        return render(requsest,'adminviewstudentattendance.html',{'data':data})
    return redirect('adminstudentattendance')   
                       
def home(request):
    return render(request,'home.html')   
def teacherregistration(request):
    return render(request,'teacherregistration.html')
@login_required(login_url='login1')     
def editcourse(request,pk):
    data=course.objects.get(id=pk)
    return render(request,'editcourse.html',{'data':data})   
def doeditcourse(request,pk):
    if request.method =='POST':
        name=request.POST['course']  
        fee=request.POST['fee']
        duration=request.POST['duration']
        sy=request.FILES.get('syallabus')
        if sy == '':
            messages.info(request,'SELECT A PDF OR FILE TYPE')
            return redirect('editcourse')
        data=course.objects.get(id=pk)
        data.course_name=name
        data.Course_fee=fee
        data.course_duration=duration
        if len(request.FILES)!=0:
            if len(data.syallabus)>=0:
                os.remove(data.syallabus.path)
                data.syallabus=sy
        data.save()
        return redirect('managecourse')
def deletecourse(request,pk):
    data=course.objects.get(id=pk)
    data.delete()
    return redirect('managecourse')
def viewnotification(request):
    Current=request.user.id
    data1=teachernotification.objects.all()
    try:
        for i in data1:
            if i.userid.id ==Current:
             data=i
        return render(request,'viewnotification.html',{'data':data,'current':Current})
    except:
        return redirect('teacherhome')
def markview(request,pk):
    data=teachernotification.objects.get(id=pk)
    data.delete()
    return redirect('teacherhome')
def teachersyallabus(request):
    current=request.user.id
    tedata=teacher.objects.get(user=current)
    courseid=tedata.courseid.id
    data=course.objects.get(id=courseid)
    return render(request,'teachersyallabus.html',{'data':data})