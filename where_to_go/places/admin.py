from django.contrib import admin
from django.utils.html import format_html

from .models import Place, Image


class ImageInline(admin.TabularInline):
    model = Image
    readonly_fields = ['get_image']

    def get_image(self, obj):
        url = obj.image.url
        max_height = 200
        ratio = obj.image.height / max_height
        width = round(obj.image.width / ratio)
        height = round(obj.image.height / ratio)
        return format_html(
            f'<img src="{url}" width="{width}" height={height} />'
        )


@admin.register(Place)
class PlaceAdmin(admin.ModelAdmin):
    inlines = [ImageInline]


@admin.register(Image)
class ImageAdmin(admin.ModelAdmin):
    pass
