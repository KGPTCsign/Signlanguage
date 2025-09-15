from django.db import models

# Create your models here.
class LoginTable(models.Model):
    username=models.CharField(max_length=100,null=True,blank=True)
    password=models.CharField(max_length=100,null=True,blank=True)
    usertype=models.CharField(max_length=100,null=True,blank=True)

class UserTable(models.Model):
    name=models.CharField(max_length=100,null=True,blank=True)
    email=models.CharField(max_length=100,null=True,blank=True)
    contactno=models.BigIntegerField(null=True,blank=True)
    gender=models.CharField(max_length=100,null=True,blank=True)
    loginid=models.ForeignKey(LoginTable,on_delete=models.CASCADE,null=True,blank=True)

class ComplaintTable(models.Model):
    complaint=models.CharField(max_length=200,null=True,blank=True)
    createdAt=models.DateField(auto_now_add=True,null=True,blank=True)
    reply=models.CharField(max_length=100,null=True,blank=True)
    userid=models.ForeignKey(UserTable,on_delete=models.CASCADE,null=True,blank=True)

class FeedbackTable(models.Model):
    feedback=models.CharField(max_length=100,null=True,blank=True)
    createdAt=models.DateField(auto_now_add=True,null=True,blank=True)
    userid=models.ForeignKey(UserTable,on_delete=models.CASCADE,null=True,blank=True)