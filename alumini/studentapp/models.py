from django.db import models
from datetime import datetime

# Create your models here.
class StudentRegistration(models.Model):
    studentname = models.CharField(max_length=100)
    Rollnumber = models.CharField(max_length=100)
    Email  = models.EmailField()
    contact = models.CharField(max_length=10)
    semister = models.CharField(max_length=50)
    year = models.CharField(max_length=50)
    group = models.CharField(max_length=100)
    StudentType = models.CharField(max_length=100)
    Gender = models.CharField(max_length=50)
    Address = models.CharField(max_length=50)
    Password = models.CharField(max_length=50)
    status = models.CharField(max_length=50)


class Publicmessgage(models.Model):
    studentid = models.CharField(max_length=100)
    studentmessage = models.CharField(max_length=100)
    timing = models.TimeField(default=datetime.now, blank=True)
    Faculty = models.CharField(max_length=100)

class PrivateChat(models.Model):
    senderid = models.CharField(max_length=100)
    receiverid = models.CharField(max_length=100)
    message = models.CharField(max_length=100)
    timing = models.DateField(auto_now_add=True)


class StudentPrivateChat(models.Model):
    senderid = models.CharField(max_length=100)
    receiverid = models.CharField(max_length=100)
    message = models.CharField(max_length=100)
    timing = models.DateField(auto_now_add=True)

class JobDetails(models.Model):
        jobrole = models.CharField(max_length=100)
        qualification = models.CharField(max_length=100)
        company = models.CharField(max_length=100)
        Experience = models.CharField(max_length=100)
        filename = models.FileField()



class FundAmount(models.Model):
    donationid = models.CharField(max_length=100)
    studentid = models.CharField(max_length=100)
    studentname = models.CharField(max_length=100)
    nameoncard = models.CharField(max_length=100)
    cardnumber = models.CharField(max_length=100)
    cardcvv = models.CharField(max_length=100)
    expiredate = models.CharField(max_length=100)
    fundamount = models.CharField(max_length=100)




