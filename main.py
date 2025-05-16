import argparse
import os
import time
from transcriber import Transcriber

def main():
    # Set up command line argument parser
    parser = argparse.ArgumentParser(description="Speech Recognition System")
    parser.add_argument("--file", required=True, help="Path to the audio file")
    parser.add_argument("--language", default="en-US", help="Language code (default: en-US)")
    parser.add_argument("--api", default="google", choices=["google", "sphinx"], 
                       help="Speech recognition API to use (default: google)")
    
    # Parse arguments
    args = parser.parse_args()
    
    # Validate file path
    if not os.path.exists(args.file):
        print(f"Error: File not found: {args.file}")
        return 1
    
    print(f"Processing file: {args.file}")
    print(f"Using {args.api} API for speech recognition")
    
    # Create transcriber
    transcriber = Transcriber(language=args.language)
    
    # Measure execution time
    start_time = time.time()
    
    # Perform transcription
    result = transcriber.transcribe_file(args.file, api=args.api)
    
    # Calculate execution time
    execution_time = time.time() - start_time
    
    # Print results
    print("\nTranscription Results:")
    print("-" * 50)
    print(result)
    print("-" * 50)
    print(f"Execution time: {execution_time:.2f} seconds")
    
    return 0

if __name__ == "__main__":
    exit(main()) 