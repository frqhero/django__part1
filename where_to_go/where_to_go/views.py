from django.http import HttpResponse
from django.template import loader


def get_geo_json():
    geo_json = {
        'type': 'FeatureCollection',
        'features': [
            {
                'type': 'Feature',
                'geometry': {
                    'type': 'Point',
                    'coordinates': [37.62, 55.793676],
                },
                'properties': {
                    'title': '«Легенды Москвы',
                    'placeId': 'moscow_legends',
                    'detailsUrl': 'https://raw.githubusercontent.com/devmanorg/where-to-go-frontend/master/places/moscow_legends.json',
                },
            },
            {
                'type': 'Feature',
                'geometry': {
                    'type': 'Point',
                    'coordinates': [37.64, 55.753676],
                },
                'properties': {
                    'title': 'Крыши24.рф',
                    'placeId': 'roofs24',
                    'detailsUrl': 'https://raw.githubusercontent.com/devmanorg/where-to-go-frontend/master/places/roofs24.json',
                },
            },
        ],
    }
    return geo_json


def show_index(request):
    template = loader.get_template('index.html')
    geo_json = get_geo_json()
    context = {'geo_json': geo_json}
    rendered_page = template.render(context, request)
    return HttpResponse(rendered_page)
