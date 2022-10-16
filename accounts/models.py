from django.contrib.auth.models import AbstractUser
from django.db import models

# Create your models here.

class CostumUser(AbstractUser):
  Female='Fm'
  Male='M'
  Gender_CHOICES=[
    (Female,'Female'),
    (Male,'Male')
  ]
  age=models.PositiveIntegerField(null=True,blank=True)
  male=models.CharField(max_length=2,choices=Gender_CHOICES,default=Female)
  image=models.ImageField(default='profile.jpg',null=True)