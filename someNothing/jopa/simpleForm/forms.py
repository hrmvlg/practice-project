from django.forms import ModelForm, DateInput
from django import forms

from .models import MusicTrack, Album, Artist


class ArtistForm(ModelForm):
    class Meta:
        model = Artist
        fields = '__all__'


class AlbumForm(ModelForm):
    class Meta:
        model = Album
        fields = '__all__'
        widgets = {
            'release_date': DateInput(attrs={'type': 'date'})
        }


class TrackForm(ModelForm):
    class Meta:
        model = MusicTrack
        fields = '__all__'
