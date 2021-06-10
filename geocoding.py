import requests

key = "AIzaSyDwx11RUEtpBZVo1XBAeSPaXIp9CN6S3AQ"
url = "https://maps.googleapis.com/maps/api/geocode/json"

def get_coordinates(address):
    resp = requests.get(url, params={"address":address, "key": key}).json()
    return (resp["results"][0]["geometry"]["location"])
