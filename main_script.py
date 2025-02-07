import os
import argparse
import subprocess
import whisper
from pathlib import Path

def split_mp3(input_file, output_dir, chunk_duration=10 * 60):
    """Splits an MP3 file into chunks using ffmpeg."""
    try:
        base_name = os.path.splitext(os.path.basename(input_file))[0]
        command = ["ffprobe", "-v", "error", "-show_entries", "format=duration", "-of", "default=noprint_wrappers=1:nokey=1", input_file]
        result = subprocess.run(command, capture_output=True, text=True, check=True)
        total_duration = float(result.stdout)
        
        os.makedirs(output_dir, exist_ok=True)

        start_time = 0
        chunk_number = 1
        chunk_paths = []

        while start_time < total_duration:
            end_time = min(start_time + chunk_duration, total_duration)
            output_file = os.path.join(output_dir, f"{base_name}_chunk_{chunk_number}.wav")

            command = [
                "ffmpeg", "-i", input_file, "-ss", str(start_time), "-to", str(end_time), "-c:a", "pcm_s16le", output_file
            ]
            subprocess.run(command, check=True)
            chunk_paths.append(output_file)
            print(f"Saved chunk {chunk_number}: {output_file}")
            
            start_time = end_time
            chunk_number += 1
        
        return chunk_paths
    except Exception as e:
        print(f"Error: {e}")
        return []

def transcribe_audio(audio_path):
    """Transcribes a WAV file using Whisper."""
    try:
        model = whisper.load_model("small")
        result = model.transcribe(str(audio_path), language="sr", task="transcribe")
        return result["text"]
    except Exception as e:
        print(f"Error during transcription: {e}")
        return None

def process_folder(input_folder, output_folder, chunk_duration):
    """Processes all MP3 files in a folder: splits and transcribes them."""
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
            
            chunk_paths = split_mp3(input_file, file_output_dir, chunk_duration)
            full_transcription = ""
            
            for chunk_path in chunk_paths:
                transcription = transcribe_audio(chunk_path)
                if transcription:
                    full_transcription += transcription + "\n"
            
            if full_transcription:
                transcript_file = os.path.join(file_output_dir, f"{os.path.splitext(file_name)[0]}.txt")
                with open(transcript_file, 'w', encoding='utf-8') as f:
                    f.write(full_transcription)
                print(f"Transcription saved: {transcript_file}")
    
    print("All files processed.")

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Split and transcribe MP3 files in a folder.")
    parser.add_argument("input_folder", help="Path to the input folder containing MP3 files.")
    parser.add_argument("-o", "--output_folder", help="Directory to save chunks and transcriptions (default: 'output')", default="output")
    parser.add_argument("-d", "--duration", help="Duration of each chunk in minutes (default: 10)", type=int, default=10)
    
    args = parser.parse_args()
    process_folder(args.input_folder, args.output_folder, args.duration * 60)
