import os
import argparse
import subprocess

def split_mp3(input_file, output_dir, chunk_duration=10 * 60):
    """Splits an MP3 file into chunks using only ffmpeg."""

    try:
        # 1. Get total duration using ffprobe (part of ffmpeg)
        command = ["ffprobe", "-v", "error", "-show_entries", "format=duration", "-of", "default=noprint_wrappers=1:nokey=1", input_file]
        result = subprocess.run(command, capture_output=True, text=True, check=True)
        total_duration = float(result.stdout)

        os.makedirs(output_dir, exist_ok=True)

        start_time = 0
        chunk_number = 1

        while start_time < total_duration:
            end_time = min(start_time + chunk_duration, total_duration)

            output_file = os.path.join(output_dir, f"chunk_{chunk_number}.wav")

            command = [
                "ffmpeg",
                "-i", input_file,
                "-ss", str(start_time),
                "-to", str(end_time),
                "-c:a", "pcm_s16le",  # Ensure WAV format
                output_file
            ]

            subprocess.run(command, check=True)

            print(f"Saved chunk {chunk_number}: {output_file}")

            start_time = end_time
            chunk_number += 1

    except FileNotFoundError:
        print(f"Error: Input file '{input_file}' not found.")
    except subprocess.CalledProcessError as e:
        print(f"Error running ffmpeg: {e}")
        print(f"FFmpeg command: {' '.join(e.cmd)}")
    except Exception as e:
        print(f"An error occurred: {e}")

if __name__ == "__main__":  # This is the main part of the script
    parser = argparse.ArgumentParser(description="Split an MP3 file into chunks.")
    parser.add_argument("input_file", help="Path to the input MP3 file.")
    parser.add_argument("-o", "--output_dir", help="Directory to save chunks (default: 'chunks')", default="chunks")
    parser.add_argument("-d", "--duration", help="Duration of each chunk in minutes (default: 10)", type=int, default=10)

    args = parser.parse_args()  # Parse command-line arguments

    input_mp3 = args.input_file
    output_dir = args.output_dir
    chunk_duration = args.duration * 60  # Convert minutes to seconds

    split_mp3(input_mp3, output_dir, chunk_duration)  # Call the splitting function
    print("Splitting complete.")