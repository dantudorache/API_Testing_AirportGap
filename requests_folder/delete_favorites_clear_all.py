import requests


def delete_favorites_clear_all(token=""):
    header_params = {'Authorization': token}
    return requests.delete(f"https://airportgap.dev-tester.com/api/favorites/clear_all", headers=header_params)
