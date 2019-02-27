"""
This is a setup.py script generated by py2applet

Usage:
    python setup.py py2app
"""

from setuptools import setup
from glob import glob
import syncplay

APP = ['syncplayClient.py']
DATA_FILES = [
    ('resources', glob('resources/*.png') + glob('resources/*.rtf') + glob('resources/*.lua')),
    ('resources/lua/intf', glob('resources/lua/intf/*.lua'))
]
OPTIONS = {
    'iconfile': 'resources/icon.icns',
    'extra_scripts': 'syncplayServer.py',
    'includes': {'PySide.QtCore', 'PySide.QtUiTools', 'PySide.QtGui', 'PySide.QtWidgets', 'certifi', 'cffi'},
    'plist': {
        'CFBundleName': 'Syncplay',
        'CFBundleShortVersionString': syncplay.version,
        'CFBundleIdentifier': 'pl.syncplay.Syncplay',
        'LSMinimumSystemVersion': '10.6.8',
        'LSMaximumSystemVersion': '10.11.6',
        'NSHumanReadableCopyright': 'Copyright © 2019 Syncplay All Rights Reserved'
    }
}

setup(
    app=APP,
    name='Syncplay',
    data_files=DATA_FILES,
    options={'py2app': OPTIONS},
    setup_requires=['py2app'],
)
