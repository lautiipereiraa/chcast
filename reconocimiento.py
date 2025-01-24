import speech_recognition as sr

def reconocer_voz():
    recognizer = sr.Recognizer()

    with sr.Microphone() as source:
        print("Escuchando... por favor di algo")
        recognizer.adjust_for_ambient_noise(source)  
        audio = recognizer.listen(source)

    try:
        print("Reconociendo...")
        texto = recognizer.recognize_google(audio, language="es-ES") 
        print(f"Lo que dijiste: {texto}")
        return texto
    except sr.UnknownValueError:
        print("No pude entender lo que dijiste.")
        return None
    except sr.RequestError:
        print("No se pudo conectar con el servicio de reconocimiento de voz.")
        return None

if __name__ == "__main__":
    reconocer_voz()
