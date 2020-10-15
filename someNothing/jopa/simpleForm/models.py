from django.db import models
from django.utils.safestring import mark_safe


class Artist(models.Model):
    artists_name = models.CharField(max_length=255)

    # выводить альбомы и исполнителей автоматом ??

    def __str__(self):
        return "%s" % self.artists_name


class Album(models.Model):
    artists = models.ForeignKey(Artist, on_delete=models.CASCADE)
    name_of_album = models.CharField(max_length=255)
    cover = models.ImageField(upload_to='images/')
    release_date = models.DateField()

    def __str__(self):
        return "%s" % self.name_of_album

    @property
    def cover_url(self):
        if self.cover and hasattr(self.cover, 'url'):
            return self.cover.url


class MusicTrack(models.Model):
    songs_title = models.CharField(max_length=255)
    album = models.ForeignKey(Album, on_delete=models.CASCADE)
    # artist = models.ForeignKey(Artist, on_delete=models.CASCADE, default=0)
    track = models.FileField(upload_to='tracks/')

    def __str__(self):
        # разобраться с выводом исполнителей
        return "%s" % self.songs_title
