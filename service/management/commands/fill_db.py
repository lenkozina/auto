from django.core.management.base import BaseCommand

import json
import os

from service.models import Slider, Gallery, Service, ServiceCategory

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

        service_categories = load_from_json('service_category')

        ServiceCategory.objects.all().delete()
        [ServiceCategory.objects.create(**service_category) for service_category in service_categories]

        Service.objects.all().delete()
        services = load_from_json('service')

        for service in services:
            service_name = service['category']
            # Получаем категорию по имени
            _category = ServiceCategory.objects.get(title=service_name)
            # Заменяем название категории объектом
            service['category'] = _category
            Service.objects.create(**service)
