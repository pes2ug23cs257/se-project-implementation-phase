"""
Test file for error paths and home route (to increase coverage).
Implements: US-014, US-022
"""
import json
from backend.app import app

def test_predict_endpoint_no_file():
    """
    GIVEN a running Flask app
    WHEN a POST request is made to /predict with NO file
    THEN check for a 400 error and a JSON error message.
    """
    client = app.test_client()
    response = client.post('/predict') # Send no file data
    
    assert response.status_code == 400
    data = json.loads(response.data)
    assert "error" in data
    assert data['error'] == "No file provided"

def test_home_route_success():
    """
    GIVEN a running Flask app
    WHEN a GET request is made to the home route '/'
    THEN check for a 200 status and the health-check message.
    """
    client = app.test_client()
    response = client.get('/')
    
    assert response.status_code == 200
    assert b"Backend is running fine!" in response.data
