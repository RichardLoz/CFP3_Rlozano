# pip install SpeechRecognition ==> Nos ayudara a decdificar el audio
# pip install PyAudio# pip install setuptools


# Importa la biblioteca speech_recognition como sr
import speech_recognition as sr

# Crea una instancia de Recognizer, que es la clase principal para el reconocimiento de voz
r = sr.Recognizer()

# Usa el micrófono como fuente de audio
with sr.Microphone() as source:
    # Imprime un mensaje indicando que el programa está escuchando
    print("Estoy escuchando....")
    
    # Escucha el audio desde el micrófono
    audio = r.listen(source)
    
    try:
        # Intenta reconocer el audio usando el servicio de reconocimiento de Google
        # Especifica que el idioma es español (es-ES)
        text = r.recognize_google(audio, language='es-ES')
        
        # Imprime el texto transcrito si el reconocimiento es exitoso
        print("Transcripción exitosa: {}".format(text))
    
    except:
        # Si ocurre un error durante el reconocimiento, imprime un mensaje de error
        print("Lo siento, no entiendo lo que estás diciendo.")
