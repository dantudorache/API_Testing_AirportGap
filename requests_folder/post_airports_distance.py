import requests


def post_airports_distance(from_id_1="", to_id_2=""):
    if from_id_1 == "" and to_id_2 == "":
        return requests.post('https://airportgap.dev-tester.com/api/airports/distance')
    elif from_id_1 != "" and to_id_2 == "":
        return requests.post(f"https://airportgap.dev-tester.com/api/airports/distance?from={from_id_1}")
    elif from_id_1 == "" and to_id_2 != "":
        return requests.post(f"https://airportgap.dev-tester.com/api/airports/distance?to={to_id_2}")
    else:
        return requests.post(f"https://airportgap.dev-tester.com/api/airports/distance?from={from_id_1}&to={to_id_2}")


