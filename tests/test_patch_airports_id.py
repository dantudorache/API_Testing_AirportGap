from requests_folder.patch_airports_id import patch_airports_id
from requests_folder.post_favorites import post_favorites
from requests_folder.delete_favorites_clear_all import delete_favorites_clear_all


class TestPatchFavorites:
    def test_patch_airports_id(self):
        note = "My usual layover when visiting family, although it's really far away..."
        token = "Token W5oe8joA6Fze2hJJcSp3fxGt"

        favorite = post_favorites(token, "AEY")
        fav_id = favorite.json()['data']['id']

        response = patch_airports_id(note=note, token=token, fav_id=fav_id)
        assert response.status_code == 200, f'Error: status code is not correct. Expected: 200, Actual: {response.status_code}'
        delete_favorites_clear_all(token)