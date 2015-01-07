import unittest
from changeless.types import FancyHash
from datetime import datetime
import tests.factory as factory

class DBTests(unittest.TestCase):
    def test_compute_corrected_times(self):
        #race = factory.race()
        race = FancyHash({
            "name": "test_name",
            "start_time": datetime.now(),
            'length': 3,
            "course": "D3",
            "owner":{"name":"GYRC"},
            "race_result_set":[]})

        results = db.correct_times(race)
        #TODO: make assertions
