from django.db import models

# Create your models here.
class log_in(models.Model):
	id = models.CharField(max_length=25,primary_key = True)
	pass_word = models.CharField(max_length=25)

class Album(models.Model):
	atrist = models.CharField(max_length=250)
	album_title = models.CharField(max_length=500)
	genre = models.CharField(max_length=100)
	album_logo = models.CharField(max_length=1000)

class Song(models.Model):
	album = models.ForeignKey(Album, on_delete=models.CASCADE)
	file_type = models.CharField(max_length = 10)
	song_title = models.CharField(max_length=250)