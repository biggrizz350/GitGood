# GitGood

A simple Python-based Git practice environment built using Tkinter. This application simulates Git commands in a PowerShell-like interface to help users practice Git workflows without affecting real repositories.

## Features
- Simulates common Git commands: `init`, `add`, `commit`, `push`, `pull`, `merge`, `rebase`, `status`, `stash`, `branch`, `checkout`.
- Displays output in a PowerShell-styled terminal.
- Allows users to practice Git commands in a safe environment.
- Includes a `git quizzed` command to test Git knowledge.

## Installation
### Prerequisites
Ensure you have Python installed on your system. You can download it from [python.org](https://www.python.org/).

### Clone the Repository
```sh
git clone https://github.com/yourusername/GitGood.git
cd GitGood
```

### Install Dependencies
This project primarily uses Tkinter, which comes pre-installed with Python, but you may want to ensure all required modules are installed:
```sh
pip install -r requirements.txt  # If additional dependencies are added
```

### Run the Application
```sh
python main.py
```

## Creating an Executable (Windows)
If you want to create a standalone `.exe` file, use PyInstaller:
```sh
pyinstaller --onefile --windowed --clean main.py
```
The `.exe` file will be generated in the `dist/` folder.

## Usage
The terminal starts with the prompt:
```sh
PS C:\Users\User>
```
You can type and execute simulated Git commands. Example usage:
```sh
git init my_project
git add file.txt
git commit -m "Initial commit"
git status
git push
git quizzed  # Tests Git knowledge
```

## Troubleshooting
### Windows Defender Blocks the Executable
If Windows Defender detects a false positive:
1. Open **Windows Security**.
2. Go to **Virus & threat protection** → **Manage settings**.
3. Temporarily **turn off real-time protection**.
4. Add the `dist/` folder to Windows Defender **exclusions**.

### Executable Gets Deleted Automatically
If the `.exe` disappears, it may be due to Windows Defender. Try rebuilding with:
```sh
pyinstaller --onefile --clean main.py
```
Then manually add an exception for the `dist/` folder.


