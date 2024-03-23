from enum import Enum
from pydantic import BaseModel
from typing import Optional

class LanguageCode(str, Enum):
    en = "English"
    fr = "French"
    es = "Spanish"
    de = "German"

class TranslationRequest(BaseModel):
    text: str
    target_language: LanguageCode
    source_language: Optional[LanguageCode] = None

class TranslationResponse(BaseModel):
    translated_text: str
    