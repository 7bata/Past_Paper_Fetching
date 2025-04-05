from setuptools import setup

APP = ['IB.py']
DATA_FILES = []
OPTIONS = {
    'argv_emulation': True,
    'packages': ['requests', 'lxml'],
    'iconfile': None,
    'plist': {
        'CFBundleName': 'IB Papers Downloader',
        'CFBundleDisplayName': 'IB Papers Downloader',
        'CFBundleGetInfoString': 'Download IB past papers',
        'CFBundleIdentifier': 'com.pastpapers.ib',
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