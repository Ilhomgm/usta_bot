# utils/language_manager.py

from langdetect import detect
import json
import os

LANG_FILE = "data/user_languages.json"

def load_languages():
    if not os.path.exists(LANG_FILE):
        return {}
    with open(LANG_FILE, "r", encoding="utf-8") as f:
        return json.load(f)

def save_languages(data):
    with open(LANG_FILE, "w", encoding="utf-8") as f:
        json.dump(data, f, ensure_ascii=False, indent=2)

def detect_language(text):
    try:
        lang = detect(text)
        if lang in ['uz', 'ru', 'en', 'zh-cn', 'zh']:
            return lang
    except:
        pass
    return 'en'  # fallback

def get_user_language(user_id):
    languages = load_languages()
    return languages.get(str(user_id), 'en')

def set_user_language(user_id, lang):
    languages = load_languages()
    languages[str(user_id)] = lang
    save_languages(languages)

def translate(key, user_id):
    lang = get_user_language(user_id)
    locale_file = f"locales/{lang}.json"
    if not os.path.exists(locale_file):
        locale_file = "locales/en.json"
    with open(locale_file, "r", encoding="utf-8") as f:
        data = json.load(f)
        return data.get(key, key)
