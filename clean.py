import os
import argparse

def delete_files_recursive(folder_paths, file_types):
    """
    Recursively searches through folders and deletes files of specified types.
    This version does not ask for confirmation.

    Args:
        folder_paths (list): A list of folder paths to search within.
        file_types (list): A list of file extensions (e.g., ['.wav', '.mp3']) to delete.
    """

    files_to_delete = []

    for folder_path in folder_paths:
        if not os.path.isdir(folder_path):
            print(f"Error: '{folder_path}' is not a valid directory.")
            continue

        print(f"Scanning folder: {folder_path}")
        for root, _, files in os.walk(folder_path):  # os.walk for recursive traversal
            for file in files:
                file_extension = os.path.splitext(file)[1].lower() # Get extension, case-insensitive
                if file_extension in file_types:
                    file_path = os.path.join(root, file)
                    files_to_delete.append(file_path)

    if not files_to_delete:
        print("No files found matching the specified file types.")
        return

    print("\nFiles to be deleted:")
    for file_path in files_to_delete:
        print(f"- {file_path}")

    print("\nDeleting files...")
    deleted_count = 0
    for file_path in files_to_delete:
        try:
            os.remove(file_path)
            deleted_count += 1
            print(f"Deleted: {file_path}")
        except OSError as e:
            print(f"Error deleting '{file_path}': {e}")

    print(f"\nSuccessfully deleted {deleted_count} files.")


def main():
    parser = argparse.ArgumentParser(description="Recursively delete files of specified types from folders.")
    parser.add_argument("folders", nargs='+', help="One or more folder paths to scan.")
    parser.add_argument(
        "-t", "--filetypes", nargs='+', default=['.wav'],
        help="File extensions to delete (e.g., '.wav' '.mp3'). Default is '.wav'."
    )

    args = parser.parse_args()

    delete_files_recursive(args.folders, [ft.lower() for ft in args.filetypes])


if __name__ == "__main__":
    main()