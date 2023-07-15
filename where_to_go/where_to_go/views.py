import json

from django.http import HttpResponse
from django.template import loader
from django.shortcuts import get_object_or_404, reverse

from places.models import Place


def get_geo_object(db_entry):
    geo_object = {
        'type': 'Feature',
        'geometry': {
            'type': 'Point',
            'coordinates': [db_entry.longitude, db_entry.latitude],
        },
        'properties': {
            'title': db_entry.title,
            'placeId': 'roofs24',
            'detailsUrl': reverse('show_place', kwargs={'place_id': db_entry.id}),
        },
    }
    return geo_object


def get_geo_json():
    features = [get_geo_object(place) for place in Place.objects.all()]
    geo_json = {
        'type': 'FeatureCollection',
        'features': features,
    }
    return geo_json


def show_index(request):
    template = loader.get_template('index.html')
    geo_json = get_geo_json()
    context = {'geo_json': geo_json}
    rendered_page = template.render(context, request)
    return HttpResponse(rendered_page)


def show_place(request, place_id):
    place = get_object_or_404(Place, id=place_id)
    images = [image.image.url for image in place.images.all()]
    response = {
        'title': place.title,
        'imgs': images,
        'description_short': place.description_short,
        'description_long': place.description_long,
        'coordinates': {
            'lat': place.latitude,
            'lng': place.longitude,
        },
    }
    return HttpResponse(
        json.dumps(response, ensure_ascii=False, indent=2),
        content_type='application/json',
    )
