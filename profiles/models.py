from django.db import models

# Create your models here.
class profile(models.Model):
    name=models.CharField(max_length=120,blank=False)
    description=models.TextField(max_length=120)
    age=models.CharField(max_length=120)
    location=models.CharField(max_length=120,default="my default location")
    def __str__(self):
        return self.name
