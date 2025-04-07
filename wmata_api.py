import json
import requests
from flask import Flask

app = Flask(__name__)

# API endpoint URL's and access keys
API_KEY = "28383a3bbe734ec6bae673d366de7486"
INCIDENTS_URL = "https://api.wmata.com/Incidents.svc/json/ElevatorIncidents"
headers = {"api_key": API_KEY, 'Accept': '*/*'}

# Get incidents by machine type (elevators/escalators)
# Field is called "unit_type" in WMATA API response
@app.route('/incidents/<unit_type>', methods= ['GET'])
def get_incidents(unit_type):

    # Create an empty list called 'incidents', Use 'requests' to do a GET request
    # to the WMATA Incidents API and Retrieve the JSON from the response
    incidents = []
    response = requests.get(INCIDENTS_URL, headers=headers)

    data = response.json()['ElevatorIncidents']

    # Iterate through the JSON response and retrieve all incidents matching 'unit_type'.
    # For each incident, create a dictionary containing 4 fields, add each incident dictionary
    # object to the 'incidents' list and return the list of incident dictionaries using json.dumps()
    for incident in data:
        if incident['UnitType'] == unit_type:
            incident_data = ({
                    'StationCode': incident['StationCode'],
                    'StationName': incident['StationName'],
                    'UnitName': incident['UnitName'],
                    'UnitType': incident['UnitType']})
            incidents.append(incident_data)

    return json.dumps(incidents)

# url to rest: 
# http://127.0.0.1:5000/incidents/ESCALATOR 
# http://127.0.0.1:5000/incidents/ELEVATOR

if __name__ == '__main__':
    app.run(debug=True)

