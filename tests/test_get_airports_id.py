from requests_folder.get_airports_id import get_airports_id



class TestAirportsId:
    def test_get_airports_id(self):
        response = get_airports_id('KIX')
        assert response.status_code == 200, f'Error: status code is not correct. Expected: 200, Actual: {response.status_code}'
