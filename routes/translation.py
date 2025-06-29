# routes/translator_routes.py
from fastapi import APIRouter, HTTPException # type: ignore
from fastapi.responses import JSONResponse # type: ignore
from models.schemas import ( # type: ignore
    SingleTranslationInput,
    SingleTranslationOutput,
    BulkTranslationInput,
    BulkTranslationOutput,
    TranslationLogRecord
)
from services.translator import perform_translation # type: ignore
from utils.validators import is_valid_input_text, is_supported_language_code # type: ignore
from db.logger import record_translation_log, fetch_all_translation_logs # type: ignore

router = APIRouter()

@router.post("/translate", response_model=SingleTranslationOutput)
def translate_single(request: SingleTranslationInput):
    if not is_valid_input_text(request.input_text):
        raise HTTPException(status_code=400, detail="Input text must be between 1 and 1000 characters.")
    if not is_supported_language_code(request.destination_language):
        raise HTTPException(status_code=400, detail="Unsupported destination language code.")

    translated_text = perform_translation(request.input_text, request.destination_language)
    record_translation_log(request.input_text, translated_text, request.destination_language)
    return {"output_text": translated_text}

@router.post("/translate/bulk", response_model=BulkTranslationOutput)
def translate_bulk(request: BulkTranslationInput):
    if any(not is_valid_input_text(text) for text in request.input_texts):
        raise HTTPException(status_code=400, detail="All input texts must be between 1 and 1000 characters.")
    if not is_supported_language_code(request.destination_language):
        raise HTTPException(status_code=400, detail="Unsupported destination language code.")

    translations = [perform_translation(text, request.destination_language) for text in request.input_texts]
    for original, translated in zip(request.input_texts, translations):
        record_translation_log(original, translated, request.destination_language)
    return {"output_texts": translations}

@router.get("/health")
def health_check():
    return {"status": "ok"}

@router.get("/logs", response_model=list[TranslationLogRecord])
def view_logs():
    logs = fetch_all_translation_logs()
    formatted_logs = [
        TranslationLogRecord(
            record_id=row[0],
            original_text=row[1],
            translated_text=row[2],
            language=row[3],
            translated_at=row[4]
        ) for row in logs
    ]
    return formatted_logs
