from urllib.parse import urlparse, unquote
import os

from django.core.files.base import ContentFile
import requests

from places.models import Place, Image


def remove_places_images(queryset):
    for image in queryset:
        os.remove(image.image.file.name)
        image.delete()


def load_place(url):
    response = requests.get(url)
    response.raise_for_status()
    response = response.json()
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
