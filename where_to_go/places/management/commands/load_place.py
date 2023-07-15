from urllib.parse import urlparse, unquote
import os

from django.core.files.base import ContentFile
from django.core.management.base import BaseCommand
import requests

from places.models import Place, Image


def remove_places_images(queryset):
    for image in queryset:
        os.remove(image.image.file.name)
        image.delete()


class Command(BaseCommand):
    def handle(self, *args, **options):
        response = requests.get(args[0]).json()
        place, created = Place.objects.get_or_create(
            title=response['title'],
            defaults={
                'description_short': response['description_short'],
                'description_long': response['description_long'],
                'latitude': response['coordinates']['lat'],
                'longitude': response['coordinates']['lng'],
            },
        )
        if not created:
            remove_places_images(place.images.all())
        for count, img in enumerate(response['imgs']):
            filename = os.path.basename(unquote(urlparse(img).path))
            image_response = requests.get(img)
            img_model = Image()
            img_model.image.save(
                filename, ContentFile(image_response.content), save=False
            )
            img_model.place = place
            img_model.order = count
            img_model.save()

    def add_arguments(self, parser):
        parser.add_argument(nargs='+', type=str, dest='args')
