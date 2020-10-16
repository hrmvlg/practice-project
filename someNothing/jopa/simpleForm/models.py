from django.db import models


class Artist(models.Model):
    artists_name = models.CharField(max_length=255)

    def __str__(self):
        return "%s" % self.artists_name


class Album(models.Model):
    artists = models.ForeignKey(Artist, on_delete=models.CASCADE)
    name_of_album = models.CharField(max_length=255)
    cover = models.ImageField(upload_to='images/')
    release_date = models.DateField()

    def __str__(self):
        return "%s" % self.name_of_album


class MusicTrack(models.Model):
    songs_title = models.CharField(max_length=255)
    album = models.ForeignKey(Album, on_delete=models.CASCADE)
    # artist = models.ForeignKey(Artist, on_delete=models.CASCADE, default=0)
    track = models.FileField(upload_to='tracks/', blank=True)

    def __str__(self):
        return "%s" % self.songs_title
