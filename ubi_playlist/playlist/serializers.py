from rest_framework import serializers
from .models import Music, Playlist
from django.contrib.auth.models import User


# Class Music
class MusicSerializer(serializers.ModelSerializer):

    class Meta:
        model = Music
        fields = '__all__'  # send back all fields


# Class Playlist
class PlaylistSerializer(serializers.ModelSerializer):

    class Meta:
        model = Playlist
        fields = ('user', 'music')  # send back specific fields


# Class User
class UserSerializer(serializers.ModelSerializer):

    class Meta:
        model = User
        fields = ('id', 'username', 'email')

