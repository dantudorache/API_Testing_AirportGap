from requests_folder.post_favorites import post_favorites

class TestPostfavorites:
    def test_post_favorites(self):
        airport_id = "EGS"
        note = "note1"
        response = post_favorites('Token W5oe8joA6Fze2hJJcSp3fxGt', airport_id=airport_id, note=note)
        assert response.status_code == 201, f'Error: status code is not correct. Expected: 201, Actual: {response.status_code}'