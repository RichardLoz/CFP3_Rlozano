# pip install SpeechRecognition
# pip install PyAudio# pip install setuptools

import speech_recognition as sr

r = sr.Recognizer()

with sr.Microphone() as source:
    print("Estoy escuchando....")
    audio = r.listen(source)
    
    try:
        text = r.recognize_google(audio, language='es-ES')
        print("Que estas diciendo? :{}".format(text))
    
    except:
        print("Lo siento, no entiendo lo que estas diciendo.")