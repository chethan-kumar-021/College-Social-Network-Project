from django.urls import path
from . import views
from django.conf import settings
from django.conf.urls.static import static


urlpatterns = [
    path('',views.index,name="index"),
    path('events',views.events,name='events'),
    path('adminlogin',views.adminlogin,name='adminlogin'),
    path('viewallstudents',views.viewallstudents,name='viewallstudents'),
    path('acceptrequest/<int:id>',views.acceptrequest,name="acceptrequest"),
    path('viewallfaculty',views.viewallfaculty,name='viewallfaculty'),
    path('facultyrequest/<int:id>',views.facultyrequest,name='facultyrequest'),
    path('adminhome',views.adminhome,name='adminhome'),
    path('allchats',views.allchats,name='allchats'),
    path('addfunddetails',views.addfunddetails,name='addfunddetails'),
    path('viewfunddetails',views.viewfunddetails,name='viewfunddetails'),
    path('fundinfo/<int:id>',views.fundinfo,name='fundinfo'),
    path('addevents',views.addevents,name='addevents'),
    path('addgallery',views.addgallery,name='addgallery'),
    path('gallery',views.gallery,name='gallery'),
    path('viewcatgallery/<str:eventname>',views.viewcatgallery,name='viewcatgallery'),
    path('viewallevents',views.viewallevents,name='viewallevents'),
    path('deleteevent/<int:id>',views.deleteevent,name='deleteevent'),
    path('viewallgallery',views.viewallgallery,name='viewallgallery'),
    path('viewadmingallery/<str:eventname>',views.viewadmingallery,name='viewadmingallery'),
    path('deleteadmingallery/<str:eventname>',views.deleteadmingallery,name='deleteadmingallery'),
    path('admindeleteimage/<int:id>',views.admindeleteimage,name='admindeleteimage'),

]