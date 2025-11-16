from gtts import gTTS
from playsound import playsound

tts = gTTS("Hello, this is a test.")
tts.save("test.mp3")
playsound("test.mp3")
