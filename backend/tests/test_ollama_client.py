import pytest
from app.core.ollama_client import OllamaClient
from httpx import HTTPError

@pytest.mark.asyncio
async def test_list_models():
    client = OllamaClient()
    try:
        models = await client.list_models()
        assert isinstance(models, list)
        assert len(models) > 0
        # Verify model format
        for model in models:
            assert isinstance(model, str)
            assert len(model) > 0
    except HTTPError as e:
        pytest.fail(f"Failed to list models: {str(e)}")

@pytest.mark.asyncio
async def test_chat_with_valid_input():
    client = OllamaClient()
    messages = [
        {"role": "user", "content": "Hello, how are you?"}
    ]
    try:
        response = await client.chat(
            model="llama2",
            messages=messages,
            temperature=0.7,
            top_p=0.9,
            max_tokens=100
        )
        assert "response" in response
        assert isinstance(response["response"], str)
        assert len(response["response"]) > 0
    except HTTPError as e:
        pytest.fail(f"Failed to chat: {str(e)}")

@pytest.mark.asyncio
async def test_chat_with_invalid_model():
    client = OllamaClient()
    messages = [
        {"role": "user", "content": "Hello"}
    ]
    with pytest.raises(HTTPError):
        await client.chat(
            model="non_existent_model",
            messages=messages
        )

@pytest.mark.asyncio
async def test_generate_with_valid_input():
    client = OllamaClient()
    prompt = "Write a short poem about coding."
    try:
        response = await client.generate(
            model="llama2",
            prompt=prompt,
            temperature=0.7,
            top_p=0.9,
            max_tokens=100
        )
        assert "response" in response
        assert isinstance(response["response"], str)
        assert len(response["response"]) > 0
    except HTTPError as e:
        pytest.fail(f"Failed to generate: {str(e)}")

@pytest.mark.asyncio
async def test_generate_with_empty_prompt():
    client = OllamaClient()
    with pytest.raises(HTTPError):
        await client.generate(
            model="llama2",
            prompt=""
        )

@pytest.mark.asyncio
async def test_chat_with_system_message():
    client = OllamaClient()
    messages = [
        {"role": "system", "content": "You are a helpful assistant."},
        {"role": "user", "content": "What is Python?"}
    ]
    try:
        response = await client.chat(
            model="llama2",
            messages=messages,
            temperature=0.7
        )
        assert "response" in response
        assert isinstance(response["response"], str)
        assert len(response["response"]) > 0
    except HTTPError as e:
        pytest.fail(f"Failed to chat with system message: {str(e)}") 