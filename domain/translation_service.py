from .model import TranslationRequest, TranslationResponse
from infra.chat_gpt_client import ChatGPTClient

class TranslationService:
    def __init__(self, chat_gpt_client: ChatGPTClient):
        self.chat_gpt_client = chat_gpt_client

    async def translate(self, request: TranslationRequest) -> TranslationResponse:
        # Note: Using .value for Enums to get the string value might need adjustment based on your enum setup
        source_lang = request.source_language if request.source_language else "English"
        target_lang = request.target_language

        translated_text = await self.chat_gpt_client.translate_text(source_lang=source_lang, target_lang=target_lang, text=request.text)

        return TranslationResponse(translated_text=translated_text)
    