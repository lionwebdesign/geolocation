import requests

class GEOLOCATION():
    def __init__(self):
        self.data  = {
            "considerIp": "true"
        }
        self.api_key = "API_GOOGLE"
        self.url = (f"https://www.googleapis.com/geolocation/v1/geolocate?key={self.api_key}")
        
    def get_location(self):
        response = requests.post(self.url, json=self.data)
        location = response.json()["location"]
        lat = location["lat"]
        lng = location["lng"]
        position = [lat, lng]
        return position
        
if(__name__ == "__main__"):
    geo = GEOLOCATION()
    print(geo.get_location())
