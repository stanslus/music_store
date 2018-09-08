from django.db import models

# Create your models here.
class profile(models.Model):
    name=models.CharField(max_length=120,blank=False)
    description=models.TextField(max_length=120)
    age=models.CharField(max_length=120)
    location=models.CharField(max_length=120,default="my default location")
    def __str__(self):
        return self.name

#album model
class Album(models.Model):
    album_title=models.CharField(max_length=200)
    genre=models.CharField(max_length=120,blank=True)
    artist= models.CharField(max_length=120,blank=False, null=False)
    album_logo=models.CharField(max_length=1000)
    def __str__(self):
        return self.album_title

class Song(models.Model):
    album=models.ForeignKey(Album,on_delete=models.CASCADE)
    file_type=models.CharField(max_length=10)
    song_title=models.CharField(max_length=250)
    def __str__(self):
        return self.song_title
