from requests_folder.get_favorites_id import *
from requests_folder.post_favorites import post_favorites
from requests_folder.delete_favorites_clear_all import delete_favorites_clear_all

class TestGetFavoritesId:
    def test_get_favorites_id(self):
        token = 'Token W5oe8joA6Fze2hJJcSp3fxGt'
        favorite = post_favorites(token, "AEY")
        fav_id = favorite.json()['data']['id']
        response = get_favorites_id(fav_id=fav_id, token=token)
        assert response.status_code == 200, f'Error: status code is not correct. Expected: 200, Actual: {response.status_code}'
        assert len(response.json()) == 1, f'Expected: 6, actual: {len(response.json())}'
        delete_favorites_clear_all(token)