import os
import subprocess
import speech_recognition as sr

# ===== MODIFY THIS PATH TO YOUR FFMPEG INSTALLATION =====
FFMPEG_PATH = r"C:\Users\vishn\Downloads\ffmpeg-7.1.1-essentials_build\bin\ffmpeg.exe"

def convert_to_wav(file_path):
    """
    Convert audio file to WAV format using FFmpeg
    
    Args:
        file_path (str): Path to the audio file
        
    Returns:
        str: Path to the WAV file
    """
    # Convert paths to absolute paths
    abs_file_path = os.path.abspath(file_path)
    file_name, file_extension = os.path.splitext(abs_file_path)
    
    # Check if the file exists
    if not os.path.exists(abs_file_path):
        raise FileNotFoundError(f"Audio file not found: {abs_file_path}")
    
    # Check if the file is already a WAV file
    if file_extension.lower() == '.wav':
        return abs_file_path
    
    # Set output WAV path
    wav_path = f"{file_name}.wav"
    
    try:
        # Call FFmpeg to convert the audio file
        process = subprocess.run([
            FFMPEG_PATH,
            "-y",           # Overwrite output files
            "-i", abs_file_path,  # Input file
            "-acodec", "pcm_s16le",  # Output codec
            "-ac", "1",     # Mono channel
            "-ar", "16000", # Sample rate
            wav_path        # Output file
        ], capture_output=True, text=True)
        
        # Check if conversion was successful
        if process.returncode == 0 and os.path.exists(wav_path) and os.path.getsize(wav_path) > 0:
            print(f"Converted {file_path} to WAV format ({os.path.getsize(wav_path)} bytes)")
            return wav_path
        else:
            error_msg = process.stderr[:500] if process.stderr else "Unknown error"
            raise Exception(f"FFmpeg conversion failed: {error_msg}")
            
    except Exception as e:
        raise Exception(f"Error converting audio file: {e}")

def load_audio(file_path):
    """
    Load an audio file and prepare it for recognition
    
    Args:
        file_path (str): Path to the audio file
        
    Returns:
        speech_recognition.AudioFile: Audio file ready for recognition
    """
    # Convert to WAV if needed
    wav_path = convert_to_wav(file_path)
    
    # Create audio file object
    audio_file = sr.AudioFile(wav_path)
    
    return audio_file 