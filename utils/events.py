import requests
import maps

api_key = ''

# Find events - Returns array of nearby events containing information
def find_events(lat, lon, radius):
    events = []
    url = 'https://api.meetup.com/2/open_events?&sign=true&photo-host=public&lat=' + str(lat) + '&lon=' + str(lon) + '&radius=' + str(radius) + '&page=20&key=' + api_key
    r = requests.get(url)
    data = r.json()
    for event in data['results']:
        if event.get('venue'):
            new_event = []
            new_event.append(event['name']) # [0]
            new_event.append(event['time']) # [1]
            new_event.append(event['description']) # [2]
            lat = event['venue']['lat'] 
            lon = event['venue']['lon']
            new_event.append(lat) # [3]
            new_event.append(lon) # [4]
            address = maps.convert_latlon(lat, lon)
            new_event.append(address) # [5]
            events.append(new_event)
        
    return events
