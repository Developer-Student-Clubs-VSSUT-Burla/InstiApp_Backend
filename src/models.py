from django.db import models
from django.contrib.auth.models import AbstractUser


# Create your models here.
#student
#event
#project
#clubs

class User(AbstractUser):
    id=models.AutoField(primary_key=True,null=False,editable=False)
    name=models.CharField(max_length=200,null=True,blank=True)
    branch=models.CharField(max_length=200,null=True,blank=True)
    regno=models.CharField(max_length=200,null=True,blank=True)
    about=models.TextField(null=True,blank=True)
    fa=models.CharField(max_length=200,null=True,blank=True)

    def __str__(self):
        return str(self.name)

class event(models.Model):
    _id=models.AutoField(primary_key=True,null=False,editable=False)
    name=models.CharField(max_length=200,null=True,blank=True)
    description=models.CharField(max_length=200,null=True,blank=True)
    guestdetails=models.TextField(blank=True,null=True)
    expected_no_of_participants=models.IntegerField(blank=True,null=True)
    date=models.DateField(blank=True,null=True)
    venue=models.CharField(max_length=200,null=True,blank=True)
    club_name=models.CharField(max_length=200,null=True,blank=True)

    def __str__(self):
        return (self.name)

class team_member(models.Model):
    _id=models.AutoField(primary_key=True,null=False,editable=False)
    name=models.CharField(max_length=200,null=True,blank=True)
    branch=models.CharField(max_length=200,null=True,blank=True)
    regno=models.CharField(max_length=200,blank=True,null=True)

    def __str__(self):
        return (self.name)
    


class project(models.Model):
    _id=models.AutoField(primary_key=True,null=False,editable=False)
    name=models.CharField(max_length=200,null=True,blank=True)
    description=models.CharField(max_length=200,null=True,blank=True)
    contributor=models.ForeignKey(User,on_delete=models.SET_DEFAULT,default="Anonymous",null=False)
    team_members=models.ManyToManyField(team_member)
    tags= models.CharField(max_length=200,null=True,blank=True)

    def __str__(self):
        return (self.name)
