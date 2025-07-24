# Visual ADB

Visual ADB is a graphical Android device management system based on PySide6 and ADB. It provides a user-friendly interface for managing Android devices, installing APKs, capturing screenshots, managing files, executing commands, viewing logs, and wireless projection.

## Features
- Device connection and management (USB & wireless)
- Device information display
- File manager for Android devices
- APK installation and management
- Command terminal for ADB shell
- Log record viewing
- Screen capture
- Wireless projection (requires scrcpy)

## Requirements
- **Python 3.9** (other versions may not be compatible)
- Android Debug Bridge (ADB) installed and added to your system PATH
- PySide6
- qfluentwidgets
- scrcpy-client (for wireless projection)
- av==9.2.0 (for scrcpy-client compatibility)

## Installation
1. Install Python 3.9 from the official website.
2. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```
   Or install manually:
   ```bash
   pip install PySide6 qfluentwidgets av==9.2.0 scrcpy-client
   ```
3. Make sure ADB is installed and accessible from the command line.

## Usage
Run the main application:
```bash
python demo.py
```

## Notes
- Wireless projection requires `scrcpy-client` and a compatible version of `av` (9.2.0). Newer versions of `av` are not supported by `scrcpy-client`.
- If you encounter issues with dependencies, please check your Python version and ensure all required packages are installed.

## License
MIT 
