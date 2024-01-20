import os
import re
import shutil
import schedule
import time as sleep_time
from pathlib import Path
from win10toast import ToastNotifier

def hide_console():
    import ctypes
    ctypes.windll.user32.ShowWindow(ctypes.windll.kernel32.GetConsoleWindow(), 0)

def show_console():
    import ctypes
    ctypes.windll.user32.ShowWindow(ctypes.windll.kernel32.GetConsoleWindow(), 1)

def extract_names(file_path):
    # Extract names from text documents
    if file_path.endswith(('.txt', '.doc', '.docx', '.rtf')):
        try:
            with open(file_path, 'r', encoding='utf-8', errors='ignore') as file:
                content = file.read()
                return re.findall(r'\b[A-Z][a-z]*\b', content)  # Extract capitalized words as names
        except UnicodeDecodeError:
            print(f"Error decoding file: {file_path}")
    return []

def is_shortcut(file_path):
    # Check if the file is a shortcut (.lnk)
    return Path(file_path).suffix.lower() == '.lnk'

def is_in_excluded_folder(file_path, excluded_folders):
    # Check if the file is within an excluded folder
    parent_folder = Path(file_path).parent.name
    return parent_folder in excluded_folders

def organize_files(input_directories, output_directory, exclude_extensions, exclude_folders, toaster):
    # Create output directory if it doesn't exist
    if not os.path.exists(output_directory):
        os.makedirs(output_directory)

    # Rest of the code to organize files
    files_found = False  # Flag to check if files are found for organization
    for input_directory in input_directories:
        for file in os.listdir(input_directory):
            file_path = os.path.join(input_directory, file)

            # Skip organizing if the file is a shortcut, in excluded folders, or in excluded files
            if not is_shortcut(file_path) and not is_in_excluded_folder(file_path, exclude_folders):
                if os.path.isfile(file_path) and not file.endswith(tuple(exclude_extensions)):
                    file_type = get_file_type(file_path)
                    category_folder = get_category_folder(file_type)
                    name_directory = os.path.join(output_directory, category_folder)
                    os.makedirs(name_directory, exist_ok=True)

                    # Check if the file already exists in the destination folder
                    dest_file_path = os.path.join(name_directory, file)
                    if os.path.exists(dest_file_path):
                        # If it exists, you can choose to skip or rename the file
                        print(f"Skipped existing file: {file_path}")
                    else:
                        files_found = True
                        shutil.move(file_path, dest_file_path)
                        print(f"Moved {file} to {name_directory}")
                else:
                    print(f"Excluded file: {file_path}")
            else:
                print(f"Skipped {file_path}")

    # Show toast notification
    if files_found:
        toaster.show_toast("File Organizer", "Files organized successfully!", duration=5)
    else:
        toaster.show_toast("File Organizer", "No files found for organization.", duration=5)
        hide_console()

def get_file_type(file_path):
    # Mapping file extensions to file types
    file_extension = Path(file_path).suffix.lower()
    file_types = {
        ".docx": "Word Documents",
        ".xlsx": "Excel",
        ".pptx": "PowerPoint",
        ".pdf": "PDF",
        ".jpg": "Images",
        ".mp3": "Music",
        ".mp4": "Videos",
        ".rar": "Zip Files",
        ".txt": "Text Documents",
        ".odt": "Text Documents",
        ".ods": "Spreadsheets",
        ".odp": "Presentations",
        ".png": "Images",
        ".gif": "Images",
        ".jpeg": "Images",
        ".bmp": "Images",
        ".tiff": "Images",
        ".svg": "Images",
        ".ogg": "Music",
        ".wav": "Music",
        ".flac": "Music",
        ".avi": "Videos",
        ".mov": "Videos",
        ".wmv": "Videos",
        ".flv": "Videos",
        ".mkv": "Videos",
        ".zip": "Compressed Files",
        ".tar": "Compressed Files",
        ".gz": "Compressed Files",
        ".7z": "Compressed Files",
        ".exe": "Executables and Libraries",
        ".dll": "Executables and Libraries",
        ".csv": "Data Formats",
        ".xml": "Data Formats",
        # Add more file types as needed
    }
    return file_types.get(file_extension, "Other")

def get_category_folder(file_type):
    # Mapping file types to category folders
    category_folders = {
        "Word Documents": "Word Documents",
        "Excel": "Excel",
        "PowerPoint": "PowerPoint",
        "PDF": "PDF",
        "Images": "Images",
        "Music": "Music",
        "Videos": "Videos",
        "Zip Files": "Compressed Files",
        "Text Documents": "Text Documents",
        "Spreadsheets": "Spreadsheets",
        "Presentations": "Presentations",
        "Compressed Files": "Compressed Files",
        "Executables and Libraries": "Executables and Libraries",
        "Data Formats": "Data Formats",
        # Add more categories as needed
    }
    return category_folders.get(file_type, "Other")

def read_configuration_file(file_path):
    # Read configuration from a text file
    configuration = {
        'input_directories': [],
        'output_directory': '',
        'exclude_extensions': [],
        'exclude_folders': [],
        'schedule_times': [],
    }

    try:
        with open(file_path, 'r') as file:
            for line in file:
                key, value = map(str.strip, line.split(':', 1))
                if key == 'input_directories':
                    configuration['input_directories'] = [path.strip() for path in value.split(',')]
                elif key == 'output_directory':
                    configuration['output_directory'] = value
                elif key == 'exclude_extensions':
                    configuration['exclude_extensions'] = [ext.strip() for ext in value.split(',')]
                elif key == 'exclude_folders':
                    configuration['exclude_folders'] = [folder.strip() for folder in value.split(',')]
                elif key == 'schedule_times':
                    configuration['schedule_times'] = [time.strip() for time in value.split(',')]
    except FileNotFoundError:
        print("Configuration file not found.")
    except Exception as e:
        print(f"Error reading configuration: {e}")

    return configuration

# Example usage
config_file_path = 'config.txt'  # Replace with the path to your configuration file
config = read_configuration_file(config_file_path)

input_directories = config['input_directories']
output_directory = config['output_directory']
exclude_extensions = config['exclude_extensions']
exclude_folders = config['exclude_folders']
schedule_times = config['schedule_times']

# Set up toaster for toast notifications
toaster = ToastNotifier()

# Schedule the job to run at the specified times
for time in schedule_times:
    schedule.every().day.at(time).do(
        organize_files,
        input_directories=input_directories,
        output_directory=output_directory,
        exclude_extensions=exclude_extensions,
        exclude_folders=exclude_folders,
        toaster=toaster
    )

# Run the scheduled jobs
while True:
    schedule.run_pending()
    sleep_time.sleep(1)
    show_console()  # Show console after each check to ensure it's visible if there's any output
