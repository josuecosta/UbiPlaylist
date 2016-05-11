from django.db import models

# Import User class from django
from django.contrib.auth.models import User


# Class Music
class Music(models.Model):
    title = models.CharField(max_length=100)
    artist = models.CharField(max_length=100)
    album = models.CharField(max_length=100)

    def __str__(self):
        return self.title + ' - ' + self.artist


# Class Playlist
class Playlist(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    music = models.ForeignKey(Music, on_delete=models.CASCADE)

    def __str__(self):
        return str(self.user.pk) + ' - ' + str(self.music.pk)

