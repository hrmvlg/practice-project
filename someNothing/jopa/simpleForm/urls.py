from django.conf import settings
from django.conf.urls.static import static
from django.conf.urls import url
from django.urls import path

from . import views

urlpatterns = [
    path('Upload/AddTrack/', views.AddTrack),
    path('Upload/AddArtist/', views.AddArtist),
    path('Upload/AddAlbum/', views.AddAlbum),
    path('Upload/', views.Upload, name='Upload'),
    path('Generate/', views.Generate, name='Generate'),
    path('', views.index, name='index'),
]

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
