# Audio Samples

Place your audio files in this directory to test the speech recognition system.

## Supported Formats

- WAV (.wav)
- MP3 (.mp3)
- FLAC (.flac)
- OGG (.ogg)
- And other formats supported by pydub

## Example Usage

```bash
# Transcribe a WAV file (from project root directory)
python main.py --file samples/sample.wav

# Transcribe an MP3 file with specified language
python main.py --file samples/sample.mp3 --language en-US

# Use the sphinx engine (offline, no internet required)
python main.py --file samples/sample.wav --api sphinx
```

## Finding Test Audio Files

You can find free speech audio samples from sources like:

1. [Open Speech and Language Resources](http://www.openslr.org/)
2. [Common Voice by Mozilla](https://commonvoice.mozilla.org/datasets)
3. [LibriSpeech](http://www.openslr.org/12/)
4. Record your own using audio recording software

Remember that the quality of transcription depends on various factors including:
- Audio quality
- Background noise
- Speaker accent
- Speech clarity 