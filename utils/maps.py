import requests

api_key = 'API_KEY'

# Get latitude and longitude of address - Returns array [lat,lon]
def convert_address(address):
    query = address.replace(' ', '%20')
    url = 'https://maps.googleapis.com/maps/api/geocode/json?&address=' + query
    r = requests.get(url)
    data = r.json()
    if data['status'] == 'OK':
        location = data['results'][0]['geometry']['location']
        lat = location['lat']
        lon = location['lng']
        return [lat,lon]

def convert_latlon(lat, lon):
    url = 'https://maps.googleapis.com/maps/api/geocode/json?latlng=' + str(lat) + ',' + str(lon) + '&key=' + api_key
    r = requests.get(url)
    data = r.json()
    if data['status'] == 'OK':
        address = data['results'][0]['formatted_address']
        return address
    



