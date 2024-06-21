from gtts import gTTS
import os

def text_to_speech(text, language='en'):
    try:
        # Create a gTTS object with the input text and language
        tts = gTTS(text=text, lang=language, slow=False)

        # Save the audio to a temporary file
        temp_audio_file = "temp_audio.mp3"
        tts.save(temp_audio_file)

        # Play the audio
        os.system(f"start {temp_audio_file}")  # For Windows
        # If you're on a Mac, use the following line instead:
        # os.system(f"afplay {temp_audio_file}")
        # If you're on Linux, use the following line instead:
        # os.system(f"xdg-open {temp_audio_file}")

        # Optional: You can also return the gTTS object if you want to save it for later use
        return tts

    except Exception as e:
        print("Error occurred:", e)

if __name__ == "__main__":
    text = input("Enter the text you want to convert to speech: ")
    language = input("Enter the language code (e.g., 'en' for English, 'es' for Spanish, 'fr' for French): ")

    text_to_speech(text, language)
