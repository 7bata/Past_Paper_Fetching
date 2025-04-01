# AS & A Level Past Papers Downloader

A Python tool to efficiently download Cambridge AS and A Level past exam papers from XtremePapers website.

## Features

- **Automatic Organization**: Downloads are organized by subject
- **Smart Grouping**: Subjects are divided into manageable groups for easier downloading
- **Comprehensive Logging**: All download activities and failures are logged
- **Resume Downloads**: Ability to retry failed downloads
- **Folder Structure**: Creates a clean directory structure based on subject names

## Installation

### Requirements

- Python 3.7+
- Internet connection

### Setup

1. Install the required packages:
```
pip install -r requirements.txt
```

2. Run the script:
```
python ASALEVEL.py
```

## Usage

1. The program fetches all available AS and A Level subjects
2. Subjects are automatically grouped into 4 categories
3. Choose which group to download
4. Files are downloaded to a 'downloads' folder, organized by subject
5. Download logs are saved to the 'logs' directory

## Configuration

By default, the crawler explores up to 2 levels deep into each subject's directory structure. This can be modified in the code if needed.

## Notes

- This tool is designed for educational purposes only
- Be respectful of the XtremePapers website's resources
- The tool adds delays between downloads to avoid overwhelming the server

## License

This project is available for personal use. Please respect the terms of service of the XtremePapers website. 