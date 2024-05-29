# SpeechRecognition ==> Nos ayuda a decodificar el audio
# Setuptools
# pyAudio

#Importar la biblioteca SpeechRecognition
import speech_recognition as sr
#Creamos instancia de Recognizer, que es la clase principal para el reconocimiento de voz
r = sr.Recognizer()
# Usar el microfono como fuente de audio
with sr.Microphone() as source:
    #Imprime un mensaje indicando que el programa esta escuchando
    print("Estoy escuchando.....")
    #Escucha el audio desde el microfono
    audio = r.listen(source)
    
    try:
        #Intentamos reconocer el audio usando el servicio de reconocimiento de Google
        #Especificar que el idioma es español
        text = r.recognize_google(audio, language = 'es-ES')
        print("Transcripción exitosa: {}" .format(text))
        
    except:
        print("No se pudo reconocer el audio")
    