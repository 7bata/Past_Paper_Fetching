# Cambridge Past Papers Download Toolkit

[![License: MIT](https://img.shields.io/badge/License-MIT-blue.svg)](https://opensource.org/licenses/MIT)

This repository contains four powerful tools for downloading past exam papers from multiple examination boards:
- **ASALEVEL_Project**: Specifically designed for Cambridge AS and A Level papers
- **IGCSE_Project**: Specifically designed for Cambridge IGCSE papers
- **Edexcel_Project**: Specifically designed for Edexcel exam papers
- **IB_Project**: Specifically designed for International Baccalaureate (IB) papers

## 📖 Overview

These tools help students and educators quickly download organized collections of past exam papers without manual navigation through the website. All tools provide:

- Automatic scraping of all available subjects/categories/examination sessions
- Batch downloading of papers grouped by subject/category/examination session
- Organized file storage following original website hierarchy
- Detailed activity logging and failure tracking
- Ability to resume failed downloads

## 🗂️ Project Structure

```plaintext
Past_Paper_Fetching/
├── ASALEVEL_Project/
│   ├── ASALEVEL.py         # AS and A Level download script
│   ├── requirements.txt    # List of dependencies
│   ├── README.md           # Project documentation
│   ├── setup.py            # Mac app packaging config
│   ├── subject_list.txt    # Retrieved subject list
│   ├── logs/               # Log files folder
│   ├── build/              # PyInstaller build files
│   └── dist/               # Executable directory
│
├── IGCSE_Project/
│   ├── IGCSE.py            # IGCSE download script
│   ├── requirements.txt    # List of dependencies
│   ├── README.md           # Project documentation
│   ├── setup.py            # Mac app packaging config
│   ├── subject_list.txt    # Retrieved subject list
│   ├── logs/               # Log files folder
│   └── dist/               # Executable directory
│
├── Edexcel_Project/
│   ├── Edexcel.py          # Edexcel download script
│   ├── requirements.txt    # List of dependencies
│   ├── README.md           # Project documentation
│   ├── setup.py            # Mac app packaging config
│   ├── logs/               # Log files folder
│   ├── build/              # PyInstaller build files
│   └── dist/               # Executable directory
│
├── IB_Project/
│   ├── IB.py               # IB download script
│   ├── requirements.txt    # List of dependencies
│   ├── README.md           # Project documentation
│   ├── setup.py            # Mac app packaging config
│   ├── session_list.txt    # Retrieved examination sessions
│   ├── logs/               # Log files folder
│   ├── build/              # PyInstaller build files
│   └── dist/               # Executable directory
│
└── MacSetup/               # Mac application build support
    ├── ASALEVEL/           # Mac setup for ASALEVEL
    ├── IGCSE/              # Mac setup for IGCSE
    └── MAC_INSTRUCTIONS.md # Instructions for Mac users
```

## ✨ Common Features

All tools offer the following powerful capabilities:

- **Smart Organization**: Automatically groups subjects/categories into manageable batches
- **Original Directory Structure**: Maintains website's folder hierarchy for easy navigation
- **Efficient Batch Processing**: Downloads all files in a group with a single command
- **Comprehensive Logging**: Records all activity with timestamps for tracking
- **Error Handling**: Tracks failed downloads and provides retry functionality
- **File Skipping**: Avoids re-downloading existing files to save time and bandwidth
- **Cross-Platform Support**: Provides Windows executables and Mac application build scripts

## 🚀 Usage

### Cambridge AS and A Level Downloader

1. Run the executable or from source:
   ```shell
   cd ASALEVEL_Project
   pip install -r requirements.txt
   python ASALEVEL.py
   ```

2. The program will fetch and group all available subjects
3. Choose option 1 to download a subject group
4. Select which group (1-4) you want to download
5. The program will automatically download all files, organizing them by subject

### Cambridge IGCSE Downloader

1. Run the executable or from source:
   ```shell
   cd IGCSE_Project
   pip install -r requirements.txt
   python IGCSE.py
   ```

2. Operation steps are the same as the AS/A Level downloader

### Edexcel Downloader

1. Run from source:
   ```shell
   cd Edexcel_Project
   pip install -r requirements.txt
   python Edexcel.py
   ```

2. The program will fetch available categories (e.g., Advanced Level, International GCSE)
3. Choose a category group to download
4. Files will be downloaded following the original website directory structure

### IB Downloader

1. Run from source:
   ```shell
   cd IB_Project
   pip install -r requirements.txt
   python IB.py
   ```

2. The program will fetch available examination sessions (2010-2023)
3. Choose a session group to download
4. Files will be downloaded maintaining the original IB directory structure

## 📝 Logging

All programs maintain detailed logs of activities:

- **Activity Log**: Records all operations with timestamps
- **Failure Log**: Tracks files that failed to download
- **Retry Log**: Documents retry attempts for failed downloads

## 🔄 Batch Downloading

Subjects/categories/sessions are automatically divided into groups to make downloading manageable. You can select which group to download based on your needs.

## 🛠️ Building Executables

### Windows (all projects)

```shell
pip install pyinstaller
cd [Project_Directory]  # ASALEVEL_Project, IGCSE_Project, Edexcel_Project, or IB_Project
pyinstaller --onefile [Script_Name].py  # ASALEVEL.py, IGCSE.py, Edexcel.py, or IB.py
```

The executable will be created in the `dist` directory.

### Mac (all projects)

```shell
pip install py2app
cd [Project_Directory]  # ASALEVEL_Project, IGCSE_Project, Edexcel_Project, or IB_Project
python setup.py py2app
```

The Mac application will be created in the `dist` directory. See `MacSetup/MAC_INSTRUCTIONS.md` for detailed instructions.

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

*Disclaimer: These tools are not affiliated with Cambridge Assessment International Education, Pearson Edexcel, International Baccalaureate Organization (IBO), or XtremePapers.*
```
