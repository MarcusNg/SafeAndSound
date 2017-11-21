import requests

api_key = 'APIKEY'

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
            new_event.append(event['venue']['lat'])
            new_event.append(event['venue']['lon'])
            events.append(new_event)
        
    return events

