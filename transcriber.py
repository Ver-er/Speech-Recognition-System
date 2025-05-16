import speech_recognition as sr
from audio_handler import load_audio

class Transcriber:
    def __init__(self, language="en-US"):
        """
        Initialize the transcriber
        
        Args:
            language (str): Language code for recognition (default: en-US)
        """
        self.recognizer = sr.Recognizer()
        self.language = language
    
    def transcribe_file(self, file_path, api="google"):
        """
        Transcribe an audio file to text
        
        Args:
            file_path (str): Path to the audio file
            api (str): Speech recognition API to use (default: google)
            
        Returns:
            str: Transcribed text
        """
        try:
            # Load audio file
            audio_file = load_audio(file_path)
            
            # Extract audio data
            with audio_file as source:
                audio_data = self.recognizer.record(source)
            
            # Perform speech recognition
            if api == "google":
                text = self.recognizer.recognize_google(audio_data, language=self.language)
            elif api == "sphinx":
                text = self.recognizer.recognize_sphinx(audio_data, language=self.language)
            elif api == "wit":
                # Requires API key
                raise NotImplementedError("Wit.ai API key required. Use google or sphinx instead.")
            else:
                raise ValueError(f"Unsupported API: {api}")
                
            return text
        
        except sr.UnknownValueError:
            return "Speech recognition could not understand audio"
        except sr.RequestError as e:
            return f"Could not request results from speech recognition service; {e}"
        except Exception as e:
            return f"Error during transcription: {e}" 