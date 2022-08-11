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
    path('login', views.login)
]

