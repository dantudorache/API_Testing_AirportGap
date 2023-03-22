from requests_folder.post_airports_distance import post_airports_distance



class TestPostAirportsDistance:
    def test_post_airports_distance(self):
        response = post_airports_distance("KIX", "NRT")
        assert response.status_code == 200, f'Error: status code is not correct. Expected: 200, Actual: {response.status_code}'



