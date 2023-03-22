from requests_folder.delete_favorites_id import delete_favorites_id
from requests_folder.post_favorites import post_favorites

class TestDeleteFavoriteId:
    def test_delete_favorites_id(self):
        token = 'Token W5oe8joA6Fze2hJJcSp3fxGt'
        favorite = post_favorites(token, "AEY")
        fav_id = favorite.json()['data']['id']
        response = delete_favorites_id(token, fav_id)
        assert response.status_code == 204, f'Error: status code is not correct. Expected: 204, Actual: {response.status_code}'