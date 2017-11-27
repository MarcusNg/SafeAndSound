# Event Finder
## Team SafeAndSound
Event Finder is a web application that allows you to find upcoming events and meetups in a certain raidus of a specified location. After inputting your desired address and radius (miles), click the 'Find Events' button. Your Location appears as a red marker and events show up as green markers. When clicking on an event, you have the option to click the 'More Info' button, which brings you to a new page with more information about the selected event and shows you other events in a 2 miles raidus of the selected event.

## API Keys
Event Finder relies on the Google Maps API and Meetup.com API.
### Google Maps API Key
1. Go to [Google Maps API](https://developers.google.com/maps/web/)
2. Select 'Get A Key'
3. Follow the steps to create a project and receive your API key
### Meetup API Key
1. Go to [Meetup API](https://secure.meetup.com/meetup_api/key/)
2. Create an account to receive an API Key

## Instructions
1. Clone the repository `$ git clone https://github.com/MarcusNg/SafeAndSound.git`
2. Add the API Keys
   * map.html
     * Add your Google Maps API Key at the bottom of the file `src="https://maps.googleapis.com/maps/api/js?key=<YOUR GOOGLE MAPS API KEY>&callback=initMap`
   * maps.py
     * Set `api_key = '<YOUR GOOGLE MAPS API KEY>'`
   * events.py
     * Set `api_key = '<YOUR MEETUP API KEY>'`
3. Next `$ pip install flask` and `$ pip install requests`
4. Run the application `$ python app.py`
5. Go to localhost to use the web app.