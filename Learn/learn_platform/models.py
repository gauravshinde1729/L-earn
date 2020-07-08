from django.db import models
from django.contrib.auth.models import User
# Create your models here.

class UserProfile(models.Model):
    user = models.OneToOneField(User,null=True, on_delete=models.CASCADE)
    firstname = models.CharField(max_length = 30 ,default="anonymous")
    lastname  = models.CharField(max_length = 30 ,default="isolated")
    bio       = models.TextField(max_length = 100 ,default="Hey there! I'm using Edu-sprint")
    profile_pic = models.ImageField(null=True,blank=True)
    date_created = models.DateTimeField(auto_now_add=True, null=True)
