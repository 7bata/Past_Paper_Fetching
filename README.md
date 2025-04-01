# Past Papers Downloader

[![License: MIT](https://img.shields.io/badge/License-MIT-blue.svg)](https://opensource.org/licenses/MIT)

A Python tool to efficiently batch download Cambridge Assessment International Education (CAIE) AS and A Level past papers from XtremePapers website.

## 📖 Overview

This tool helps students and educators quickly download organized collections of past exam papers without manual navigation through the website. It provides:

- Automatic scraping of all available subjects
- Batch downloading of papers grouped by subject
- Organized file storage following subject hierarchy
- Detailed activity logging and failure tracking
- Ability to resume failed downloads

## ✨ Features

- **Subject Organization**: Automatically groups 80+ subjects into manageable batches
- **Smart Directory Structure**: Creates folders by subject name and preserves subfolder structure
- **Efficient Batch Processing**: Downloads all files in a subject group with a single command
- **Comprehensive Logging**: Records all activity with timestamps for tracking
- **Error Handling**: Tracks failed downloads and provides retry functionality
- **File Skipping**: Avoids re-downloading existing files to save time and bandwidth

## 🔧 Installation

### Requirements
- Python 3.7+
- Internet connection

### Dependencies

```
pip install requests lxml
```

Or install using the requirements file:

```
pip install -r requirements.txt
```

## 🚀 Usage

### Running the Program

```
python ASALEVEL.py
```

### Operation Steps

1. The program will fetch and group all available subjects
2. Choose option 1 to download a subject group
3. Select which group (1-4) you want to download
4. The program will automatically download all files, organizing them by subject
5. All activity is logged to the `logs` directory
6. If any files fail to download, use option 2 to retry those specific files

## 📁 Project Structure

```
PastPapers/
├── ASALEVEL.py          # Main Python script
├── requirements.txt     # Python dependencies
├── subject_list.txt     # Generated list of all subjects
├── downloads/           # Downloaded files organized by subject
│   ├── Biology (9700)/
│   ├── Chemistry (9701)/
│   └── ...
└── logs/                # Activity and error logs
    ├── download_activity_log_*.txt
    ├── download_failures_*.txt
    └── retry_failures_*.txt
```

## 📝 Logging

The program maintains detailed logs of all activities:

- **Activity Log**: Records all operations with timestamps
- **Failure Log**: Tracks files that failed to download
- **Retry Log**: Documents retry attempts for failed downloads

## 🔄 Batch Downloading

Subjects are automatically divided into 4 groups (approximately 20 subjects each) to make downloading manageable. You can select which group to download based on your interests.

## ⚠️ Important Notes

- This tool is designed for educational purposes only
- Be respectful of the XtremePapers website's resources
- The tool adds delays between downloads to avoid overwhelming the server
- Some antivirus software might flag the program—this is a false positive

## 🛠️ Building Executable (Optional)

To create a standalone executable:

```
pip install pyinstaller
pyinstaller --onefile ASALEVEL.py
```

The executable will be created in the `dist` directory.

## 📄 License

This project is licensed under the MIT License - see the LICENSE file for details.

## 🤝 Contributing

Contributions, issues, and feature requests are welcome! Feel free to check the issues page.

## 🙏 Acknowledgements

- [XtremePapers](https://papers.xtremepape.rs/) for hosting the past papers
- All contributors and testers who helped improve this tool

---

*Disclaimer: This tool is not affiliated with Cambridge Assessment International Education or XtremePapers.*

