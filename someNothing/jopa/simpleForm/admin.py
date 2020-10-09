from django.contrib import admin
from .models import Artist
from  .models import Album
from  .models import MusicTrack


class AlbumAdmin(admin.ModelAdmin):
    list_display = ('artists', 'name_of_album', 'cover', 'release_date')


class MusicTrackAdmin(admin.ModelAdmin):
    list_display = ('songs_title', 'album', 'track')


admin.site.register(Artist)
admin.site.register(Album, AlbumAdmin)
admin.site.register(MusicTrack, MusicTrackAdmin)