from rest_framework import serializers


from .models import Album, AlbumPhoto, Photo


class AlbumSerializer(serializers.ModelSerializer):
    """
    Album Serializer
    """
    class Meta:
        model = Album
        fields = ('album_id', 'album_title', 'is_Active')


class PhotoSerializer(serializers.ModelSerializer):
    """
    Album Serializer
    """
    class Meta:
        model = Photo
        fields = ('photo_id', 'photo_name')


class AlbumPhotoSerializer(serializers.ModelSerializer):
    """
    Album Serializer
    """
    album_id = AlbumSerializer()
    photo_id = PhotoSerializer()

    class Meta:
        model = AlbumPhoto
        fields = ('id', 'album_id', 'photo_id')

    def create(self, validated_data):
        """
        This need to be overridden because serializers doesn't update nested data during creation of new obj
        :param validated_data:
        :return:
        """
        album_data = validated_data.pop('album_id')
        photo_data = validated_data.pop('photo_id')
        album_ins = Album.objects.create(**album_data)
        photo_ins = Photo.objects.create(**photo_data)
        data = {'album_id_id': album_ins.album_id, 'photo_id_id': photo_ins.photo_id}
        album_photo = AlbumPhoto.objects.create(**data)
        return album_photo

    def update(self, instance, validated_data):
        """
        This need to be overridden because serializers doesn't update nested data
        :param instance:
        :param validated_data:
        :return:
        """
        photo_data = validated_data.pop('photo_id')
        album_data = validated_data.pop('album_id')
        photo_instance = instance.photo_id
        album_instance = instance.album_id
        # update the photo instance
        photo_instance.photo_name = photo_data['photo_name']
        photo_instance.save()
        # update album instance
        album_instance.album_title = album_data['album_title']
        album_instance.is_Active = album_data['is_Active']
        album_instance.save()
        # save the albumphoto instance
        instance.save()
        return instance
