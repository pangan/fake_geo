import random

from decimal import Decimal


class FakeGeo:
    def __init__(self, center={'lat':0,'lan':0}, radius=0):
        self.center = center
        self.radius = radius

    def get(self):
        center_lat = float(self.center['lat'])
        center_lan = float(self.center['lan'])
        radius = float(self.radius)

        geo = random.uniform(self.center['lat'] - radius, self.center['lat'] + radius)
        lat = Decimal(str(geo)).quantize(Decimal('.000001'))

        geo = random.uniform(self.center['lan'] - radius, self.center['lan'] + radius)
        lan = Decimal(str(geo)).quantize(Decimal('.000001'))
        return lat, lan
