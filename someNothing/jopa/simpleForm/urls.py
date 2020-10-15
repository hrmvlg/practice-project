from django.conf import settings
from django.conf.urls.static import static
from django.urls import path, re_path
from django.views.static import serve

from . import views

urlpatterns = [
    path('AddTrack/', views.AddTrack),
    path('AddArtist/', views.AddArtist),
    path('AddAlbum/', views.AddAlbum),
    path('', views.index),
]

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
