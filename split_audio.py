import os
import argparse
import subprocess

def split_mp3(input_file, output_dir, chunk_duration=10 * 60):
    """Splits an MP3 file into chunks using only ffmpeg."""
    try:
        base_name = os.path.splitext(os.path.basename(input_file))[0]
        
        # Get total duration using ffprobe
        command = ["ffprobe", "-v", "error", "-show_entries", "format=duration", "-of", "default=noprint_wrappers=1:nokey=1", input_file]
        result = subprocess.run(command, capture_output=True, text=True, check=True)
        total_duration = float(result.stdout)

        os.makedirs(output_dir, exist_ok=True)

        start_time = 0
        chunk_number = 1

        while start_time < total_duration:
            end_time = min(start_time + chunk_duration, total_duration)
            output_file = os.path.join(output_dir, f"{base_name}_chunk_{chunk_number}.wav")

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


def process_folder(input_folder, output_folder, chunk_duration):
    """Processes all MP3 files in a folder."""
    if not os.path.isdir(input_folder):
        print(f"Error: Input folder '{input_folder}' does not exist.")
        return
    
    os.makedirs(output_folder, exist_ok=True)
    
    for file_name in os.listdir(input_folder):
        if file_name.lower().endswith(".mp3"):
            input_file = os.path.join(input_folder, file_name)
            file_output_dir = os.path.join(output_folder, os.path.splitext(file_name)[0])
            os.makedirs(file_output_dir, exist_ok=True)
            print(f"Processing {input_file}...")
            split_mp3(input_file, file_output_dir, chunk_duration)
    
    print("All files processed.")


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Split all MP3 files in a folder into chunks.")
    parser.add_argument("input_folder", help="Path to the input folder containing MP3 files.")
    parser.add_argument("-o", "--output_folder", help="Directory to save chunks (default: 'chunks')", default="chunks")
    parser.add_argument("-d", "--duration", help="Duration of each chunk in minutes (default: 10)", type=int, default=10)
    
    args = parser.parse_args()
    
    input_folder = args.input_folder
    output_folder = args.output_folder
    chunk_duration = args.duration * 60  # Convert minutes to seconds
    
    process_folder(input_folder, output_folder, chunk_duration)
