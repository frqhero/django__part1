from django.core.management.base import BaseCommand

from .loading_place import load_place


class Command(BaseCommand):
    def handle(self, *args, **options):
        load_place(args[0])

    def add_arguments(self, parser):
        parser.add_argument(nargs='+', type=str, dest='args')
