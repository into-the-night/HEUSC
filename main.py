from s2t import get_speech

speech = get_speech()
speech = speech['text']

print(speech)
t = speech.split(' ')
if (t[1] == 'Play'):
    from play import play_music
    play_music(t[2:])
else:
    from search import ask_google
    answer = ask_google(speech)
    from t2s import speak
    speak(answer)



