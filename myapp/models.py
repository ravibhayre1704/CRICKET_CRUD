from django.db import models



# Create your models here.
class fruit(models.Model):
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    Phone = models.CharField(max_length=10)
    Address = models.CharField(max_length=100)
    Email = models.CharField(max_length=100)
    Password = models.CharField(max_length=100,blank=True,null=True)
    is_active = models.BooleanField(default=True)
