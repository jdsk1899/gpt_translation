import httpx
from fastapi import HTTPException

class ChatGPTClient:
    def __init__(self, api_key: str):
        self.api_key = api_key
        self.headers = {
            "Authorization": f"Bearer {self.api_key}",
            "Content-Type": "application/json",
        }
        self.endpoint = "https://api.openai.com/v1/chat/completions"

    async def translate_text(self, source_lang: str, target_lang: str, text: str, model: str = "gpt-3.5-turbo", temperature: float = 0) -> str:
        payload = {
            "model": model,
            "messages": [
                {"role": "system", "content": f"Translate this {text} from {source_lang} to {target_lang}."},
                {"role": "user", "content": text},
            ],
            "temperature": temperature,
        }
        async with httpx.AsyncClient() as client:
            response = await client.post(self.endpoint, headers=self.headers, json=payload)

        if not response.is_success:
            raise HTTPException(status_code=response.status_code, detail=f"OpenAI API error: {response.text}")

        data = response.json()
        try:
            translated_text = data["choices"][0]["message"]["content"]
            return translated_text
        except (KeyError, IndexError):
            raise HTTPException(status_code=500, detail="Unexpected response format from OpenAI API.")
