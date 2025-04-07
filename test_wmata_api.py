from wmata_api import app
import json
import unittest

class WMATATest(unittest.TestCase):
    # Ensure both endpoints return a 200 HTTP code
    # Create a test client for the Flask app
    def setUp(self):
        self.app = app.test_client()

    def test_http_success(self):
        # Assert that the response code of incidents/escalators returns a 200 code
        escalator_response = app.test_client().get("/incidents/escalators").status_code
        self.assertEqual(escalator_response, 200)

        # Assert that the response code of incidents/elevators returns a 200 code
        elevator_response = app.test_client().get("/incidents/elevators").status_code
        self.assertEqual(elevator_response, 200)

    # Ensure all returned incidents have the 4 required fields
    def test_required_fields(self):
        required_fields = ["StationCode", "StationName", "UnitType", "UnitName"]

        response = app.test_client().get("/incidents/escalators")
        json_response = json.loads(response.data.decode())

        # For each incident in the JSON response assert that each of the required fields
        # are present in the response
        for incident in json_response :
            self.assertTrue(all(field in incident for field in required_fields))

        response = app.test_client().get("/incidents/elevators")
        json_response = json.loads(response.data.decode())

        # For each incident in the JSON response assert that each of the required fields
        # are present in the response
        for incident in json_response :
            self.assertTrue(all(field in incident for field in required_fields))

    # Ensure all entries returned by the /escalators endpoint have a UnitType of "ESCALATOR"
    def test_escalators(self):
        response = app.test_client().get("/incidents/escalators")
        json_response = json.loads(response.data.decode())

        # For each incident in the JSON response, assert that the 'UnitType' is "ESCALATOR"
        for incident in json_response:
            self.assertEqual(incident["UnitType"], "ESCALATOR")

    # Ensure all entries returned by the /elevators endpoint have a UnitType of "ELEVATOR"
    def test_elevators(self):
        response = app.test_client().get("/incidents/elevators")
        json_response = json.loads(response.data.decode())

        # For each incident in the JSON response, assert that the 'UnitType' is "ELEVATOR"
        for incident in json_response:
            self.assertEqual(incident["UnitType"], "ELEVATOR")

if __name__ == "__main__":
    unittest.main()

