from django.urls import path,include
from .import views
urlpatterns = [
    path('',views.home,name='home'),
    path('login1',views.login1,name='login1'),
    path('adminhome',views.adminhome,name='adminhome'),
    path('studenthome',views.studenthome,name='studenthome'),
    path('teacherhome',views.teacherhome,name='teacherhome'),
    path('addcourse',views.addcourse,name='addcourse'),
    path('department',views.department,name='department'),
    path('assign',views.assign,name='assign'),
    path('sregistration',views.sregistration,name='sregistration'),
    path('doregistration',views.doRegistration,name='doregistration'),
    path('doLogin',views.doLogin,name='doLogin'),
    path('doaddcourse',views.doaddcourse,name='doaddcourse'),
    path('managecourse',views.managecourse,name='managecourse'),
    path('adddepartment',views.adddepartment,name='adddepartment'),
    path('addassign',views.addassign,name='addassign'),
    path('tableassign',views.tableassign,name='tableassign'),
    path('studentprofile',views.studentprofile,name='studentprofile'),
    path('teacherprofile',views.teacherprofile,name='teacherprofile'),
    path('studentatendance',views.studentatendance,name='studentatendance'),
    path('teacherrest',views.teacherreset,name='teacherreset'),
    path('studentatendancedata',views.studentatendancedata,name='studentatendancedata'),
    path('assignmentst',views.assignmentst,name='assignmentst'),
    path('doassignment',views.doassignment,name='doassignment'),
    path('studentpage',views.studentpage,name='studentpage'),
    path('teacherdetails',views.teacherdetails,name='teacherdetails'),
    path('delteacher/<int:pk>',views.delteacher,name='delteacher'),
    path('logout',views.logout,name='logout'),
    path('studentdetails',views.studentdetails,name='studentdetails'),
    path('delstudent/<int:pk>',views.delstudent,name='delstudent'),
    path('viewuser',views.viewuser,name='viewuser'),
    path('approve/<int:pk>',views.approve,name='approve'),
    path('disapprove/<int:pk>',views.disapprove,name='disapprove'),
    path('present',views.present,name='present'),
    path('stattendanceview',views.stattendanceview,name='stattendanceview'),
    path('teacherattendanceview',views.teacherattendanceview,name='teacherattendanceview'),
    path('present1',views.present1,name='present1'),
    path('absent1/<int:pk>',views.absent1,name='absent1'),
    path('teviewattendance',views.teviewattendance,name='teviewattendance'),
    path('studentleave',views.studentleave,name='studentleave'),
    path('dostudentleave',views.dostudentleave,name='dostudentleave'),
    path('viewstudentleave',views.viewstudentleave,name='viewstudentleave'),
    path('studentleaveaction',views.studentleaveaction,name='studentleaveaction'),
    path('leaveapprove<int:pk>',views.leaveapprove,name='leaveapprove'),
    path('leavedisapprove<int:pk>',views.leavedisapprove,name='leavedisapprove'),
    path('viewteacherleave',views.viewteacherleave,name='viewteacherleave'),
    path('teacherleave',views.teacherleave,name='teacherleave'),
    path('doteacherleave',views.doteacherleave,name='doteacherleave'),
    path('pushassignment<int:pk>',views.pushassignment,name='pushassignment'),
    path('viewassignment',views.viewassignment,name='viewassignment'),
    path('editteacher',views.editteacher,name='editteacher'),
    path('editstudent',views.editstudent,name='editstudent'),
    path('studentupdate',views.studentupdate,name='studentupdate'),
    path('teacherupdate',views.teacherupdate,name='teacherupdate'),
    path('resetpassword',views.resetpassword,name='resetpassword'),
    path('dogeneration',views.dogeneration,name='dogeneration'),
    path('adminstudentattendance',views.adminstudentattendance,name='adminstudentattendance'),
    path('adminstudentatendancedata',views.adminstudentatendancedata,name='adminstudentatendancedata'),
    path('teacherregistration',views.teacherregistration,name='teacherregistration'),
    path('doteacherregistration',views.doteacherregistration,name='doteacherregistration'),
    path('editcourse/<int:pk>',views.editcourse,name='editcourse'),
    path('doeditcourse/<int:pk>',views.doeditcourse,name='doeditcourse'),
    path('deletecourse/<int:pk>',views.deletecourse,name='deletecourse'),
    path('viewnotification',views.viewnotification,name='viewnotification'),
    path('markview/<int:pk>',views.markview,name='markview'),
    path('deleteassign/<int:pk>',views.deleteassign,name='deleteassign'),
    path('teachertableassign',views.teachertableassign,name='teachertableassign'),
     path('submitassignmet/<int:pk>',views.submitassignmet,name='submitassignmet'),
     path('viewassignmentform',views.viewassignmentform,name='viewassignmentform'),
     path('teacherviewstudentatten',views.teacherviewstudentatten,name='teacherviewstudentatten'),
     path('teacherviewst',views.teacherviewst,name='teacherviewst'),
     path('syallabus',views.syallabus,name='syallabus'),
     path('teachersyallabus',views.teachersyallabus,name='teachersyallabus'),
    
     
    
    
    
    
    
   
]
