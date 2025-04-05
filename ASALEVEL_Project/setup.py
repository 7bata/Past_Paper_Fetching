from setuptools import setup

APP = ['ASALEVEL.py']
DATA_FILES = []
OPTIONS = {
    'argv_emulation': True,
    'packages': ['requests', 'lxml'],
    'iconfile': None,
    'plist': {
        'CFBundleName': 'AS/A Level Papers Downloader',
        'CFBundleDisplayName': 'AS/A Level Papers Downloader',
        'CFBundleGetInfoString': 'Download Cambridge AS/A Level past papers',
        'CFBundleIdentifier': 'com.pastpapers.asalevel',
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