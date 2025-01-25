# GeoTracker

GeoTracker is a Python program designed to securely and permanently delete files and folders beyond recovery on Windows systems. It overwrites the files with random data multiple times before deletion, ensuring that the data cannot be easily recovered.

## Features

- Securely shreds individual files by overwriting with random data.
- Recursively shreds entire folders, ensuring all contents are unrecoverable.
- Provides an option to mark files for deletion upon next reboot for enhanced security.
- User-friendly command-line interface.

## Requirements

- Python 3.x
- Windows Operating System

## Installation

1. Clone this repository to your local machine.
   ```bash
   git clone https://github.com/yourusername/GeoTracker.git
   ```
2. Navigate to the project directory.
   ```bash
   cd GeoTracker
   ```

## Usage

1. Run the `GeoTracker.py` script using Python.
   ```bash
   python GeoTracker.py
   ```
2. Follow the on-screen prompts to select whether you want to shred a file or a folder.
3. Enter the path of the file or folder you wish to shred.
4. Enter the number of passes for shredding (default is 3). More passes mean more security but will take longer.
5. GeoTracker will securely delete the specified file or folder.

## Disclaimer

**Warning: Use this program with caution. Once a file or folder is shredded using GeoTracker, it cannot be recovered. Ensure you have backups of any important data before using this tool.**

## License

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for details.