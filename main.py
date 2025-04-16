import speech_recognition as sr

def listen_for_command():
    recognizer = sr.Recognizer()

    with sr.Microphone() as source:
        print("🎤 Listening... Speak your command")
        audio = recognizer.listen(source)

    try:
        command = recognizer.recognize_google(audio)
        print(f"🗣️ You said: {command}")
        return command
    except sr.UnknownValueError:
        print("😕 Sorry, I couldn't understand that.")
        return None
    except sr.RequestError as e:
        print(f"⚠️ Error with the recognition service: {e}")
        return None

if __name__ == "__main__":
    listen_for_command()
