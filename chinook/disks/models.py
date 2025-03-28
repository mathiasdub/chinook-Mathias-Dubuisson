from django.db import models

# Create your models here.


class Artist(models.Model):
    id = models.IntegerField()
    name = models.CharField(max_length=200)
 
 
class Album(models.Model):
    id = models.IntegerField()
    title = models.CharField(max_length=200)
    artist = models.ForeignKey(Artist)
       

class Track(models.Model):
    id = models.IntegerField()
    name = models.CharField(max_length=200)
    composer = models.CharField(max_length=200)
    milliseconds = models.IntegerField()
    bytes = models.IntegerField()
    unitPrice = models.FloatField()
    album = models.ForeignKey(Album)