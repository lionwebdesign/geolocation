import requests

datos  = {
    "considerIp": "true"
}

api_key = "AIzaSyA-C2U9OWidR-wfrXZl5OEXbosiVVFOhC0"
url = (f"https://www.googleapis.com/geolocation/v1/geolocate?key={api_key}")
response = requests.post(url, json=datos)
location = response.json()["location"]
lat = location["lat"]
lng = location["lng"]
acuracy = response.json()["acuracy"]

print(lat)
print(lng)
print(acuracy)