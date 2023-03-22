from requests_folder.get_airports import get_airports


class TestAirports:
    def test_get_airports(self):
        response = get_airports()
        assert response.status_code == 200, f'Error: status code is not correct. Expected: 200, Actual: {response.status_code}'








