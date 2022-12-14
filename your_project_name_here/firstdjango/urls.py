from django.urls import path     
from . import views
urlpatterns = [
    path('createUser', views.createUser),
    path('', views.index),
    path('brookfield', views.brookfield),
    path('sundial', views.sundial),
    path('album/<str:name>', views.album),
    path('magic-sheet', views.magicSheet),
    path('random-album', views.randomAlbum),
    path('ryan', views.ryan),
    path('random-artist', views.randomArtist),
    path('top-random', views.randomPersonTop),
    path('great-scene', views.greatScene),
    path('jazz', views.jazz),
    path('login', views.login),
    path('listening-log', views.listeningLog),
    path('add-listening-log', views.addListeningLog),
    path('add-log', views.addToLog),
    path('ryan-rym', views.ryan),
    path('sms', views.sms),
    path('mlep', views.mlep),
    path('utstms', views.utstms),
    path('mela', views.mela),
    path('charts', views.charts),
    path('recs', views.recs),
    path('rymchallenge', views.rymchallenge),
    path('rymrecs', views.rymrecs),
    path('criterion', views.criterion),
    path('melodicEng', views.melEng)
]

