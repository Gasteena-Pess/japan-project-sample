import speech_recognition as sr

def transcribe_audio(audio_file_path):
    recognizer = sr.Recognizer()

    # Load the audio file
    with sr.AudioFile(audio_file_path) as source:
        audio_data = recognizer.record(source)

    try:
        # Use Google Speech Recognition API to convert audio to text
        text = recognizer.recognize_google(audio_data)
        return text
    except sr.UnknownValueError:
        print("Google Speech Recognition could not understand the audio")
    except sr.RequestError as e:
        print(f"Could not request results from Google Speech Recognition service; {e}")

    return None

# Example usage
audio_file_path = "path/to/your/audio/file.wav"
result = transcribe_audio(audio_file_path)

if result:
    print("Transcription:")
    print(result)
