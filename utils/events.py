import requests
import maps

api_key = ''

# Find events - Returns array of nearby events containing information
def find_events(lat, long, radius):
    events = []
    url = 'https://api.meetup.com/2/open_events?&sign=true&photo-host=public&lat=' + str(lat) + '&lon=' + str(long) + '&radius=' + str(radius) + '&page=20&key=' + api_key
    r = requests.get(url)
    data = r.json()
    for event in data['results']:
        if event.get('venue'):
            new_event = []
            new_event.append(event['name'])
            new_event.append(event['time'])
            new_event.append(event['description'])
            lat = event['venue']['lat']
            lon = event['venue']['lon']
            new_event.append(lat)
            new_event.append(lon)
            new_event.append(maps.convert_latlon(lat, lon))
            events.append(new_event)
        
    return events

# Get event info - Returns array of event info
