# preprocess_audio.py (Standalone preprocessing script)

import subprocess
import argparse  # For command-line arguments
from pathlib import Path

def preprocess_audio(audio_path, target_sr=16000):
    """Preprocesses audio using ffmpeg."""
    try:
        audio_path = Path(audio_path)
        if not audio_path.exists():
            raise FileNotFoundError(f"Audio file not found: {audio_path}")

        output_path = audio_path.with_suffix(".preprocessed.wav")  # Output file

        command = [
            "ffmpeg",
            "-i", str(audio_path),
            "-ar", str(target_sr),
            "-ac", "1",
            "-c:a", "pcm_s16le",
            str(output_path)
        ]
        subprocess.run(command, capture_output=True, check=True)
        return output_path

    except subprocess.CalledProcessError as e:
        print(f"Error during preprocessing with ffmpeg: {e}")
        print(f"FFmpeg stderr: {e.stderr.decode()}")
        return None
    except FileNotFoundError as e:
        print(e)
        return None
    except Exception as e:
        print(f"An unexpected error occurred during preprocessing: {e}")
        return None


if __name__ == "__main__":  # This block makes it a standalone script
    parser = argparse.ArgumentParser(description="Preprocess audio using ffmpeg.")
    parser.add_argument("input_audio", help="Path to the input audio file")
    parser.add_argument("-o", "--output", help="Path to the output preprocessed audio file (optional). If not provided, it defaults to input_file.preprocessed.wav")
    parser.add_argument("-sr", "--samplerate", type=int, default=16000, help="Target sample rate (default: 16000)")


    args = parser.parse_args()

    input_audio = args.input_audio
    output_audio = args.output or Path(input_audio).with_suffix(".preprocessed.wav") # default name
    target_sr = args.samplerate

    preprocessed_audio = preprocess_audio(input_audio, target_sr)

    if preprocessed_audio:
        print(f"Preprocessed audio saved to: {preprocessed_audio}")
    else:
        print("Audio preprocessing failed.")