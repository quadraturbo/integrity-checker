# File Integrity Checker v2

![Python Version](https://img.shields.io/badge/python-3.x-blue.svg)
![License](https://img.shields.io/badge/license-GPL%203.0-green.svg)
![Platform](https://img.shields.io/badge/platform-Windows%20%7C%20Linux-lightgrey.svg)
![Status](https://img.shields.io/badge/status-stable-brightgreen.svg)

A Python script to verify file integrity using SHA-256 hash, compatible with Windows and Linux.

## Description

`int_checkerv2.py` is a command-line tool that allows you to compare two files to determine if they have been modified. It uses the SHA-256 algorithm to calculate and compare file hashes, providing a reliable way to detect any changes in their content.

### Note
While using this tool ,ensure to add the extensions of the files to compare.

## Features

- **Cross-platform**: Works on Windows and Linux
- **Interactive interface**: User-friendly menu that guides you step by step
- **Automatic detection**: Uses native operating system tools
  - Windows: `certutil`
  - Linux: `sha256sum`
- **Accurate verification**: Compares files using SHA-256 hash
- **Error handling**: Path validation and error management via sanitization
- **Clear messages**: Explicitly indicates whether files are identical or have been modified

## Requirements

- Python 3.x
- **Windows**: `certutil` (included by default)
- **Linux**: `sha256sum` (included in most distributions)

## Installation

1. Clone this repository:
```bash
git clone https://github.com/quadraturbo/file-integrity-checker.git
cd file-integrity-checker
```

2. No external dependencies required, only Python 3.

## Usage

Run the script from the terminal:

```bash
python int_checkerv2.py
```

The program will guide you through the following steps:

1. Select your operating system (Windows or Linux)
2. Enter the path of the original file
3. Enter the path of the file to compare
4. The script will calculate the hashes and display the result

### Usage Example

```
=== File Integrity Checker ===

Select your operating system:
1. Windows
2. Linux
Option: 1

Enter the path of the original file: C:\documents\original_file.pdf
Enter the path of the file to compare: C:\downloads\downloaded_file.pdf

Calculating hashes...

The files are identical. They have not been modified.
```

## How It Works

The script performs the following steps:

1. Asks the user to select their operating system
2. Receives the paths of the two files to compare
3. Executes the native system command to calculate the SHA-256 hash:
   - Windows: `certutil -hashfile <file> SHA256`
   - Linux: `sha256sum <file>`
4. Compares both hashes
5. Displays the result indicating whether the files are identical or have been modified

## Future Improvements

This project can be expanded with the following features:

- macOS support
- Verification of multiple files simultaneously
- Support for other hash algorithms (MD5, SHA-1, SHA-512)
- Export results to log file
- Graphical User Interface (GUI)
- Batch mode for mass processing
- Report generation in PDF/HTML format

## Contributing

This is a personal practice project, but contributions are welcome. If you want to improve the code:

1. Fork the project
2. Create a branch for your feature (`git checkout -b feature/new-feature`)
3. Commit your changes (`git commit -am 'Add new feature'`)
4. Push to the branch (`git push origin feature/new-feature`)
5. Open a Pull Request

## License

This project is licensed under the GPL 3.0 License. See the `LICENSE` file for more details.

## Author

Personal practice project to learn:
- Managing `subprocess` in Python
- Implementing hashing and integrity verification
- Cross-platform file path handling
- Clean code best practices

## Notes

- Make sure you have read permissions on the files you want to verify
- File paths must be valid absolute or relative paths
- The script does not modify files, it only reads their content to calculate the hash

---

**Found this project useful?** Give it a star on GitHub
