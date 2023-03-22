from requests_folder.delete_favorites_clear_all import delete_favorites_clear_all

class TestDeleteFavoriteCearAll:
    def test_delete_favorites_clear_all(self):
        token = 'Token W5oe8joA6Fze2hJJcSp3fxGt'
        response = delete_favorites_clear_all(token)
        assert response.status_code == 204, f'Error: status code is not correct. Expected: 204, Actual: {response.status_code}'