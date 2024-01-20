# FileNest Pro

FileNest Pro is a file organization tool written in Python that automatically categorizes and organizes files in specified directories.

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
10. [New Updates](#new-updates)
11. [Adding to Task Scheduler](#adding-to-task-scheduler)

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
   cd FileNest-Pro


Sure, here's an updated version of your README file:

markdown
Copy code
# FileNest Pro

FileNest Pro is a file organization tool written in Python that automatically categorizes and organizes files in specified directories.

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
10. [New Updates](#new-updates)
11. [Adding to Task Scheduler](#adding-to-task-scheduler)

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
   cd FileNest-Pro
Install dependencies:
bash
Copy code
pip install -r requirements.txt
Configuration
Create a configuration file (config.txt) in the project directory.

Example configuration:


input_directories: C:\Users\pious\Downloads, C:\Users\pious\OneDrive\Documents, C:\Users\pious\OneDrive\Desktop
output_directory: C:\Users\pious\OneDrive\Desktop\Organized
exclude_extensions: .lnk
exclude_folders: Desktop Shortcuts
schedule_times: 08:13,18:00
Usage
Run the script using the following command:


python organizer.py
Customization
Modify the config.txt file to customize input directories, output directory, excluded extensions, excluded folders, and scheduled times.

Scheduled Execution
The script can be scheduled to run automatically at specified times. Example:


schedule_times: 08:13,18:00
This will schedule the organization task to run at 8:13 AM and 6:00 PM every day.

Contribution
Feel free to contribute by opening issues or submitting pull requests. Contributions are welcome!

License
This project is licensed under the MIT License.

New Updates
Version X.Y.Z (Replace with the actual version)
Add any new features, improvements, or bug fixes here.
Adding to Task Scheduler
Create a batch file (run_filenest.bat) with the following content:


@echo off
start "" "organizer.py"
Save the batch file in the same directory as organizer.py.

Use Windows Task Scheduler to set up a task that runs the batch file at your specified intervals.


