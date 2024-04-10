from gtts import gTTS
from playsound import playsound

def speak(answer):
    tts = gTTS(answer, lang='en', tld='co.uk')
    tts.save("text.mp3")
    playsound("text.mp3")

