from django.db import models

# Create your models here.


class Artist(models.Model):
    name = models.CharField(max_length=200)
    
    def __str__(self):
        return self.name
 
 
class Album(models.Model):
    title = models.CharField(max_length=200)
    artist = models.ForeignKey(Artist, on_delete=models.CASCADE)
    
    def __str__(self):
        return self.title
       

class Track(models.Model):
    name = models.CharField(max_length=200)
    composer = models.CharField(null=True, max_length=200)
    milliseconds = models.IntegerField()
    bytes = models.IntegerField()
    unitPrice = models.FloatField()
    album = models.ForeignKey(Album, on_delete=models.CASCADE, related_name="tracks")
    
    def __str__(self):
        return self.name