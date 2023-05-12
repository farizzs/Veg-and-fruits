from django.db import models

# Create your models here.

class martdb(models.Model):
    Name = models.CharField(max_length = 20, null = True, blank = True)
    Description = models.CharField(max_length=40, null=True, blank=True)
    Image = models.ImageField(upload_to="profile")

class productdb(models.Model):
    Product = models.CharField(max_length=25, null=True, blank=True)
    Image = models.ImageField(upload_to="profile")
    Description = models.CharField(max_length=25, null=True, blank=True)
    Price = models.IntegerField(null=True, blank=True)
    Category = models.CharField(max_length=15, null=True, blank=True)
    Quantity = models.CharField(max_length=20, null=True, blank=True)

class contactdb(models.Model):
    Name = models.CharField(max_length=25, null=True, blank=True)
    Email = models.EmailField(max_length=20, null=True, blank=True)
    Subject = models.CharField(max_length=100, null=True, blank=True)
    Message = models.CharField(max_length=200, null=True, blank=True)