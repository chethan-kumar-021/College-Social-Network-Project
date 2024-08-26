from django.shortcuts import render,redirect
from django.conf import settings
from django.contrib import messages
from studentapp.models import StudentRegistration,Publicmessgage,FundAmount
from facultyapp.models import FacultyRegistration
from .models import FundDetails,Eventdetails,Gallery
from django.core.mail import send_mail
from datetime import datetime
from django.core.files.storage import default_storage
from django.core.files.storage import FileSystemStorage



# Create your views here.




def index(request):
    return render(request,'index.html')


def adminlogin(request):
    if request.method=="POST":
        adminemail = request.POST['adminemail']
        adminpassword = request.POST['adminpassword']
        if adminemail == "admin@gmail.com" and adminpassword =="admin":
            request.session['adminemail'] = adminemail
            return render(request,'adminhome.html')
        else:
            messages.add_message(request,messages.WARNING,"Invalid Credentials")
            return render(request,'adminlogin.html')
    return render(request,"adminlogin.html")

def viewallstudents(request):
    # dc = StudentRegistration.objects.only(studentname,Rollnumber,Email,contact,semister,year,group,StudentType,Gender,Address,status)
    dc= StudentRegistration.objects.all()
    return render(request,'viewallstudents.html',{'data':dc})




def acceptrequest(request,id):
    dc= StudentRegistration.objects.get(id=id)
    dc.status="active"
    name=dc.studentname
    dc.save()
    print(dc)
    message = f'Hi {name}'
    subject =" Alumin "
    m0 = "your registration is active you can login now"
    # m1 = "This message is automatic generated so dont reply to this Mail"
    # m2 = "Thanking you"
    # m3 = "Regards"
    # m4 = "Admin"
    # email_from = settings.EMAIL_HOST_USER
    # recipient_list = [email]
    # text = message + '\n' + '\n' + m1 + '\n' + m2 + '\n' + m3 + '\n' + m4
    # send_mail(subject, text, email_from, recipient_list,fail_silently=False,)
    return redirect('viewallstudents')

def viewallfaculty(request):
    dc = FacultyRegistration.objects.all()
    return render(request,'viewallfaculty.html',{'data':dc})


def facultyrequest(request,id):
    dc = FacultyRegistration.objects.get(id=id)
    dc.status="active"
    name = dc.Facultyname
    dc.save()
    message = f'Hi {name}'
    subject =" Alumin "
    m0 = "your registration is active you can login now"
    # m1 = "This message is automatic generated so dont reply to this Mail"
    # m2 = "Thanking you"
    # m3 = "Regards"
    # m4 = "Admin"
    # email_from = settings.EMAIL_HOST_USER
    # recipient_list = [email]
    # text = message + '\n' + '\n' + m1 + '\n' + m2 + '\n' + m3 + '\n' + m4
    # send_mail(subject, text, email_from, recipient_list,fail_silently=False,)
    return redirect('viewallfaculty')

def adminhome(request):
    return render(request,'adminhome.html')

def allchats(request):
    adminemail = request.session['adminemail']
    dc = Publicmessgage.objects.all()
    return render(request,'allchats.html',{'data':dc})


def addfunddetails(request):
    if request.method == "POST":
        fundname = request.POST['fundname']
        fundtype = request.POST['fundtype']
        description = request.POST['description']
        filecontent = request.FILES['fundimage']

        dc = FundDetails(FundName=fundname,FundType=fundtype,FundDescription=description,FundImage=filecontent,Imgname=filecontent)
        dc.save()
        print(fundname,fundtype,description,filecontent)
    return render(request,'addfunddetails.html')


def viewfunddetails(request):
    dc = FundDetails.objects.all()
    return render(request,'viewfunddetails.html',{'dc':dc})


def fundinfo(request,id):
    print(id)
    dc = FundDetails.objects.filter(id=id)
    data= FundAmount.objects.all()
    return render(request,'fundinfo.html',{'dc':dc,'i':data})


def addevents(request):
    if request.method=="POST":
        eventname = request.POST['eventname']
        eventhead = request.POST['eventhead']
        contact = request.POST['contact']
        eventdate = request.POST['eventdate']
        starttime = request.POST['starttime']
        endtime = request.POST['endtime']
        address = request.POST['address']
        eventimage = request.FILES['eventimage']
        a = Eventdetails(eventname=eventname,eventhead=eventhead,contact=contact,eventdate=eventdate,starttime=starttime,endtime=endtime,address=address,eventimage=eventimage)
        a.save()

    return render(request,'addevents.html')


def addgallery(request):
    if request.method=="POST":
        eventname = request.POST['eventname']
        eventimage = request.FILES['eventimage']
        d = Gallery(eventname=eventname,eventimage=eventimage)
        d.save()
    return render(request,'addgallery.html')

def events(request):
    data = Eventdetails.objects.all()
    return render(request,'events.html',{'i':data})



def gallery(request):
    sql=Gallery.objects.values('eventname').distinct()
    # sql = Gallery.objects.order_by('eventname').values().distinct()
    return render(request,'gallery.html',{'i':sql})

def viewcatgallery(request,eventname):
    print(eventname)
    data = Gallery.objects.filter(eventname=eventname)
    return render(request,'viewcatgallery.html',{'data':data})

def viewallevents(request):
    sql=Eventdetails.objects.all()
    return render(request,'viewallevents.html',{'sql':sql})



def deleteevent(request,id):
    print(id)
    Eventdetails.objects.filter(id=id).delete()
    return redirect('viewallevents')


def viewallgallery(request):
    sql=Gallery.objects.values('eventname').distinct()
    return render(request,'viewallgallery.html',{'i':sql})

def viewadmingallery(request,eventname):
    print(eventname)
    data = Gallery.objects.filter(eventname=eventname)
    return render(request,'viewadmingallery.html',{'data':data})

def deleteadmingallery(request,eventname):
    print(eventname)
    Gallery.objects.filter(eventname=eventname).delete()
    return redirect('viewallgallery')

def admindeleteimage(request,id):
    print(id)
    Gallery.objects.filter(id=id).delete()
    return redirect('viewallgallery')

