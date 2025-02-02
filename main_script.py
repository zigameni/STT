import whisper
import sys
from pathlib import Path
import os

def transcribe_audio(audio_path_str):
    """Transcribes audio (MP3 or WAV)."""
    try:
        audio_path = Path(audio_path_str)
        print(f"Processing file: {audio_path}")

        if not audio_path.exists():
            raise FileNotFoundError(f"Could not find audio file at: {audio_path}")

        if audio_path.suffix.lower() not in ['.mp3', '.wav']:
            raise ValueError("Invalid audio format. Only MP3 and WAV are supported.")

        print("Loading Whisper model...")
        model = whisper.load_model("small")

        print("Transcribing audio...")
        result = model.transcribe(str(audio_path), language="sr", task="transcribe")

        return result

    except FileNotFoundError as e:
        print(f"File not found error: {str(e)}")
        return None
    except ValueError as e:
        print(f"Invalid audio format error: {str(e)}")
        return None
    except Exception as e:
        print(f"Error during transcription: {str(e)}")
        print(f"Full error type: {type(e)}")
        return None

def process_file_or_folder(path_str):
    """Processes either a single audio file or a folder of audio files."""
    path = Path(path_str)

    if path.is_file():
        if path.suffix.lower() not in ['.mp3', '.wav']:
            print("Error: File must be an MP3 or WAV")
            return

        result = transcribe_audio(path_str)
        if result:
            output_path = path.with_suffix('.txt')
            with open(output_path, 'w', encoding='utf-8') as f:
                f.write(result["text"])
            print(f"\nTranscription saved to: {output_path}")

            # Check if language_probability exists before printing
            if 'language_probability' in result:  # The crucial fix
                print(f"Language detection confidence: {result['language_probability']:.2%}")
            else:
                print("Language detection confidence not available.")

    elif path.is_dir():
        for file in path.iterdir():
            if file.is_file() and file.suffix.lower() in ['.mp3', '.wav']:
                print(f"Processing file in folder: {file}")
                result = transcribe_audio(str(file))
                if result:
                    output_path = file.with_suffix('.txt')
                    with open(output_path, 'w', encoding='utf-8') as f:
                        f.write(result["text"])
                    print(f"Transcription saved to: {output_path}")

                    # Check if language_probability exists before printing (same fix here)
                    if 'language_probability' in result:
                        print(f"Language detection confidence: {result['language_probability']:.2%}")
                    else:
                        print("Language detection confidence not available.")
    else:
        print(f"Error: {path} is neither a file nor a directory.")


def main():
    if len(sys.argv) != 2:
        print("Usage: python script.py <path_to_audio_file_or_folder>")
        return

    path_str = ' '.join(sys.argv[1:]).strip('"')
    process_file_or_folder(path_str)


if __name__ == "__main__":
    main()