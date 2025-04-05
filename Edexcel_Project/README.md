# Edexcel Past Papers Downloader

A Python tool for efficiently downloading Edexcel exam past papers from the XtremePapers website.

## Features

- **Original Directory Structure**: Maintains the same directory structure as the website for easy navigation
- **Automatic Organization**: Downloaded files are automatically organized by category and subject
- **Smart Grouping**: Divides categories into manageable groups for downloading
- **Comprehensive Logging**: Records all download activities and failures
- **Resume Capability**: Ability to re-download from failure logs
- **Deep Crawling**: Supports recursive crawling of multi-level directory structures

## Installation

### Requirements

- Python 3.7+
- Internet connection

### Setup

1. Install required packages:
```
pip install -r requirements.txt
```

2. Run the script:
```
python Edexcel.py
```

## Usage

1. The program will fetch all available categories under Edexcel (such as Advanced Level, International GCSE, etc.)
2. Categories will be automatically divided into 2 groups
3. Select the group you want to download
4. Files will be downloaded to the `downloads` folder, organized according to the original directory structure
5. Download logs are saved in the `logs` directory

## Directory Structure

The downloaded files maintain the original website directory structure:

```
downloads/
├── Advanced Level/
│   ├── Accounting/
│   │   ├── 2005 Jan_/
│   │   │   ├── Examiner-report/
│   │   │   │   └── 226080_Accounting_6001_MS_ER.pdf
│   │   │   └── ... other files and directories ...
│   │   └── ... other years and sessions ...
│   └── ... other subjects ...
└── International GCSE/
    └── ... similar structure ...
```

## Configuration

By default, the crawler explores up to 5 levels deep in each category's directory structure. This setting can be modified in the code if needed.

## Notes

- This tool is for educational purposes only
- Please respect the XtremePapers website's resources
- The tool adds delays between downloads to avoid overloading the server

## License

This project is available for personal use. Please respect the terms of service of the XtremePapers website. 