import json

from django.http import HttpResponse
from django.shortcuts import get_object_or_404, reverse, render

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
            'detailsUrl': reverse('show_place', kwargs={'place_id': db_entry.id}),
        },
    }
    return geo_object


def show_index(request):
    features = [get_geo_object(place) for place in Place.objects.all()]
    geo_spots = {
        'type': 'FeatureCollection',
        'features': features,
    }
    context = {'geo_spots': geo_spots}
    return render(request, 'index.html', context=context)


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
