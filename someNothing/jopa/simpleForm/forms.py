from django.forms import ModelForm, DateInput, Form

from .models import MusicTrack, Album, Artist


class ArtistForm(ModelForm):
    class Meta:
        model = Artist
        fields = '__all__'
        labels = {
            'artists_name': 'Введите исполнителя',
        }


class AlbumForm(ModelForm):
    class Meta:
        model = Album
        fields = '__all__'
        widgets = {
            'release_date': DateInput(attrs={'type': 'date'}),
        }
        labels = {
            'artists': 'Выберите исполнителя',
            'name_of_album': 'Введите название альбома',
            'cover': 'Загрузите обложку',
            'release_date': 'Дата релиза',
        }


class TrackForm(ModelForm):
    class Meta:
        model = MusicTrack
        fields = '__all__'
        labels = {
            'songs_title': 'Название трека',
            'album': 'Выберите альбом',
            'track': 'Загрузите аудиодорожку',
        }


class GenerateForm(ModelForm):
    class Meta:
        model = MusicTrack
        fields = ("album", )
        labels = {
            'album': 'Выберите альбом'
        }
