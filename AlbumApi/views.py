from django.shortcuts import render

# Rest frame Work
from rest_framework import viewsets
from rest_framework.decorators import api_view
from rest_framework.response import Response
from .serializers import AlbumSerializer, PhotoSerializer, AlbumPhotoSerializer


from .models import Album, AlbumPhoto, Photo


class AlbumPhotoViewSet(viewsets.ModelViewSet):
    """
    AlbumPhoto Viewset
    """
    queryset = AlbumPhoto.objects.all()
    serializer_class = AlbumPhotoSerializer
