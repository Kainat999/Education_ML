from django.contrib.auth.models import User
from django.db import models

class Interest(models.Model):
    title = models.CharField(max_length=100)

class Goal(models.Model):
    description = models.TextField()

class UserProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    bio = models.TextField()
    preferences = models.TextField()
    interests = models.ManyToManyField(Interest)
    goals = models.ManyToManyField(Goal)
