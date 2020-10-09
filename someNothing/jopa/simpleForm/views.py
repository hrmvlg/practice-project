from django.http import HttpResponseRedirect
from django.shortcuts import render

from .forms import ArtistForm, AlbumForm, TrackForm
from .models import Artist, Album, MusicTrack


def AllAboutMusic(request):
    formArtist = ArtistForm()
    formAlbum = AlbumForm()

    artist = Artist.objects.all()
    album = Album.objects.all()
    music_track = MusicTrack.objects.all()
    context = {'artist': artist, 'album': album, 'music_track': music_track, 'formArtist': formArtist,
               'formAlbum': formAlbum}
    return render(request, 'AllAboutMusic.html', context)


def AddArtist(request):
    formArtist = ArtistForm()
    context = {'formArtist': formArtist}
    return render(request, 'AllAboutMusic.html', context)


def AddAlbum(request):
    formAlbum = AlbumForm()
    context = {'formAlbum': formAlbum}
    return render(request, 'simpleForm/templates/AllAboutMusic.html', context)

# def AddNewArtist(request):
#    if request.method == 'POST' and 'btnform1' in request.POST:
#        form = AddArtistForm(request.POST)
#        if form.is_valid():
#            new_artist = Artist()
#            new_artist.artists_name = request.POST.get('artists_name')
#            new_artist.save()
#            return HttpResponseRedirect("/")
#        return render(request, 'AllAboutMusic.html', {'form': form})

# def AddAlbum(request):
#    new_album = Album()
#    new_album.name_of_album = request.POST.get('name_of_album')
#    new_album.artists = request.POST.get('artists')
#    new_album.cover = request.POST.get('cover')
#    new_album.release_date = request.POST.get('release_date')
#    return HttpResponseRedirect('/')
