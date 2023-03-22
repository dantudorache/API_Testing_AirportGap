import requests


def delete_favorites_id(token="", fav_id=""):
    header_params = {'Authorization': token}
    return requests.delete(f"https://airportgap.dev-tester.com/api/favorites/{fav_id}", headers=header_params)
