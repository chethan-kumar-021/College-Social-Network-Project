from django.urls import path
from . import views
from django.conf import settings
from django.conf.urls.static import static


urlpatterns = [
    path('',views.studentlogin,name='studentlogin'),
    path('studentregistration',views.studentregistration,name='studentregistration'),
    path('chat',views.chat,name='chat'),
    path("studenthome",views.studenthome,name='studenthome'),
    path('publicchat',views.publicchat,name='publicchat'),
    path('studentprivatechat',views.studentprivatechat,name='studentprivatechat'),
    path('facultychat/<str:facultyid>/',views.facultychat,name='facultychat'),
    path('facultyallchat',views.facultyallchat,name='facultyallchat'),
    path('studentchat/<str:Rollnumber>/',views.studentchat,name='studentchat'),
    path('facultytofaculty',views.facultytofaculty,name='facultytofaculty'),
    path('studenttofaculty/<str:reciever>/',views.studenttofaculty,name='studenttofaculty'),
    path('studentfund',views.studentfund,name='studentfund'),
    path('studenttofacultychat',views.studenttofacultychat,name='studenttofacultychat'),
    path('studentfaculty/<str:facultyid>/',views.studentfaculty,name='studentfaculty'),
    path('oldstudenthome',views.oldstudenthome,name='oldstudenthome'),
    path('addjobdetails',views.addjobdetails,name='addjobdetails'),
    path('jobnotification',views.jobnotification,name='jobnotification'),
    path('acceptfund',views.acceptfund,name='acceptfund'),
    path('updatefunddetails',views.updatefunddetails,name='updatefunddetails'),
    path('jobdetails',views.jobdetails,name='jobdetails'),
    path('oldstudentfunddetails',views.oldstudentfunddetails,name='oldstudentfunddetails'),
    path('oldstudentdonation/<int:id>',views.oldstudentdonation,name='oldstudentdonation'),
    path('studentfunddonationdetails/<int:id>',views.studentfunddonationdetails,name='studentfunddonationdetails'),
    path('studentstudentprivatechat',views.studentstudentprivatechat,name='studentstudentprivatechat'),
    path('studentstudentprivate/<str:Rollnumber>',views.studentstudentprivate,name='studentstudentprivate'),
    path('studentforgotpassword',views.studentforgotpassword,name='studentforgotpassword'),
    path('studentupdatepassword',views.studentupdatepassword,name='studentupdatepassword'),


]
