from django.contrib import admin
from django.utils.safestring import mark_safe

from .models import Artist
from .models import Album
from .models import MusicTrack


class AlbumAdmin(admin.ModelAdmin):
    list_display = ('artists', 'name_of_album', 'preview', 'cover', 'release_date',)
    fields = ['artists', 'name_of_album', 'cover', 'release_date']

    def preview(self, obj):
        return mark_safe(f'<img src="{obj.cover.url}" width="100" height="100">')


class MusicTrackAdmin(admin.ModelAdmin):
    list_display = ('songs_title', 'album', 'track')


admin.site.register(Artist)
admin.site.register(Album, AlbumAdmin)
admin.site.register(MusicTrack, MusicTrackAdmin)
