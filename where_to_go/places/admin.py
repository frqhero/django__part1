from adminsortable2.admin import SortableTabularInline, SortableAdminBase
from django.contrib import admin
from django.utils.html import format_html

from .models import Place, Image


class ImageTabularInline(SortableTabularInline):
    model = Image
    readonly_fields = ['get_image']

    def get_image(self, obj):
        max_height = 200
        return format_html(
            '<img src="{}" style="max-height:{}px" />',
            obj.image.url,
            max_height
        )


@admin.register(Place)
class PlaceAdmin(SortableAdminBase, admin.ModelAdmin):
    inlines = [ImageTabularInline]


@admin.register(Image)
class ImageAdmin(admin.ModelAdmin):
    pass
