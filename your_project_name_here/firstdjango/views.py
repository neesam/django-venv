from django.shortcuts import render, HttpResponse, redirect
import random
from django.http import JsonResponse
from firstdjango.models import Users, Brookfield, Sundial, Albums, Tracks, RYM, RandAlbum, Artist, Ryan, RandomArtist, RandPerson, GreatScene, Jazz, Log

def index(request):
    context = {
        'users': Users.objects.all()
    }
    return render(request, 'info.html', context)

def createUser(request):

    Users.objects.create(name=request.POST['name'], age=request.POST['age'])
    return redirect('/')

def sundial(request):

    context = {
        'sundial': Sundial.objects.all().order_by('?')
    }
    return render(request, 'sundial.html', context)

def brookfield(request):
    context = {
        'brookfield': Brookfield.objects.all().order_by('?')
    }

    return render(request, 'brookfield.html', context)

def album(request, name):

    context = {
        'albums': Albums.objects.get(name=name),
        'tracks': Tracks.objects.filter(album=name),
        'brookfield': Brookfield.objects.all()

    }
    return render(request, 'album.html', context)

def magicSheet(request):

    context = {
        'album': RYM.objects.all().order_by('?').first(),
    }

    return render(request, 'magic_sheet.html', context)

def randomAlbum(request):

    context = {
        'artist': RandAlbum.objects.all().order_by('?').first()
    }

    return render(request, 'random_album.html', context)

def ryan(request):
    
    context = {
        'album': Ryan.objects.all().order_by('?').first()
    }

    return render(request, 'random_ryan.html', context)

def randomArtist(request):

    context = {
        'artist': RandomArtist.objects.all().order_by('?').first()
    }

    return render(request, 'random_artist.html', context)

def randomPersonTop(request):
    
        context = {
            'album': RandPerson.objects.all().order_by('?').first()
        }
    
        return render(request, 'random_person_top.html', context)

def greatScene(request):
    
        context = {
            'album': GreatScene.objects.all().order_by('?').first()
        }
    
        return render(request, 'great_scene.html', context)

def jazz(request):
    
        context = {
            'album': Jazz.objects.all().order_by('?').first()
        }
    
        return render(request, 'jazz.html', context)

def login(request):
    
    return render(request, 'login.html')

def listeningLog(request):

    context = {
        'albums': Log.objects.all().order_by('-created_at')
    }

    return render(request, 'listening_log.html', context)

def addListeningLog(request):
    
    return render(request, 'add_listening_log.html')

def addToLog(request):

    Log.objects.create(album=request.POST['album'], artist=request.POST['artist'], image=request.POST['image'], rating=request.POST['rating'])

    return redirect('/listening-log')