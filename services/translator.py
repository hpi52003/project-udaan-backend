from googletrans import Translator  # type: ignore

translator_engine = Translator()

def perform_translation(original_text: str, target_language_code: str) -> str:
    try:
        translation_result = translator_engine.translate(original_text, dest=target_language_code)
        return translation_result.text
    except Exception:
        return "[Translation failed]"
