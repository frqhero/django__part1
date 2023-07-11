import json

from django.http import HttpResponse, JsonResponse
from django.template import loader
from django.shortcuts import get_object_or_404, reverse

from places.models import Place


def get_moscow_legends_object():
    moscow_legends = Place.objects.get(title__contains='Легенды')
    moscow_legends_object = {
        'type': 'Feature',
        'geometry': {
            'type': 'Point',
            'coordinates': [moscow_legends.longitude, moscow_legends.latitude],
        },
        'properties': {
            'title': moscow_legends.title,
            'placeId': 'moscow_legends',
            'detailsUrl': reverse('show_place', kwargs={'place_id': moscow_legends.id}),
        },
    }
    address = reverse('show_place', kwargs={'place_id': 1})
    return moscow_legends_object


def get_roofs_object():
    roofs = Place.objects.get(title__contains='Крыши')
    roofs_object = {
        'type': 'Feature',
        'geometry': {
            'type': 'Point',
            'coordinates': [roofs.longitude, roofs.latitude],
        },
        'properties': {
            'title': roofs.title,
            'placeId': 'roofs24',
            'detailsUrl': reverse('show_place', kwargs={'place_id': roofs.id}),
        },
    }
    return roofs_object


def get_geo_json():
    moscow_legends_object = get_moscow_legends_object()
    roofs_object = get_roofs_object()
    geo_json = {
        'type': 'FeatureCollection',
        'features': [moscow_legends_object, roofs_object],
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
