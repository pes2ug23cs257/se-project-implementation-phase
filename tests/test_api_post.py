import io
from backend.app import app

def test_predict_post():
    client = app.test_client()

    # Create a dummy file to simulate real upload
    data = {
        "file": (io.BytesIO(b"fake image data"), "test.jpg")
    }

    resp = client.post("/predict", data=data, content_type='multipart/form-data')

    assert resp.status_code == 200
    result = resp.get_json()
    assert "label" in result
    assert "confidence" in result
