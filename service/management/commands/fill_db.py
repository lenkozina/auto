from django.core.management.base import BaseCommand

import json
import os

from service.models import Slider, Gallery, Service

JSON_PATH = 'service/json'

def load_from_json(file_name):
    with open(os.path.join(JSON_PATH, file_name + '.json'), 'r', encoding='utf-8') as infile:
        return json.load(infile)

class Command(BaseCommand):
    def handle(self, *args, **options):
        sliders = load_from_json('slider')

        Slider.objects.all().delete()
        [Slider.objects.create(**slider) for slider in sliders]

        galleries = load_from_json('gallery')
        
        Gallery.objects.all().delete()
        [Gallery.objects.create(**gallery) for gallery in galleries]

        services = load_from_json('service')

        Service.objects.all().delete()
        [Service.objects.create(**service) for service in services]
