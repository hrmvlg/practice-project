from django.http import HttpResponseRedirect
from django.shortcuts import render

from .forms import ArtistForm, AlbumForm, TrackForm
from .models import Artist, Album, MusicTrack


def AllAboutMusic(request):
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
    if request.method == 'POST' and 'bntAddAlbum' in request.POST:
        fromAlbum = AlbumForm(request.POST)
        if fromAlbum.is_valid():
            new_album = Album()
            new_album.name_of_album = request.POST.get('name_of_album')
            new_album.artists = request.POST.get('artists')
            new_album.cover = request.POST.get('cover')
            new_album.release_date = request.POST.get('release_date')
            new_album.save()
    return HttpResponseRedirect('/')


def AddTrack(request):
    if request.method == 'POST' and 'btnAddTrack' in request.POST:
        formTrack = TrackForm(request.POST)
        if formTrack.is_valid():
            formTrack.save()
    return HttpResponseRedirect('/')
