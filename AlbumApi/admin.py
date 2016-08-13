from django.contrib import admin


from .models import Album, AlbumPhoto, Photo


class AlbumAdmin(admin.ModelAdmin):
    search_fields = ["album_title"]
    list_display = ["album_id", "album_title", "is_Active"]


class PhotoAdmin(admin.ModelAdmin):
    search_fields = ["photo_name"]
    list_display = ["photo_id", "photo_name"]


class AlbumPhotoAdmin(admin.ModelAdmin):
    list_display = ["photo_id", "album_id"]


admin.site.register(Album, AlbumAdmin)
admin.site.register(Photo, PhotoAdmin)
admin.site.register(AlbumPhoto, AlbumPhotoAdmin)