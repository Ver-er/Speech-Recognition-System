# Speech Recognition System

*COMPANY*: CODTECH IT SOLUTIONS

*NAME*: PALADUGU VISHNU VARDHAN

*INTERN ID*: CODF32

*DOMAIN*: ARTIFICIAL INTELLIGENCE 

*DURATION*: 4 WEEEKS

*MENTOR*: NEELA SANTOSH KUMAR


A simple speech-to-text system that transcribes audio files using pre-trained models via the SpeechRecognition library.

## Features

- Transcribe audio files to text
- Support for multiple audio formats (.wav, .mp3, etc.)
- Uses Google's Speech Recognition API
- Simple command-line interface

## Installation

1. Clone this repository:
```
git clone https://github.com/Ver-er/Speech-Recognition-System.git
cd Speech-Recognition-System
```

2. Install required dependencies:
```
pip install -r requirements.txt
```

3. Install FFmpeg (required for audio conversion):
   - **Windows**: Download from [ffmpeg.org](https://ffmpeg.org/download.html)
   - **macOS**: `brew install ffmpeg`
   - **Linux**: `sudo apt install ffmpeg` or equivalent for your distribution

4. Configure FFmpeg path:
   - Open `audio_handler.py`
   - Set the `FFMPEG_PATH` variable to point to your FFmpeg executable
   - Example: `FFMPEG_PATH = r"C:\ffmpeg\bin\ffmpeg.exe"`

### Note on PyAudio Installation

If you encounter issues installing PyAudio, you may need to install additional system dependencies:

- **Windows**: `pip install pipwin` followed by `pipwin install pyaudio`
- **macOS**: `brew install portaudio` followed by `pip install pyaudio`
- **Linux**: `sudo apt-get install python3-pyaudio` or equivalent for your distribution

## Usage

Run the application with an audio file:
```
python main.py --file samples/your_audio_file.mp3 --language en-US
```

### Available Options

- `--file` (required): Path to the audio file
- `--language` (optional): Language code for recognition (default: en-US)
- `--api` (optional): Recognition API to use (choices: google, sphinx; default: google)

## Project Structure

```
speech-recognition-system/
├── main.py                 # Command-line interface
├── audio_handler.py        # Audio loading and processing
├── transcriber.py          # Speech recognition logic
├── requirements.txt        # Project dependencies
└── samples/                # Example audio files
```

## Dependencies

- SpeechRecognition
- PyAudio
- pocketsphinx (for offline recognition)
- FFmpeg (system dependency)

## License

MIT 

# Output

![output](output.png)