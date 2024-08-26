from email import message
from logging import warning
from django.shortcuts import render
from studentapp.models  import PrivateChat, StudentRegistration,Publicmessgage,FundAmount
from .models import FacultyRegistration
from adminmodule.models import FundDetails
from django.contrib import messages
# Create your views here.
def facultylogin(request):
    if request.method == "POST":
        facultyid = request.POST['facultid']
        request.session['facultyid'] = facultyid
        facultypassword = request.POST['facultypassword']
        dc = FacultyRegistration.objects.filter(facultyid=facultyid,facultypassword=facultypassword,status='active').exists()
        if dc:
            return render(request,'facultyhome.html')
        else:
            request.session['facultyid'] = facultyid
            messages.add_message(request,messages.WARNING,"Credential's are not valid")
            return render(request,'facultylogin.html')
    return render(request,'facultylogin.html')




def facultyregistration(request):
    if request.method == "POST":
        Facultyname = request.POST['facultyname']
        facultyid = request.POST['facultyid']
        facultyemail = request.POST['facultyemail']
        facultypassword = request.POST['facultypassword']
        facultydept = request.POST['facultydept']
        facultyroll = request.POST['facultyroll']
        contact = request.POST['contact']
        status="inactive"
        data = FacultyRegistration.objects.filter(facultyroll=facultyroll,facultypassword=facultypassword).exists()
        if data:
            messages.add_message(request,messages.WARNING,'details already exists')
            return render(request,'facultyregistration.html')
        else:
            dc = FacultyRegistration(Facultyname=Facultyname,facultyid=facultyid,facultyemail=facultyemail,facultypassword=facultypassword,facultydept=facultydept,facultyroll=facultyroll,contact=contact,status=status)
            dc.save()
            return render(request,'facultylogin.html')
    return render(request,'facultyregistration.html')



def typechat(request):
    return render(request,'typechat.html')



def facultyhome1(request):
    return render(request,'facultyhome1.html')



def facultypublicchat(request):
    if request.method == "POST":
        msg = request.POST['messages']
        print(request.session['facultyid'])
        dc = Publicmessgage(studentmessage = msg,Faculty=request.session['facultyid'])
        dc.save()
    dc = Publicmessgage.objects.all()
    return render(request,'facultypublicchat.html',{'data':dc,'faculty':request.session['facultyid'],'facultyid':request.session['facultyid']})


def facultyprivatechat(request):
    dc = FacultyRegistration.objects.filter(status='active')
    data = StudentRegistration.objects.filter(status='active')
    return render(request,'facultyprivatechat.html',{'dc':dc,'data':data,'myid':request.session['facultyid']})



def facultystudentchat(request,Rollnumber):
    studentid = Rollnumber
    facultyid = request.session['facultyid']
    print(studentid,facultyid)
    if request.method == 'POST':
        print(studentid,facultyid)
        messages = request.POST['messages']
        dc = PrivateChat(senderid = facultyid,receiverid=studentid,message = messages)
        dc.save()
        dc1= PrivateChat.objects.filter(senderid=facultyid,receiverid=studentid)
        dc2= PrivateChat.objects.filter(senderid=studentid,receiverid=facultyid)
        dc = dc1 | dc2
        print(dc)
        return render(request,'facultystudentchat.html',{'dc':dc,'Rollnumber':studentid,'sender':facultyid,'studentid':studentid})
    dc= PrivateChat.objects.filter(senderid=facultyid,receiverid=studentid)
    return render(request,'facultystudentchat.html',{'dc':dc,'Rollnumber':studentid,'sender':facultyid,'studentid':studentid})


def facultyfacultychat(request,facultyid):

    facultyloggedin = request.session['facultyid']
    if request.method == "POST":
        print(facultyid,facultyloggedin)
        messages = request.POST['messages']
        dc = PrivateChat(senderid = facultyloggedin,receiverid=facultyid,message = messages)
        dc.save()
        dc1 =  PrivateChat.objects.filter(senderid=facultyloggedin,receiverid=facultyid)
        dc2 = PrivateChat.objects.filter(senderid=facultyid,receiverid=facultyloggedin)
        data = dc1 | dc2
        print(data)
        return render(request,'facultyfacultychat.html',{'data':data,'facultyid':facultyid,'facultyloggedin':facultyloggedin})


    dc1 =  PrivateChat.objects.filter(senderid=facultyloggedin,receiverid=facultyid)
    dc2 = PrivateChat.objects.filter(senderid=facultyid,receiverid=facultyloggedin)
    data = dc1 | dc2
    print(data)
    return render(request,'facultyfacultychat.html',{'data':data,'facultyid':facultyid,'facultyloggedin':facultyloggedin})

def facultyfunddetails(request):
    dc = FundDetails.objects.all()
    data =FundAmount.objects.all()
    return render(request,'facultyfunddetails.html',{'dc':dc,'i':data})



def facultyforgotpassword(request):
    if request.method=="POST":
        facultyemail = request.POST['facultyemail']
        sql=FacultyRegistration.objects.filter(facultyemail=facultyemail).exists()
        print(sql)
        if sql==False:
            msg='nodata'
            return render(request,"facultyforgotpassword.html",{'msg':msg})
        else:
            msg="data"
            request.session['faculty_email']=facultyemail
            return render(request,"facultyforgotpassword.html",{'msg':msg})
    return render(request,'facultyforgotpassword.html',{'msg':'nodata'})


def facultyupdatepassword(request):
    msg='password not matching'
    if request.method=="POST":
        password = request.POST['password']
        password1 = request.POST['password1']
        if password == password1:
            email=request.session['faculty_email']
            data = FacultyRegistration.objects.get(facultyemail=email)
            data.facultypassword = password
            data.save()
            return render(request,'facultylogin.html')
        else:
            return render(request,'facultylogin.html',{'msg':msg})

    return render(request,"facultyupdatepassword.html",{'msg':'data','cont':'Email not valid'})



