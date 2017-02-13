import datetime
from random import randint

class DummyDurationGetter():
    def get_duration(self, origin = "Brooklyn", destination = "Queens", departure_time = datetime.datetime.now()):
        return randint(100, 1000)