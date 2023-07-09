import unittest
from unittest import mock
from pokemon_lookup import find


class MockResponse:
        def __init__(self, json_data, text, status_code) -> None:
            self.status_code = status_code
            self.text = text
            self.json_data = json_data

        def json(self):
            return self.json_data

def mocked_requst_good(*args, **kwargs):
    return MockResponse({"species": { "name": "test_pokemon"}}, "test", 200)

def mocked_requst_bad(*args, **kwargs):
    return MockResponse({"species": { "name": ""}}, "Unknown ID", 401)

class FindTestCases(unittest.TestCase):

    @mock.patch('pokemon_lookup.find.requests.get', side_effect=mocked_requst_good)
    def test_get_name_positivie(self, mock_get):
        name = find.name(1)
        assert name == "test_pokemon"

    @mock.patch('pokemon_lookup.find.requests.get', side_effect=mocked_requst_bad)
    def test_get_name_negative(self, mock_get):
        try:
            name = find.name(1)
            self.assertFalse("Did not throw exception as expected")
        except:
            self.assertTrue("Threw Exception")


