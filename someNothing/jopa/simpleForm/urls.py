from django.urls import path
from . import views

urlpatterns = (
    path('', views.AllAboutMusic),
    path('AddArtist/', views.AddArtist),
    path('AddAlbum/', views.AddAlbum),
    path('AddTrack/', views.AddTrack),
)