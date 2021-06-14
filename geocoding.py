from secrets import G_MAPS_API_KEY
import requests

key = G_MAPS_API_KEY
url = "https://maps.googleapis.com/maps/api/geocode/json"

def get_coordinates(address):
    resp = requests.get(url, params={"address":address, "key": key}).json()
    return (resp["results"][0]["geometry"]["location"])

