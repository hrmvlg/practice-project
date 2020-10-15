from django.http import HttpResponseRedirect, HttpResponse
from django.shortcuts import render, redirect, get_object_or_404

from .forms import ArtistForm, AlbumForm, TrackForm
from .models import Artist, Album, MusicTrack


def index(request):
    formArtist = ArtistForm()
    formAlbum = AlbumForm()
    formTrack = TrackForm()

    artist = Artist.objects.all()
    album = Album.objects.all()
    music_track = MusicTrack.objects.all()

    context = {'artist': artist,
               'album': album,
               'music_track': music_track,
               'formArtist': formArtist,
               'formAlbum': formAlbum,
               'formTrack': formTrack}
    return render(request, 'AllAboutMusic.html', context)


def AddArtist(request):
    if request.method == 'POST' and 'bntAddArtist' in request.POST:
        formArtist = ArtistForm(request.POST)
        if formArtist.is_valid():
            new_artist = Artist()
            new_artist.artists_name = request.POST.get('artists_name')
            new_artist.save()
    return HttpResponseRedirect("/")


def AddAlbum(request):
    formAlbum = AlbumForm
    if request.method == 'POST':
        formAlbum = formAlbum(request.POST, request.FILES)
        if formAlbum.is_valid():
            formAlbum.save()
    return HttpResponseRedirect("/")


def AddTrack(request):
    formTrack = TrackForm
    if request.method == 'POST':
        formTrack = formTrack(request.POST, request.FILES)
        if formTrack.is_valid():
            formTrack.save()
    return HttpResponseRedirect("/")
