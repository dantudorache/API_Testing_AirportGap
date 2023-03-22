import requests


def patch_airports_id(fav_id="", note="", token=""):
    header_params = {'Authorization': token}
    return requests.patch(f"https://airportgap.dev-tester.com/api/favorites/{fav_id}?note={note}", headers=header_params)

