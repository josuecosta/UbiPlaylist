from rest_framework import generics
from django.contrib.auth.models import User
from . models import Music, Playlist
from . serializers import MusicSerializer, PlaylistSerializer, UserSerializer


# Music
class MusicList(generics.ListCreateAPIView):
    queryset = Music.objects.all()
    serializer_class = MusicSerializer


class MusicDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Music.objects.all()
    serializer_class = MusicSerializer


# User
class UserList(generics.ListCreateAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer


class UserDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer


# Playlist
class Playlist(generics.RetrieveUpdateDestroyAPIView):
    queryset = Playlist.objects.all()
    serializer_class = PlaylistSerializer


from django.views import generic


class IndexView(generic.ListView):
    template_name = 'index.html'

    def get_queryset(self):
        return Music.objects.all()


