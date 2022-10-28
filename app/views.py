from rest_framework import generics
from rest_framework.response import Response
from app.models import Album, Author, Song
from app.serializers import AuthorsSerializer, AlbumsSerializer, SongsSerializer
from rest_framework import status

class AuthorsView(generics.GenericAPIView):
    serializer_class = AuthorsSerializer
    def get(self, request):
        authors = [author.name for author in Author.objects.all()]
        return Response(authors)

    def post(self, request):
        serializer = self.serializer_class(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class AlbumsView(generics.GenericAPIView):
    serializer_class = AlbumsSerializer
    def get(self, request):
        albums = [album.name for album in Album.objects.all()]
        return Response(albums)

    def post(self, request):
        serializer = self.serializer_class(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
class SongView(generics.GenericAPIView):
    serializer_class = SongsSerializer
    def get(self, request):
        songs = [song.name for song in Song.objects.all()]
        return Response(songs)

    def post(self, request):
        serializer = self.serializer_class(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)