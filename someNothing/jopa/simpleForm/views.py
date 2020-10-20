from django.http import HttpResponseRedirect, HttpResponse
from django.shortcuts import render, redirect, get_object_or_404

from .forms import ArtistForm, AlbumForm, TrackForm, GenerateForm
from .models import Artist, Album, MusicTrack


def index(request):
    return render(request, 'Home.html')


def AddArtist(request):
    if request.method == 'POST' and 'bntAddArtist' in request.POST:
        formArtist = ArtistForm(request.POST)
        if formArtist.is_valid():
            new_artist = Artist()
            new_artist.artists_name = request.POST.get('artists_name')
            new_artist.save()
    return HttpResponseRedirect("/Upload")


def AddAlbum(request):
    formAlbum = AlbumForm
    if request.method == 'POST':
        formAlbum = formAlbum(request.POST, request.FILES)
        if formAlbum.is_valid():
            formAlbum.save()
    return HttpResponseRedirect("/Upload")


def AddTrack(request):
    formTrack = TrackForm
    if request.method == 'POST':
        formTrack = formTrack(request.POST, request.FILES)
        if formTrack.is_valid():
            formTrack.save()
    return HttpResponseRedirect("/Upload")


def Upload(request):
    formArtist = ArtistForm()
    artist = Artist.objects.all()
    formAlbum = AlbumForm()
    album = Album.objects.all()
    formTrack = TrackForm()
    music_track = MusicTrack.objects.all()
    context = {'artist': artist, 'formArtist': formArtist,
               'album': album, 'formAlbum': formAlbum,
               'music_track': music_track, 'formTrack': formTrack}

    return render(request, 'Upload.html', context)


def Generate(request):
    formGenerate = GenerateForm()
    album = Album.objects.all()
    context = {'album': album, 'formGenerate': formGenerate}
    return render(request, 'Generate.html', context)
