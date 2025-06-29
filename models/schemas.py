from pydantic import BaseModel  # type: ignore
from typing import List

class SingleTranslationInput(BaseModel):
    input_text: str
    destination_language: str

class SingleTranslationOutput(BaseModel):
    output_text: str

class BulkTranslationInput(BaseModel):
    input_texts: List[str]
    destination_language: str

class BulkTranslationOutput(BaseModel):
    output_texts: List[str]

class TranslationLogRecord(BaseModel):
    record_id: int
    original_text: str
    translated_text: str
    language: str
    translated_at: str
