from django.db import models

# Create your models here.


class Artist(models.Model):
    name = models.CharField(max_length=200)
 
 
class Album(models.Model):
    title = models.CharField(max_length=200)
    artist = models.ForeignKey(Artist, on_delete=models.CASCADE)
       

class Track(models.Model):
    name = models.CharField(max_length=200)
    composer = models.CharField(max_length=200)
    milliseconds = models.IntegerField()
    bytes = models.IntegerField()
    unitPrice = models.FloatField()
    album = models.ForeignKey(Album, on_delete=models.CASCADE)