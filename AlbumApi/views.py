from rest_framework import viewsets
from .serializers import AlbumPhotoSerializer


from .models import AlbumPhoto


class AlbumPhotoViewSet(viewsets.ModelViewSet):
    """
    AlbumPhoto Viewset
    """
    queryset = AlbumPhoto.objects.all()
    serializer_class = AlbumPhotoSerializer
