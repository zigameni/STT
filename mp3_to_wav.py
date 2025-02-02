import subprocess
import argparse
from pathlib import Path

def mp3_to_wav(mp3_path, output_wav_path=None):
    """Converts an MP3 file to a WAV file using ffmpeg."""
    try:
        mp3_path = Path(mp3_path)
        if not mp3_path.exists():
            raise FileNotFoundError(f"MP3 file not found: {mp3_path}")

        if output_wav_path is None:
            output_wav_path = mp3_path.with_suffix(".wav")  # Default output name

        command = [
            "ffmpeg",
            "-i", str(mp3_path),
            "-vn",  # Remove video if present (important for audio-only conversion)
            "-acodec", "pcm_s16le", # Ensure 16-bit PCM encoding for wide compatibility
            str(output_wav_path)
        ]

        subprocess.run(command, capture_output=True, check=True)
        return output_wav_path

    except subprocess.CalledProcessError as e:
        print(f"Error during conversion with ffmpeg: {e}")
        print(f"FFmpeg stderr: {e.stderr.decode()}")
        return None
    except FileNotFoundError as e:
        print(e)
        return None
    except Exception as e:
        print(f"An unexpected error occurred during conversion: {e}")
        return None


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Convert MP3 to WAV using ffmpeg.")
    parser.add_argument("input_mp3", help="Path to the input MP3 file")
    parser.add_argument("-o", "--output", help="Path to the output WAV file (optional). If not provided, it defaults to input_file.wav")

    args = parser.parse_args()

    input_mp3 = args.input_mp3
    output_wav = args.output

    wav_file = mp3_to_wav(input_mp3, output_wav)

    if wav_file:
        print(f"MP3 converted to WAV: {wav_file}")
    else:
        print("MP3 to WAV conversion failed.")