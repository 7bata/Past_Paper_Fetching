# Building and Running Standalone Applications on Mac

## Build Steps

### 1. Preparation
Make sure Python 3 is installed on your Mac. Open Terminal and run the following command to check:
```bash
python3 --version
```

### 2. Install Necessary Tools
```bash
# Install project dependencies
pip3 install requests lxml

# Install py2app (Mac-specific packaging tool)
pip3 install py2app
```

### 3. Build AS and A Level Downloader
```bash
# Navigate to ASALEVEL_Project directory
cd ASALEVEL_Project

# Build the application
python3 setup.py py2app
```
After building, the application will be located in the `dist` folder, named `ASALEVEL.app`.

### 4. Build IGCSE Downloader
```bash
# Navigate to IGCSE_Project directory
cd ../IGCSE_Project

# Build the application
python3 setup.py py2app
```
After building, the application will be located in the `dist` folder, named `IGCSE.app`.

### 5. Build Edexcel Downloader
```bash
# Navigate to Edexcel_Project directory
cd ../Edexcel_Project

# Build the application
python3 setup.py py2app
```
After building, the application will be located in the `dist` folder, named `Edexcel.app`.

### 6. Build IB Downloader
```bash
# Navigate to IB_Project directory
cd ../IB_Project

# Build the application
python3 setup.py py2app
```
After building, the application will be located in the `dist` folder, named `IB.app`.

## Using the Applications

1. Open the corresponding `dist` folder in Finder.
2. Double-click the `.app` file to run the application.
3. Follow the prompts to select download options:
   - ASALEVEL/IGCSE: Select subject groups to download
   - Edexcel: Select examination category groups to download
   - IB: Select examination session groups to download
4. Files will be downloaded to the `downloads` folder created by the application.

## Troubleshooting

- If you encounter an "Unidentified Developer" warning, hold the Control key and click the application icon, then select "Open".
- If the application fails to start, try running it from Terminal using the following command:
  ```bash
  open -a /path/to/your/app
  ```
- Downloading large numbers of files may take a significant amount of time. Please be patient.
- If errors occur during the download process, check the log files in the `logs` folder for detailed information.

## Notes

- The applications will create `downloads` and `logs` folders in the current directory.
- Downloaded files will be organized according to the original website directory structure.
- Please respect exam website resources by avoiding frequent downloads.
- Each project has slightly different download logic:
  - ASALEVEL/IGCSE: Organized by subject
  - Edexcel: Organized by examination category
  - IB: Organized by examination session 