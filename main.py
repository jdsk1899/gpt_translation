from domain.model import TranslationRequest,  TranslationResponse
from domain.translation_service import TranslationService
from fastapi import FastAPI, HTTPException
from infra.chat_gpt_client import ChatGPTClient
from infra.configuration import settings

app = FastAPI()

chat_gpt_client = ChatGPTClient(api_key=settings.API_KEY)
translation_service = TranslationService(chat_gpt_client)

@app.post("/translate", response_model=TranslationResponse)
async def translate(request: TranslationRequest):
    try:
        response =  await translation_service.translate(request)
        return response
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))
    