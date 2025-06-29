# tests/test_translation.py

from fastapi.testclient import TestClient  # type: ignore
from main import app  # type: ignore

client = TestClient(app)

def test_translate_single_success():
    payload = {
        "input_text": "Hello",
        "destination_language": "hi"
    }
    response = client.post("/translate", json=payload)
    assert response.status_code == 200
    assert "output_text" in response.json()
    assert isinstance(response.json()["output_text"], str)

def test_translate_single_invalid_language():
    payload = {
        "input_text": "Hello",
        "destination_language": "zz"  # unsupported language
    }
    response = client.post("/translate", json=payload)
    assert response.status_code == 400
    assert response.json()["detail"] == "Unsupported destination language code."

def test_translate_single_long_text():
    payload = {
        "input_text": "a" * 1001,  # exceeds 1000 characters
        "destination_language": "hi"
    }
    response = client.post("/translate", json=payload)
    assert response.status_code == 400
    assert response.json()["detail"] == "Input text must be between 1 and 1000 characters."

def test_translate_bulk_success():
    payload = {
        "input_texts": ["Hello", "Good morning"],
        "destination_language": "hi"
    }
    response = client.post("/translate/bulk", json=payload)
    assert response.status_code == 200
    assert "output_texts" in response.json()
    assert len(response.json()["output_texts"]) == 2

def test_health_check():
    response = client.get("/health")
    assert response.status_code == 200
    assert response.json() == {"status": "ok"}

def test_view_logs():
    response = client.get("/logs")
    assert response.status_code == 200
    assert isinstance(response.json(), list)
