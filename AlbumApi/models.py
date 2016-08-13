from __future__ import unicode_literals

from django.db import models


class Album(models.Model):
    """
    Model for Album
    """
    album_id = models.AutoField(primary_key=True)
    album_title = models.CharField(max_length=100)
    is_Active = models.BooleanField()

    def __unicode__(self):
        return self.album_title


class Photo(models.Model):
    """
    Model for Photo
    """
    photo_id = models.AutoField(primary_key=True)
    photo_name = models.CharField(max_length=100)

    def __unicode__(self):
        return self.photo_name


class AlbumPhoto(models.Model):
    """
    Model for AlbumPhoto
    """
    album_id = models.ForeignKey(Album, related_name='albums')
    photo_id = models.ForeignKey(Photo, related_name='photos')
