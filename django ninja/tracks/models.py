from django.db import models

# Create your models here.
class Track(models.Model):
    title = models.CharField(max_length=200)
    artist = models.CharField(max_length=200)
    duration = models.FloatField()
    last_play = models.DateTimeField()
