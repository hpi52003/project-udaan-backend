import sqlite3
from datetime import datetime

# Establish DB connection
database_connection = sqlite3.connect("translations.db", check_same_thread=False)
db_cursor = database_connection.cursor()

# Create logs table if it doesn't exist
db_cursor.execute("""
CREATE TABLE IF NOT EXISTS translations (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    text TEXT NOT NULL,
    translated TEXT NOT NULL,
    lang TEXT NOT NULL,
    timestamp TEXT NOT NULL
)
""")
database_connection.commit()

def record_translation_log(original_text: str, translated_text: str, language_code: str):
    timestamp = datetime.utcnow().isoformat()
    db_cursor.execute("""
        INSERT INTO translations (text, translated, lang, timestamp)
        VALUES (?, ?, ?, ?)
    """, (original_text, translated_text, language_code, timestamp))
    database_connection.commit()

def fetch_all_translation_logs():
    db_cursor.execute("SELECT * FROM translations")
    return db_cursor.fetchall()
