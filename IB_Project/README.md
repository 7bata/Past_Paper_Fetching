# IB Past Papers Downloader

A Python tool for efficiently downloading International Baccalaureate (IB) past exam papers from the XtremePapers website.

## Features

- **Examination Session Organization**: Files are organized by examination year sessions (2010-2023)
- **Original Directory Structure**: Maintains the exact same directory structure as the website for easy navigation
- **Smart Grouping**: Divides examination sessions into manageable groups for downloading
- **Comprehensive Logging**: Records all download activities and failures
- **Resume Capability**: Ability to re-download from failure logs

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
python IB.py
```

## Usage

The program offers three options:

1. **Download a Session Group**: Sessions are divided into 4 groups, each containing 3-4 examination sessions for batch downloading
2. **Re-download from Failure Log**: Resume downloading files that failed in previous attempts
3. **Exit Program**

All files will be downloaded to the `downloads` folder, organized by examination session and subject.

## Directory Structure

The downloaded files maintain the exact same directory structure as the website:

```
downloads/
├── 2022 Examination Session/
│   ├── Biology_HL/
│   │   ├── Paper_1/
│   │   │   └── ... exam files ...
│   │   ├── Paper_2/
│   │   │   └── ... exam files ...
│   │   └── Mark_Scheme/
│   │       └── ... answer files ...
│   ├── Mathematics/
│   │   ├── HL/
│   │   │   └── ... exam files ...
│   │   └── SL/
│   │       └── ... exam files ...
│   └── ... other subjects ...
└── ... other examination sessions ...
```

The directory structure perfectly replicates the original website structure, maintaining all directory levels and organization, ensuring files are placed exactly as they appear on the website.

## Configuration

By default, the crawler explores up to 4 levels deep in each examination session's directory structure, which is sufficient to cover most IB exam paper organization structures.

## Notes

- This tool is for educational purposes only
- Please respect the XtremePapers website's resources
- The tool adds delays between downloads to avoid overloading the server

## License

This project is available for personal use. Please respect the terms of service of the XtremePapers website. 