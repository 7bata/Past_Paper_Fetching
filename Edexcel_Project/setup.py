from setuptools import setup

APP = ['Edexcel.py']
DATA_FILES = []
OPTIONS = {
    'argv_emulation': True,
    'packages': ['requests', 'lxml'],
    'iconfile': None,
    'plist': {
        'CFBundleName': 'Edexcel Papers Downloader',
        'CFBundleDisplayName': 'Edexcel Papers Downloader',
        'CFBundleGetInfoString': 'Download Edexcel past papers',
        'CFBundleIdentifier': 'com.pastpapers.edexcel',
        'CFBundleVersion': '1.0.0',
        'CFBundleShortVersionString': '1.0.0',
        'NSHumanReadableCopyright': 'Copyright © 2023, Your Name, All Rights Reserved'
    }
}

setup(
    app=APP,
    data_files=DATA_FILES,
    options={'py2app': OPTIONS},
    setup_requires=['py2app'],
) 