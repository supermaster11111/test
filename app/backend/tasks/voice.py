import threading
try:
    import speech_recognition as sr
    import pyttsx3
except Exception:  # library may be missing
    sr = None
    pyttsx3 = None
from .config import SECRETS
from .logger import logger


def _loop():
    if not sr or not pyttsx3:
        logger.warning("Voice libraries not available")
        return
    recognizer = sr.Recognizer()
    engine = pyttsx3.init()
    mic = sr.Microphone()
    while True:
        with mic as source:
            audio = recognizer.listen(source, phrase_time_limit=5)
        try:
            text = recognizer.recognize_google(audio).lower()
            if "hey bro" in text:
                logger.info("Wake word detected")
                engine.say("Hello")
                engine.runAndWait()
        except Exception:
            continue


def start_voice_thread():
    if not SECRETS.get('voice', {}).get('enabled', False):
        logger.info("Voice assistant disabled in config")
        return
    thread = threading.Thread(target=_loop, daemon=True)
    thread.start()
    logger.info("Voice thread started")
