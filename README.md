# Serbian Speech-to-Text (STT) Transcription

This repository contains Python scripts for performing Serbian Speech-to-Text (STT) transcription using the Whisper model.  The scripts can process either individual audio files or entire folders of audio files.

## Scripts

### `split_audio.py`

*(Description of `split_audio.py` and its functionality would go here.  Since you didn't provide the code for this script, I'll add a placeholder.  Please replace this with the actual information about how to use `split_audio.py`)*

This script is used to split longer audio files into smaller chunks, which can improve the accuracy and efficiency of the transcription process.  It takes [describe the input, e.g., a long audio file] as input and outputs [describe the output, e.g., a folder of smaller audio files].

**Usage:**

```bash
python split_audio.py <path_to_long_audio_file> <output_folder> <chunk_duration_seconds>
```

### `main_script.py`

This script uses the Whisper model to transcribe audio files (MP3 or WAV format) in Serbian. It can process either a single audio file or a directory containing multiple audio files.

**Dependencies:**

*   `whisper`:  Install with `pip install git+https://github.com/openai/whisper.git`
*   `pathlib`: (Included in standard Python library)
*   `os`: (Included in standard Python library)

**Usage:**

```bash
python main_script.py <path_to_audio_file_or_folder>
```

**Arguments:**

*   `<path_to_audio_file_or_folder>`:  The path to the audio file (MP3 or WAV) or the directory containing audio files to transcribe.  If a directory is provided, all MP3 and WAV files within that directory will be processed.  Paths containing spaces should be enclosed in quotes.

**Output:**

The script generates a text file (`.txt`) for each transcribed audio file. The text file contains the transcribed text.  The output files are saved in the same directory as the audio files, with the same base name. The script also prints the language detection confidence (if available from the Whisper model).

**Example (single file):**

```bash
python main_script.py "audio_file.mp3"
```

**Example (folder):**

```bash
python main_script.py "path/to/audio/folder"
```

**Example (folder with spaces in name):**
```bash
python main_script.py "path/to/my audio/folder"
```

**Notes:**

*   The script uses the "small" Whisper model. You can change this in the `transcribe_audio` function if needed (e.g., to "base", "medium", or "large", but remember those require more resources).
*   The language is set to Serbian ("sr").
*   Error handling is included for file not found, invalid audio format, and other exceptions during transcription.
*   The script prints the path to the saved transcription and the language detection confidence (if available).

## Installation

1.  **Clone the repository:**

    ```bash
    git clone [https://github.com/zigameni/STT.git](https://www.google.com/search?q=https://github.com/zigameni/STT.git)  # Replace with your repository URL
    cd STT
    ```

2.  **Create a virtual environment (recommended):**

    ```bash
    python3 -m venv .venv
    source .venv/bin/activate  # On Windows: .venv\Scripts\activate
    ```

3.  **Install the dependencies:**

    ```bash
    pip install git+[https://github.com/openai/whisper.git](https://github.com/openai/whisper.git)
    ```

## Contributing

Contributions are welcome!  Please open an issue or submit a pull request.

## Pro tip :P

1. You can you a light weight model, such as base, and take the output and copy-paste it into Deepseek, asking it to format it for you. Check out `Prompt.txt` as an example.

2. If your audio is to big, you can use `split_audio.py` which will by default split the audio into chunks of 10 mins, and store them into a folder callled `chunks`, using the `main_script.py` you can transcribe the entire folder.  
 