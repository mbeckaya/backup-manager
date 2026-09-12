# Backup Manager

A lightweight automation tool for creating, organizing, and logging directory backups.

---

## Features

* Automated directory backups
* Timestamped backup folders
* Configurable source and backup directories
* Copies configured files and directories
* Logs backup events with timestamps
* Basic error handling
* Simple and lightweight automation workflow

---

## Project Status

✅ Completed

The backup automation script is fully functional and demonstrates how Python can be used to automate repetitive file management and backup tasks.

Current functionality includes:

* Directory backup creation
* Backup folder organization
* Process logging
* Error handling for file operations

---

## Getting Started

### Requirements

* Python 3.x installed

### Configuration

Configure the source and backup directories in `main.py`.

Example:

```python
source = r"C:/Source"

destination = (
    "D:/",
    "E:/",
)
```

### Run the Script

```bash
python main.py
```

---

## Backup Process

The script follows a simple automation workflow:

1. Loads the configured source and backup paths
2. Creates a new timestamped backup folder
3. Copies configured directories to the backup location
4. Logs the backup process with timestamps
5. Handles possible file operation errors

---

## Technologies

* Python 3
* File System Automation
* Directory Management
* Logging
* Error Handling

---

## Purpose

This project demonstrates how Python can be used to automate repetitive file management tasks.

It was created as a practical example of a lightweight automation workflow using Python, with a focus on file system operations, configurable paths, timestamp handling, logging, and error handling.