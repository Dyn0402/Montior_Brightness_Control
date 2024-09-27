#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on September 27 1:36 PM 2024
Created in PyCharm
Created as Montior_Brightness_Control/build_executable.py

@author: Dylan Neff, Dylan
"""

import subprocess
import os


def main():
    build_executable('MonitorBrightnessControl.py', 'monitor_brightness_icon.ico')
    print('donzo')


def build_executable(script_name, icon_path=None):
    # Ensure the script exists
    if not os.path.isfile(script_name):
        print(f"Error: {script_name} not found.")
        return

    # Basic PyInstaller command
    pyinstaller_command = [
        'pyinstaller',
        '--onefile',         # Create a single executable
        '--windowed',        # No console window for GUI apps
        script_name          # The Python script to convert to an executable
    ]

    # If an icon path is provided, add the --icon option
    if icon_path and os.path.isfile(icon_path):
        pyinstaller_command.insert(-1, f'--icon={icon_path}')
    elif icon_path:
        print(f"Warning: Icon file '{icon_path}' not found. Proceeding without custom icon.")

    try:
        # Run the PyInstaller command
        subprocess.run(pyinstaller_command, check=True)
        print("Executable built successfully.")
    except subprocess.CalledProcessError as e:
        print(f"Error: Failed to build executable. {e}")
    except FileNotFoundError:
        print("Error: PyInstaller is not installed. Please install it using 'pip install pyinstaller'.")


if __name__ == '__main__':
    main()
