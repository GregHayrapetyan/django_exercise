from rest_framework import serializers, fields
from app.models import Album, Author, Song

class AuthorsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Author
        fields = "__all__"

class AlbumsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Album
        fields = "__all__"

class SongsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Song
        fields = "__all__"