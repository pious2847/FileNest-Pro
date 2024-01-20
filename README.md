# Document Organizer

Document Organizer is a Python script that automatically organizes files in specified directories based on their types.

## Table of Contents
1. [Features](#features)
2. [Requirements](#requirements)
3. [Installation](#installation)
4. [Configuration](#configuration)
5. [Usage](#usage)
6. [Customization](#customization)
7. [Scheduled Execution](#scheduled-execution)
8. [Contribution](#contribution)
9. [License](#license)

## Features

- Organize files into categorized folders (e.g., Images, Music, Documents).
- Exclude specific file extensions and folders from organization.
- Read configuration from a text file for easy customization.
- Schedule automatic organization at specified times.

## Requirements

- Python 3.x
- pip (Python package installer)

## Installation

1. **Clone the repository:**
   ```bash
   git clone https://https://github.com/pious2847/FileNest-Pro.git
   cd document-organizer

Install dependencies:
pip install -r requirements.txt

Configuration
Create a configuration file (config.txt) in the project directory.


input_directories: path/to/directory1, path/to/directory2
output_directory: path/to/organized/folder
exclude_extensions: .lnk, .tmp
exclude_folders: Excluded Folder1, Excluded Folder2
schedule_time: 18:00
input_directories: Comma-separated list of directories to organize.
output_directory: Path to the folder where organized files will be moved.
exclude_extensions: Comma-separated list of file extensions to exclude.
exclude_folders: Comma-separated list of folders to exclude.
schedule_time: Time in 24-hour format for scheduled organization.
Usage
Run the script using the following command:


python organizer.py
Customization
Modify the config.txt file to customize input directories, output directory, excluded extensions, excluded folders, and scheduled time.

Scheduled Execution
The script can be scheduled to run automatically at a specified time. Example:


schedule_time: 18:00
This will schedule the organization task to run every day at 6:00 PM.

Contribution
Feel free to contribute by opening issues or submitting pull requests. Contributions are welcome!

License
This project is licensed under the MIT License.



Make sure to replace placeholder values (e.g., `@pious2847`, `path/to/directory1`) with the actual values for your project. Additionally, update the `LICENSE` file if needed.





