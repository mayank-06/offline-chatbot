import os
from gtts import gTTS
import pyglet
import time
import speech_recognition as sr

def record_voice():
    recognizer = sr.Recognizer()
    with sr.Microphone() as source:
        print("🎤 Speak now...")
        audio = recognizer.listen(source)
        try:
            return recognizer.recognize_google(audio)
        except:
            return None

def speak_text(text):
    tts = gTTS(text)
    tts.save("response.mp3")
    music = pyglet.media.load("response.mp3", streaming=False)
    music.play()
    time.sleep(music.duration)
    os.remove("response.mp3")