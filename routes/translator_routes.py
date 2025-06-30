from fastapi import APIRouter, HTTPException, status # type: ignore
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
#Language list is added to notify by the user easily
language_reference = {
    "hindi": "hi", "tamil": "ta", "kannada": "kn", "bengali": "bn",
    "english": "en", "spanish": "es", "french": "fr", "german": "de",
    "telugu": "te", "gujarati": "gu", "malayalam": "ml", "marathi": "mr"
}


@router.get("/")
def read_root():
    return {
        "message": "Welcome to the Translation API. Use /supported-languages to view available language codes."
    }


@router.get("/supported-languages")
def get_supported_languages():
    return {"language_guide": language_reference}


@router.post("/translate", response_model=SingleTranslationOutput)
def translate_text(request: SingleTranslationInput):
    """
    Validates and translates a single block of text.
    Shows multiple errors if both validations fail.
    """
    errors = []

    if not is_valid_input_text(request.input_text):
        errors.append("❌ Input text must be between 1 and 1000 characters.")

    if not is_supported_language_code(request.destination_language):
        errors.append("❌ Unsupported destination language code.")

    if errors:
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail=errors)

    translated = perform_translation(request.input_text, request.destination_language)
    record_translation_log(request.input_text, translated, request.destination_language)
    return {"output_text": translated}


@router.post("/translate/bulk", response_model=BulkTranslationOutput)
def translate_multiple(request: BulkTranslationInput):
    """
    Validates and translates multiple lines of text.
    Aggregates all validation errors.
    """
    errors = []

    if not is_supported_language_code(request.destination_language):
        errors.append("❌ Unsupported destination language code.")

    for i, text in enumerate(request.input_texts):
        if not is_valid_input_text(text):
            errors.append(f"❌ Line {i + 1} must be between 1 and 1000 characters.")

    if errors:
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail=errors)

    translated_list = [
        perform_translation(text, request.destination_language) for text in request.input_texts
    ]

    for original, translated in zip(request.input_texts, translated_list):
        record_translation_log(original, translated, request.destination_language)

    return {"output_texts": translated_list}


@router.get("/health")
def check_health():
    return {"status": "ok"}


@router.get("/logs", response_model=list[TranslationLogRecord])
def get_translation_logs():
    logs = fetch_all_translation_logs()
    return [
        TranslationLogRecord(
            record_id=row[0],
            original_text=row[1],
            translated_text=row[2],
            language=row[3],
            translated_at=row[4]
        )
        for row in logs
    ]
