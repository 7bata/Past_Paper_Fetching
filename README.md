# Cambridge Past Papers Download Toolkit

[![License: MIT](https://img.shields.io/badge/License-MIT-blue.svg)](https://opensource.org/licenses/MIT)

This repository contains two powerful tools for downloading Cambridge Assessment International Education (CAIE) past exam papers:
- **ASALEVEL_Project**: Specifically designed for AS and A Level papers
- **IGCSE_Project**: Specifically designed for IGCSE papers

## 📖 Overview

These tools help students and educators quickly download organized collections of past exam papers without manual navigation through the website. Both tools provide:

- Automatic scraping of all available subjects
- Batch downloading of papers grouped by subject
- Organized file storage following subject hierarchy
- Detailed activity logging and failure tracking
- Ability to resume failed downloads

## 🗂️ Project Structure

```plaintext
PastPapers/
├── ASALEVEL_Project/
│   ├── ASALEVEL.py         # AS and A Level download script
│   ├── requirements.txt    # List of dependencies
│   ├── README.md           # Project documentation
│   ├── subject_list.txt    # Retrieved subject list
│   ├── logs/               # Log files folder
│   ├── build/              # PyInstaller build files
│   └── dist/               # Executable directory
│
└── IGCSE_Project/
    ├── IGCSE.py            # IGCSE download script
    ├── requirements.txt    # List of dependencies
    ├── README.md           # Project documentation
    ├── subject_list.txt    # Retrieved subject list
    ├── logs/               # Log files folder
    └── dist/               # Executable directory
```

## ✨ Common Features

Both tools offer the following powerful capabilities:

- **Subject Organization**: Automatically groups 80+ (AS/A Level) or 100+ (IGCSE) subjects into manageable batches
- **Smart Directory Structure**: Creates folders by subject name and preserves subfolder structure
- **Efficient Batch Processing**: Downloads all files in a subject group with a single command
- **Comprehensive Logging**: Records all activity with timestamps for tracking
- **Error Handling**: Tracks failed downloads and provides retry functionality
- **File Skipping**: Avoids re-downloading existing files to save time and bandwidth
- **Executable Support**: Provides packaged .exe files that don't require Python installation

## 🚀 Usage

### AS and A Level Downloader

1. Run the executable:
   - Open the `ASALEVEL_Project/dist` folder
   - Double-click `ASALEVEL.exe`
   
   Or run from source:
   ```shell
   cd ASALEVEL_Project
   pip install -r requirements.txt
   python ASALEVEL.py
   ```

2. The program will fetch and group all available subjects
3. Choose option 1 to download a subject group
4. Select which group (1-4) you want to download
5. The program will automatically download all files, organizing them by subject
6. All activity is logged to the `logs` directory
7. If any files fail to download, use option 2 to retry those specific files

### IGCSE Downloader

1. Run the executable:
   - Open the `IGCSE_Project/dist` folder
   - Double-click `IGCSE.exe`
   
   Or run from source:
   ```shell
   cd IGCSE_Project
   pip install -r requirements.txt
   python IGCSE.py
   ```

2. Operation steps are the same as the AS/A Level downloader

## 📝 Logging

The program maintains detailed logs of all activities:

- **Activity Log**: Records all operations with timestamps
- **Failure Log**: Tracks files that failed to download
- **Retry Log**: Documents retry attempts for failed downloads

## 🔄 Batch Downloading

Subjects are automatically divided into 4 groups (approximately 20-25 subjects each) to make downloading manageable. You can select which group to download based on your interests.

## 🛠️ Building Executables

Both projects already include pre-built executables. If you want to build them yourself:

```shell
pip install pyinstaller
cd ASALEVEL_Project    # or cd IGCSE_Project
pyinstaller --onefile ASALEVEL.py    # or pyinstaller --onefile IGCSE.py
```

The executable will be created in the `dist` directory.

## ⚠️ Important Notes

- These tools are designed for educational purposes only
- Be respectful of the XtremePapers website's resources
- The tools add delays between downloads to avoid overwhelming the server
- Some antivirus software might flag the programs—this is a false positive

## 📄 License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## 🙏 Acknowledgements

- [XtremePapers](https://papers.xtremepape.rs/) for hosting the past papers
- All contributors and testers who helped improve these tools

---

*Disclaimer: These tools are not affiliated with Cambridge Assessment International Education or XtremePapers.*
```
