from email import message
from logging import warning
from django.shortcuts import render,redirect

from facultyapp.models import FacultyRegistration
from adminmodule.models import FundDetails
from .models import StudentRegistration,Publicmessgage,PrivateChat,JobDetails,FundAmount,StudentPrivateChat
from django.contrib import messages
import datetime



# Create your views here.
def studentlogin(request):
    if request.method=="POST":
        studentid = request.POST['studentId']
        studentpassword = request.POST['studentpassword']

        a = StudentRegistration.objects.filter(Rollnumber=studentid,Password=studentpassword,status='active',StudentType='persuing')
        b = StudentRegistration.objects.filter(Rollnumber=studentid,Password=studentpassword,status='active',StudentType='old')
        if a.exists():
            request.session['studentid'] = studentid
            return render(request,'studenthome.html',{'id':request.session['studentid']})
        if b.exists():
            return render(request,'oldstudent.html',{'id':request.session['studentid']})
        messages.add_message(request,messages.WARNING,'Invalid Credentials')
        return render(request,"studentlogin.html")
    return render(request,"studentlogin.html")


def studentregistration(request):
    if request.method == "POST":
        studentname = request.POST['studentname']
        studentrollno = request.POST['studentrollno']
        studentemail = request.POST['studentemail']
        phoneno = request.POST['phoneno']
        semister = request.POST['semister']
        year = request.POST['year']
        group = request.POST['group']
        studenttype = request.POST['studenttype']
        studentgender = request.POST['studentgender']
        address = request.POST['address']
        password = request.POST['password']
        status = "inactive"
        studenttype = request.POST['studenttype']

        aa = StudentRegistration.objects.filter(Rollnumber=studentrollno,Password=password)
        print(aa)
        print(aa.exists())
        if aa.exists() == True:
            messages.add_message(request,messages.WARNING,"Invalid Credentials")
            return render(request,'studentregistration.html')
        else:
            a = StudentRegistration(studentname=studentname,Rollnumber=studentrollno,Email=studentemail,contact=phoneno,semister=semister,year=year,group=group,StudentType=studenttype,Gender=studentgender,Address=address,Password=password,status=status)
            a.save()
            return render(request,'studentlogin.html')
    return render(request,'studentregistration.html')

def chat(request):
    return render(request,'chat.html')



def studenthome(request):
    return render(request,'studenthome.html')


def publicchat(request):
    stu_id = request.session['studentid']
    facultyid = request.session['facultyid']
    if request.method=="POST":
        messages = request.POST['messages']
        stu_id = request.session['studentid']
        timining = datetime.time()
        print(request.session['facultyid'])
        dc=Publicmessgage(studentid=stu_id,studentmessage=messages)
        dc.save()
    data = Publicmessgage.objects.all()
    return render(request,'publicchat.html',{'data':data,'stu_id':stu_id})





def studentprivatechat(request):
    stu_id = request.session['studentid']
    print(stu_id)
    dc = FacultyRegistration.objects.filter(status='active')
    data = StudentRegistration.objects.filter(status='active')
    return render(request,'studentprivatechat.html',{'dc':dc,'data':data,'stu_id' :stu_id})




def facultyallchat(request):

    if request.method =="POST":
        senderid = request.session['studentid']
        receiverid = request.session['faculty_id']
        messages = request.POST['messages']
        timining = datetime.time()
        dc = PrivateChat(Senderid=senderid,Receiverid=receiverid,studentmessage=messages,timing = timining)
        dc.save()
        dc = PrivateChat.objects.filter(Senderid=request.session['studentid'],Receiverid=request.session['faculty_id'])
        return render(request,'facultychat.html',{'data':dc,'facultyid':receiverid,'studentid':request.session['studentid']})
    dc = PrivateChat.objects.filter(Senderid=request.session['studentid'],Receiverid=request.session['faculty_id'])
    return render(request,'facultychat.html',{'data':dc,'facultyid':request.session['faculty_id'],'studentid':request.session['studentid']})

def facultychat(request,facultyid):
    print(facultyid)
    receiver = facultyid
    sender = request.session['studentid']
    print(sender)
    faculty = request.session['facultyid']
    dc = PrivateChat.objects.filter(Senderid=sender,Receiverid=faculty)
    return render(request,'facultychat.html',{'data':dc,'sender':sender,'reciever':receiver})



def studenttofaculty(request,reciever):
    if request.method =="POST":
        print("==============")
        print(reciever)
        messages = request.POST["messages"]
        sender = request.session['studentid']
        timining = datetime.time()
        dc = PrivateChat(Senderid=sender,Receiverid=reciever,studentmessage=messages,timing=timining)
        dc.save()
        dc = PrivateChat.objects.filter(Senderid=sender,Receiverid=reciever)
    dc = PrivateChat.objects.filter(Senderid=sender,Receiverid=reciever)
    return render(request,'facultychat.html',{'data':dc,'sender':sender,'reciever':reciever})


def studenttofacultychat(request):
    dc = FacultyRegistration.objects.filter(status='active')

    return render(request,'studenttofacultychat.html',{'dc':dc})

def studentfaculty(request,facultyid):
    print(facultyid)
    Receiver = facultyid
    print("---------------------")
    sender = request.session['studentid']
    print(sender)
    if request.method == "POST":
        messages = request.POST['messages']
        dc = PrivateChat(senderid=sender,message=messages,receiverid=Receiver)
        dc.save()
        dc = PrivateChat.objects.all()
        return render(request,'studentfacultychat.html',{'facultyid':Receiver,'dc':dc,'sender':sender})

    dc = PrivateChat.objects.all()
    return render(request,'studentfacultychat.html',{'facultyid':Receiver,'dc':dc,'sender':sender})

def facultytofaculty(request):
    sender =  request.session['facultyid']
    receiverid = request.session['faculty_id']
    if request.method == "POST":
        sender =  request.session['facultyid']
        print(sender)
        receiverid = request.session['faculty_id']
        print(receiverid)
        timining = datetime.time()
        messages = request.POST['messages']
        print(messages)
        dc= PrivateChat(Senderid=sender,Receiverid=receiverid,studentmessage=messages,timing=timining)
        dc.save()
        dc = PrivateChat.objects.filter(Senderid=sender,Receiverid=receiverid)
        return render(request,'facultytofaculty.html',{'data':dc,'sender':sender})
    dc = PrivateChat.objects.filter(Senderid=sender,Receiverid=receiverid)
    return render(request,'facultytofaculty.html',{'data':dc,'sender':sender})


def studentchat(request,Rollnumber):
    print(Rollnumber)
    sender = Rollnumber
    receiver = request.session['facultyid']
    dc = PrivateChat.objects.filter(Receiverid=receiver,Senderid=sender)
    return render(request,'studentchat.html',{'data':dc})


def studentfund(request):
    dc = FundDetails.objects.all()
    return render(request,'studentfund.html',{'dc':dc})


def oldstudenthome(request):
    return render(request,'oldstudent.html',{'id':request.session['studentid']})

def addjobdetails(request):
    if request.method == "POST":
        jobrole = request.POST['jobrole']
        qualification = request.POST['qualification']
        company = request.POST['company']
        Experience = request.POST['Experiance']
        filename = request.FILES['filename']
        print("--------------------")
        dc = JobDetails(jobrole=jobrole,qualification=qualification,company=company,Experience=Experience,filename=filename)
        dc.save()
        messages.add_message(request,messages.SUCCESS,'Invalid Credentials')
        return redirect('oldstudenthome')

def jobnotification(request):
    dc = JobDetails.objects.all()
    return render(request,'jobnotification.html',{'dc':dc})

def acceptfund(request):
    studentid = request.session['studentid']
    print(studentid)
    dc = StudentRegistration.objects.filter(Rollnumber=studentid)

    return render(request,'acceptfund.html',{'dc':dc})

def updatefunddetails(request):
    if request.method=="POST":
        studentname = request.POST['studentname']
        fundamount = request.POST['fundamount']
        dc = FundAmount(studentname=studentname,fundamount=fundamount)
        dc.save()
        return redirect('acceptfund')



def jobdetails(request):
    return render(request,'jobdetails.html')

def oldstudentfunddetails(request):
    dc = FundDetails.objects.all()
    return render(request,'oldstudentfunddetails.html',{'dc':dc})



def oldstudentdonation(request,id):
    print(id)
    if request.method=="POST":
        donationid = request.POST['donationid']
        studentname = request.POST['studentname']
        nameoncard = request.POST['nameoncard']
        cardnumber = request.POST['cardnumber']
        cardcvv = request.POST['cardcvv']
        expiredate = request.POST['expiredate']
        amount = request.POST['amount']
        studentroll =request.session['studentid']
        dc = FundAmount(donationid=donationid,studentid=studentroll,studentname=studentname,nameoncard=nameoncard,cardnumber=cardnumber,cardcvv=cardcvv,expiredate=expiredate,fundamount=amount)
        dc.save()
        return render(request,'oldstudentdonation.html',{'id':id,'msg':'payment success'})

    return render(request,'oldstudentdonation.html',{'id':id})


def studentfunddonationdetails(request,id):
    print(id)
    if request.method=="POST":
        donationid = request.POST['donationid']
        studentname = request.POST['studentname']
        nameoncard = request.POST['nameoncard']
        cardnumber = request.POST['cardnumber']
        cardcvv = request.POST['cardcvv']
        expiredate = request.POST['expiredate']
        amount = request.POST['amount']
        studentroll =request.session['studentid']
        dc = FundAmount(donationid=donationid,studentid=studentroll,studentname=studentname,nameoncard=nameoncard,cardnumber=cardnumber,cardcvv=cardcvv,expiredate=expiredate,fundamount=amount)
        dc.save()
        return render(request,'studentfunddonationdetails.html',{'id':id,'msg':'payment success'})
    return render(request,'studentfunddonationdetails.html',{'id':id})



def studentstudentprivatechat(request):
    dc = StudentRegistration.objects.filter(status='active')
    c=request.session['studentid']
    return render(request,'studentstudentprivatechat.html',{'dc':dc,'studentid':c})

def studentstudentprivate(request,Rollnumber):
    print(Rollnumber)
    Receiver = Rollnumber
    request.session["receiver_id"] = Receiver
    sender = request.session['studentid']

    if request.method == "POST":
        messages = request.POST['messages']
        dc = StudentPrivateChat(senderid = sender,receiverid=Receiver,message = messages)
        dc.save()
        dc1 =  StudentPrivateChat.objects.filter(senderid=sender,receiverid=Receiver)
        dc2 = StudentPrivateChat.objects.filter(senderid=Receiver,receiverid=sender)
        data = dc1 | dc2
        print(data)
        return render(request,'studentstudentprivate.html',{'data':data,'Receiver':Receiver,'sender':sender,'Rollnumber':Rollnumber})


    dc1 =  StudentPrivateChat.objects.filter(senderid=sender,receiverid=Receiver)
    dc2 = StudentPrivateChat.objects.filter(senderid=Receiver,receiverid=sender)
    data = dc1 | dc2
    print(data)
    return render(request,'studentstudentprivate.html',{'data':data,'Receiver':Receiver,'sender':sender,'Rollnumber':Rollnumber})




def studentforgotpassword(request):
    if request.method=="POST":
        studentemail = request.POST['studentemail']
        sql=StudentRegistration.objects.filter(Email=studentemail).exists()
        print(sql)
        if sql==False:
            msg='nodata'
            return render(request,"studentforgotpassword.html",{'msg':msg})
        else:
            msg="data"
            request.session['student_email']=studentemail
            return render(request,"studentforgotpassword.html",{'msg':msg})
    return render(request,"studentforgotpassword.html",{'msg':'nodata'})

def studentupdatepassword(request):
    msg='password not matching'
    if request.method=="POST":
        password = request.POST['password']
        password1 = request.POST['password1']
        if password == password1:
            email=request.session['student_email']
            data = StudentRegistration.objects.get(Email=email)
            data.Password = password
            data.save()
            return render(request,'studentlogin.html')
    return render(request,"studentforgotpassword.html",{'msg':'data','cont':'Email not valid'})









