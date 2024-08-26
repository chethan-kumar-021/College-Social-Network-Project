from django.urls import path
from . import views
from django.conf import settings
from django.conf.urls.static import static


urlpatterns = [
    path('',views.facultylogin,name='facultylogin'),
    path('facultyregistration',views.facultyregistration,name='facultyregistration'),
    path('typechat',views.typechat,name='typechat'),
    path('facultypublicchat',views.facultypublicchat,name='facultypublicchat'),
    path('facultyhome1',views.facultyhome1,name='facultyhome1'),
    path('facultyprivatechat',views.facultyprivatechat,name='facultyprivatechat'),
    path('facultyfunddetails',views.facultyfunddetails,name='facultyfunddetails'),
    path('facultystudentchat/<str:Rollnumber>',views.facultystudentchat,name='facultystudentchat'),
    path('facultyfacultychat/<str:facultyid>',views.facultyfacultychat,name='facultyfacultychat'),
    path('facultyforgotpassword',views.facultyforgotpassword,name='facultyforgotpassword'),
    path('facultyupdatepassword',views.facultyupdatepassword,name='facultyupdatepassword'),




]
