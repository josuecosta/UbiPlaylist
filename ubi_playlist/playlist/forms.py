from django.contrib.auth.models import User
from .models import Music, Playlist
from django import forms


class UserForm(forms.ModelForm):

    class Meta:
        model = User
        fields = ['username', 'email']


class PlaylistForm(forms.ModelForm):

    class Meta:
        model = Playlist
        fields = ['user', 'music']


class MusicForm(forms.ModelForm):

    class Meta:
        model = Music
        fields = ['title', 'artist', 'album']
