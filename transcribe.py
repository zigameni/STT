import whisper
import sys
import argparse
from pathlib import Path

def transcribe_audio(audio_path):
    """
    Transcribe audio file using Whisper model
    
    Parameters:
    audio_path (str): Path to the WAV file
    
    Returns:
    str: Transcribed text
    """
    try:
        # Load the base model
        model = whisper.load_model("base")
        
        # Transcribe the audio
        result = model.transcribe(audio_path)
        
        return result["text"]
    
    except Exception as e:
        return f"Error during transcription: {str(e)}"

def main():
    # Set up argument parser
    parser = argparse.ArgumentParser(description='Transcribe WAV audio files to text')
    parser.add_argument('input_file', help='Path to input WAV file')
    parser.add_argument('-o', '--output', help='Path to output text file (optional)')
    
    args = parser.parse_args()
    
    # Check if input file exists
    input_path = Path(args.input_file)
    if not input_path.exists():
        print(f"Error: Input file '{args.input_file}' does not exist")
        sys.exit(1)
    
    # Transcribe the audio
    print("Transcribing audio... This may take a few minutes.")
    transcribed_text = transcribe_audio(str(input_path))
    
    # Handle output
    if args.output:
        output_path = Path(args.output)
        output_path.write_text(transcribed_text)
        print(f"Transcription saved to: {output_path}")
    else:
        print("\nTranscription:")
        print(transcribed_text)

if __name__ == "__main__":
    main()