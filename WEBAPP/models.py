from django.db import models

# Create your models here.
class Signupdb(models.Model):
    username = models.CharField(max_length=50, null=True, blank=True)
    emailid = models.EmailField(max_length=50, null=True, blank=True)
    password = models.CharField(max_length=15, null=True, blank=True)
    confirm_password = models.CharField(max_length=15, null=True, blank=True)
