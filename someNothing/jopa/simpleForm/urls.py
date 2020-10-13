from django.urls import path
from . import views

urlpatterns = (
    path('AddTrack/', views.AddTrack),
    path('AddArtist/', views.AddArtist),
    path('AddAlbum/', views.AddAlbum),
    path('', views.AllAboutMusic),
)