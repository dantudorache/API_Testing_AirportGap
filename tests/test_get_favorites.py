from requests_folder.get_favorites import get_favorites


class TestGetFavorites:
    def test_get_favorites(self):
        response = get_favorites('Token W5oe8joA6Fze2hJJcSp3fxGt')
        assert response.status_code == 200, f'Error: status code is not correct. Expected: 200, Actual: {response.status_code}'


