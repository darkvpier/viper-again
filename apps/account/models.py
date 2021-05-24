from django.contrib.auth.models import AbstractUser
from django.db import models

class User(AbstractUser):
    is_coordinator = models.BooleanField(default=False)
    is_student = models.BooleanField(default=False)
    first_name = models.CharField(max_length=100)
    last_name =  models.CharField(max_length=100)


class Coordinator(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, primary_key=True)
    phone = models.CharField(max_length=20)
    department = models.CharField(max_length=200)
    def __str__(self):
        return f"{self.username}"

class Student(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, primary_key=True)
    phone = models.CharField(max_length=20)
    department = models.CharField(max_length=200)
    def __str__(self):
        return f"{self.user}"