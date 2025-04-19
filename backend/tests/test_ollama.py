import pytest
from fastapi.testclient import TestClient
from app.main import app

client = TestClient(app)

def test_health():
    response = client.get("/health")
    assert response.status_code == 200
    assert response.json() == {"status": "healthy"}

def test_models():
    response = client.get("/models")
    assert response.status_code == 200
    models = response.json()
    assert isinstance(models, list)
    assert len(models) > 0
    for model in models:
        assert isinstance(model, str)
        assert len(model) > 0

def test_chat_with_valid_input():
    response = client.post(
        "/chat",
        json={
            "messages": [{"role": "user", "content": "Hello, how are you?"}],
            "model": "llama2",
            "temperature": 0.7,
            "top_p": 0.9,
            "max_tokens": 100
        }
    )
    assert response.status_code == 200
    data = response.json()
    assert "response" in data
    assert isinstance(data["response"], str)
    assert len(data["response"]) > 0

def test_chat_with_invalid_model():
    response = client.post(
        "/chat",
        json={
            "messages": [{"role": "user", "content": "Hello"}],
            "model": "non_existent_model"
        }
    )
    assert response.status_code == 500
    assert "detail" in response.json()

def test_chat_with_empty_messages():
    response = client.post(
        "/chat",
        json={
            "messages": [],
            "model": "llama2"
        }
    )
    assert response.status_code == 422

def test_generate_with_valid_input():
    response = client.post(
        "/generate",
        json={
            "prompt": "Write a short poem about AI",
            "model": "llama2",
            "temperature": 0.7,
            "top_p": 0.9,
            "max_tokens": 100
        }
    )
    assert response.status_code == 200
    data = response.json()
    assert "response" in data
    assert isinstance(data["response"], str)
    assert len(data["response"]) > 0

def test_generate_with_empty_prompt():
    response = client.post(
        "/generate",
        json={
            "prompt": "",
            "model": "llama2"
        }
    )
    assert response.status_code == 422

def test_chat_with_system_message():
    response = client.post(
        "/chat",
        json={
            "messages": [
                {"role": "system", "content": "You are a helpful assistant."},
                {"role": "user", "content": "What is Python?"}
            ],
            "model": "llama2",
            "temperature": 0.7
        }
    )
    assert response.status_code == 200
    data = response.json()
    assert "response" in data
    assert isinstance(data["response"], str)
    assert len(data["response"]) > 0 