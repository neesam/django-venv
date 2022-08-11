from email.mime import image
from django.db import models

# Create your models here.
class Users(models.Model):
    name = models.CharField(max_length=255)
    age = models.IntegerField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

class Brookfield(models.Model):
    name = models.CharField(max_length=255)
    image = models.CharField(max_length=255)
    link = models.CharField(max_length=255)

class Sundial(models.Model):
    image = models.CharField(max_length=255)
    title = models.CharField(max_length=255)
    link = models.CharField(max_length=255)

class Artist(models.Model):
    artist = models.CharField(max_length=255)


class Albums(models.Model):
    name = models.CharField(max_length=255)
    image = models.CharField(max_length=255)
    artist = models.CharField(max_length=255)
    artist_image = models.CharField(max_length=255, default="you a bitch")

class Tracks(models.Model):
    tracklist_id = models.IntegerField(default=0)
    title = models.CharField(max_length=255)
    album = models.CharField(max_length=255)
    artist = models.CharField(max_length=255)
    extension = models.CharField(max_length=255, default="idk")

class RYM(models.Model):
    title = models.CharField(max_length=255)
    artist = models.CharField(max_length=255)

class RandAlbum(models.Model):
    album = models.CharField(max_length=255)

class Ryan(models.Model):
    album = models.CharField(max_length=255)
    artist = models.CharField(max_length=255)

class RandomArtist(models.Model):
    artist = models.CharField(max_length=255)

class RandPerson(models.Model):
    album = models.CharField(max_length=255)

class GreatScene(models.Model):
    album = models.CharField(max_length=255)

class Jazz(models.Model):
    album = models.CharField(max_length=255)