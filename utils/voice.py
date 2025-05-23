import speech_recognition as sr
import os

def recognize_voice_from_file(file_path):
    recognizer = sr.Recognizer()
    with sr.AudioFile(file_path) as source:
        audio = recognizer.record(source)
    try:
        text = recognizer.recognize_whisper(audio)
        return text
    except Exception as e:
        return f"[Ошибка распознавания]: {e}"
