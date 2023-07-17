import os

from django.conf import settings
from django.core.management.base import BaseCommand

from .load_place import Command as LoadPlaceCommand


class Command(BaseCommand):
    def handle(self, *args, **options):
        static_folder = 0
        static_dir = settings.STATICFILES_DIRS[static_folder]
        with open(f'{static_dir}/places.txt', 'r') as file:
            links = [place.strip() for place in file.readlines()]
        [LoadPlaceCommand.handle('_', link) for link in links]