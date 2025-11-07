"""
Developer: Jayani (US-002)
Story: Integrate Upload UI with Backend API
Purpose: To verify that the upload endpoint (/predict) is reachable and returns a valid response.
"""

import io
from backend.app import app


def test_predict_post_endpoint():
    """Test that /predict returns a valid JSON with label and confidence."""
    client = app.test_client()

    # Simulate sending a dummy image file
    data = {
        "file": (io.BytesIO(b"fake image bytes"), "test.jpg")
    }

    response = client.post("/predict", data=data, content_type="multipart/form-data")

    assert response.status_code == 200, "Expected 200 OK"
    json_data = response.get_json()

    # Check response keys
    assert "label" in json_data, "Response should contain 'label'"
    assert "confidence" in json_data, "Response should contain 'confidence'"

    # Optional print for CI logs
    print("✅ /predict endpoint test passed:", json_data)

