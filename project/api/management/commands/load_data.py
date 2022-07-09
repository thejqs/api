import json

from django.core.management.base import BaseCommand, CommandError
from project.api.models import Factory, Sprocket

class Command(BaseCommand):
    help = "Loads factory and sprocket data"
    # could we pass in the relevant filename on invocation? well sure. but what fun would that be
    factories_filepath = "data/seed_factory_data.json"
    sprockets_filepath = "data/seed_sprocket_types.json"

    
    def handle(self, *args, **kwargs):
        self._load_factories(self.factories_filepath)
        self._load_sprockets(self.sprockets_filepath)
        

    def _load_factories(self, filepath):
        with open(filepath) as sf:
            data = json.load(sf)
            for factory in data["factories"]:
                try:
                    f_created = Factory.objects.create(chart_data=factory["factory"]["chart_data"])
                    f_created.save()
                    self.stdout.write(self.style.SUCCESS("Successfully loaded factories data"))
                except Exception as e:
                    self.stdout.write(self.style.ERROR(f"Failed to create factories data: {e}"))

    def _load_sprockets(self, filepath):
        with open(filepath) as ss:
            data = json.load(ss)
            for sprocket in data["sprockets"]:
                try:
                    s_created = Sprocket.objects.create(
                        teeth=sprocket["teeth"],
                        pitch_diameter=sprocket["pitch_diameter"],
                        outside_diameter=sprocket["outside_diameter"],
                        pitch=sprocket["pitch"]
                    )
                    s_created.save()
                    self.stdout.write(self.style.SUCCESS("Successfully loaded sprockets data"))
                except Exception as e:
                    self.stdout.write(self.style.ERROR(f"Failed to create sprockets data: {e}"))
                