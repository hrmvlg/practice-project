from django.forms import ModelForm

from .models import MusicTrack, Album, Artist


class ArtistForm(ModelForm):
    class Meta:
        model = Artist
        fields = '__all__'


class AlbumForm(ModelForm):
    class Meta:
        model = Album
        fields = '__all__'


class TrackForm(ModelForm):
    class Meta:
        model = MusicTrack
        fields = '__all__'

# class AddAlbumForm(forms.Form):
#    artists = forms.ModelChoiceField(queryset=Artist.objects.all())
#    name_of_album = forms.CharField(max_length=255)
#    cover = forms.ImageField()
#    release_date = forms.DateField()
#
#
# class AddTrackForm(forms.Form):
#    songs_title = forms.CharField(max_length=255)
#    album = forms.ModelChoiceField(queryset=Album.objects.all())
#    track = forms.FileField()
