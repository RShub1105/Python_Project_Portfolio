
# 🗂️ File Organiser

A simple Python script to automatically organize files in a directory into categorized subfolders by file type.

## Features

- Automatically detects and categorizes files by their extensions.

- Supports multiple file types including documents, media, archives, and code files.

- Skips folders and handles errors gracefully.

- Easy to configure and use.


## How its works

This script scans a specified directory and moves files into categorized folders such as:

-     Images/ – .jpg, .png, .gif, etc.

-     Documents/ – .pdf, .docx, .txt, etc.

-     Videos/ – .mp4, .mov, .avi, etc.

-     Audio/ – .mp3, .wav, etc.

-     Archives/ – .zip, .rar, .7z, etc.

-     Scripts/ – .py, .js, .sh, etc.

-     Others/ – Any uncategorized file types.
## Installation

No external dependencies are required. Simply download or clone this repository.

bash

Copy
Edit
git clone https://github.com/yourusername/file-organiser.git
cd file-organiser
## Usage

    python file_organiser.py /path/to/your/directory

## Example

    python file_organiser.py ~/Downloads


## Folder Structure

    Downloads/
    ├── Images/
    │   ├── photo1.jpg
    ├── Documents/
    │   ├── resume.pdf
    ├── Archives/
    │   ├── backup.zip
    ├── Others/
    │   ├── unknownfile.xyz
## 📁 Supported Categories

You can modify the EXTENSION_MAP dictionary in the script to customize how file extensions are categorized.
## License

[MIT](https://choosealicense.com/licenses/mit/)

