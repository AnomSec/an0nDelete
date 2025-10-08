# An0nDelete

![Python](https://img.shields.io/badge/python-3.6+-blue.svg)
![License](https://img.shields.io/badge/license-MIT-green.svg)
![Security](https://img.shields.io/badge/security-file%20wiper-red.svg)

A secure file and directory deletion tool that overwrites data multiple times before removal, ensuring sensitive files cannot be recovered.

## 🚀 Features

- **Secure File Deletion**: Overwrite files with multiple passes before deletion
- **Directory Recursion**: Securely delete entire directory structures
- **Customizable Passes**: Configure the number of overwrite passes (default: 3)
- **Safety Checks**: Automatic validation of files and directories before operations
- **Cross-Platform**: Works on Windows, Linux, and macOS

## 📦 Installation

### Prerequisites
- Python 3.6 or higher
- pip package manager

### Clone the Repository
```bash
git clone https://github.com/AnomSec/an0nDelete.git
cd an0nDelete
```
### Usage
```bash
python main.py [-h] [-f FILE] [-d DIR] [-p PASSES]
```
