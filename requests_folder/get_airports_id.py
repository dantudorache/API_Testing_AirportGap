import requests


def get_airports_id(id):
    return requests.get(f'https://airportgap.dev-tester.com/api/airports/{id}')





