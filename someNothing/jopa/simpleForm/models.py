from django.db import models


class Artist(models.Model):
    artists_name = models.CharField(max_length=255)

    # выводить альбомы и исполнителей автоматом

    def __str__(self):
        return "%s" % self.artists_name

    pass


class Album(models.Model):
    #artists = models.ManyToManyField(Artist)
    artists = models.ForeignKey(Artist, on_delete=models.CASCADE, default=0)
    name_of_album = models.CharField(max_length=255)
    cover = models.ImageField(upload_to='images/')
    release_date = models.DateField()

    # разобраться с длиной песен, отображением треков

    def __str__(self):
        return "%s" % self.name_of_album

    pass


class MusicTrack(models.Model):
    songs_title = models.CharField(max_length=255)
    album = models.ForeignKey(Album, on_delete=models.CASCADE)
    track = models.FileField(upload_to='tracks/')
    # Добавление аудиодорожки

    def __str__(self):
        # разобраться с выводом исполнителей
        return "%s" % self.songs_title

    pass
