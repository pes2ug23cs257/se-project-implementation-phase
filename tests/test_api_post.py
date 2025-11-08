from backend.app import app

def test_predict_post():
    client = app.test_client()
    resp = client.post("/predict", data={"file": (b"fake", "test.jpg")})
    assert resp.status_code == 200
    assert "label" in resp.get_json()
