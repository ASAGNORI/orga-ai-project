import httpx
from typing import List, Dict, Any, Optional
from app.core.config_instance import settings

class OllamaClient:
    def __init__(self):
        self.base_url = settings.OLLAMA_BASE_URL
        self.client = httpx.AsyncClient(timeout=30.0)
    
    async def list_models(self) -> List[str]:
        """Get list of available models from Ollama."""
        async with self.client as client:
            response = await client.get(f"{self.base_url}/api/tags")
            response.raise_for_status()
            return [model["name"] for model in response.json()["models"]]
    
    async def chat(
        self,
        model: str,
        messages: List[Dict[str, str]],
        temperature: float = 0.7,
        top_p: float = 0.9,
        max_tokens: Optional[int] = None
    ) -> Dict[str, Any]:
        """Send a chat request to Ollama."""
        payload = {
            "model": model,
            "messages": messages,
            "options": {
                "temperature": temperature,
                "top_p": top_p,
            }
        }
        if max_tokens:
            payload["options"]["num_predict"] = max_tokens
            
        async with self.client as client:
            response = await client.post(
                f"{self.base_url}/api/chat",
                json=payload
            )
            response.raise_for_status()
            return response.json()
    
    async def generate(
        self,
        model: str,
        prompt: str,
        temperature: float = 0.7,
        top_p: float = 0.9,
        max_tokens: Optional[int] = None
    ) -> Dict[str, Any]:
        """Generate text using Ollama."""
        payload = {
            "model": model,
            "prompt": prompt,
            "options": {
                "temperature": temperature,
                "top_p": top_p,
            }
        }
        if max_tokens:
            payload["options"]["num_predict"] = max_tokens
            
        async with self.client as client:
            response = await client.post(
                f"{self.base_url}/api/generate",
                json=payload
            )
            response.raise_for_status()
            return response.json()

# Create a singleton instance
ollama_client = OllamaClient() 