from django.db import models

# Create your models here.
class FundDetails(models.Model):
    FundName = models.CharField(max_length=100)
    FundType = models.CharField(max_length=100)
    FundDescription =  models.CharField(max_length=100)
    FundImage = models.ImageField(upload_to='static/products',null=True,blank=True)
    Imgname = models.CharField(max_length=50)


class Eventdetails(models.Model):
    eventname = models.CharField(max_length=100)
    eventhead = models.CharField(max_length=100)
    contact = models.CharField(max_length=100)
    eventdate = models.CharField(max_length=100)
    starttime = models.CharField(max_length=100)
    endtime = models.CharField(max_length=100)
    address = models.CharField(max_length=100)
    eventimage = models.ImageField(upload_to='static/events',null=True,blank=True)

class Gallery(models.Model):
    eventname = models.CharField(max_length=100)
    eventimage = models.ImageField(upload_to='static/gallery',null=True,blank=True)
