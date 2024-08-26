from django.db import models

# Create your models here.


class FacultyRegistration(models.Model):
    Facultyname = models.CharField(max_length=100)
    facultyid = models.CharField(max_length=50)
    facultyemail = models.CharField(max_length=50)
    facultypassword = models.CharField(max_length=50)
    facultydept = models.CharField(max_length=50)
    facultyroll = models.CharField(max_length=50)
    contact = models.CharField(max_length=50)
    status  = models.CharField(max_length=50)
