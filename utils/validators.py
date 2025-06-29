def is_valid_input_text(text: str) -> bool:
    return 0 < len(text) <= 1000

def is_supported_language_code(lang_code: str) -> bool:
    allowed_languages = ['hi', 'ta', 'kn', 'bn', 'en', 'es', 'fr', 'de', 'te', 'gu', 'ml', 'mr']
    return lang_code in allowed_languages
