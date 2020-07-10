from django.db import models
from django.contrib.auth.models import User

class TutorApplicationRequest(models.Model):
    requestID = models.AutoField(primary_key=True)
    firstname = models.CharField(max_length=30,default="Tutor")
    lastname  = models.CharField(max_length=30,default="Tutor")
    email     = models.CharField(max_length=50)
    phonenumber = models.CharField(max_length=15)
    city      = models.CharField(max_length=20)
    details   = models.CharField(max_length=500)
    experience = models.CharField(max_length=200)

    def __str__(self):
        return (self.firstname)

class TutorProfile(models.Model):
    TutorID   = models.AutoField(primary_key=True)
    user      = models.OneToOneField(User,null=True, on_delete=models.CASCADE)
    firstname = models.CharField(max_length=30, default="Tutor")
    lastname  = models.CharField(max_length=30, default="Tutor")
    bio       = models.CharField(max_length=500)


    def __str__(self):
        return (str(self.TutorID))


