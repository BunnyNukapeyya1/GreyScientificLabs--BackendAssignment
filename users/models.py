from venv import create
from django.db import models
from django.contrib.auth.models import AbstractUser

# Create your models here.
class User(AbstractUser):
    role = models.CharField(max_length=50,null=True,blank=True )


GENDER_CHOICES = [('MALE','male'),('FEMALE','female'),('OTHERS','others')]
class Patient(models.Model):
    name = models.CharField(max_length=255,null=True,blank=True)
    age = models.IntegerField()
    gender = models.CharField(max_length=20,choices= GENDER_CHOICES,default="OTHERS")
    address = models.TextField()
    created_by = models.ForeignKey(User,models.CASCADE,blank=True,null=True)
    
class MedicalRecord(models.Model):
    patient = models.ForeignKey(Patient,models.CASCADE,null=True,blank=True)
    symptoms = models.TextField(max_length=200,null=True,blank=True)  
    diagnosis = models.TextField(max_length=200,null=True,blank=True) 
    treatment = models.TextField(max_length=200,null=True,blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
