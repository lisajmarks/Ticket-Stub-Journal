import requests

key = "AIzaSyCu-Ly-18p0peGx74ep4mBP1ExdN2kcZ9Y"
url = "https://maps.googleapis.com/maps/api/geocode/json"

def get_coordinates(address):
    resp = requests.get(url, params={"address":address, "key": key}).json()
    return (resp["results"][0]["geometry"]["location"])

