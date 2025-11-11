import io, json, os
from backend.app import app

def test_predict_endpoint_returns_json():
    client = app.test_client()
    fpath = os.path.join(os.path.dirname(__file__), "..", "frontend", "index.html")
    with open(fpath, "rb") as f:
        data = {"file": (io.BytesIO(f.read()), "index.html")}
        resp = client.post("/predict", data=data, content_type="multipart/form-data")
        body = json.loads(resp.data)
        assert resp.status_code == 200
        assert "label" in body and "confidence" in body
