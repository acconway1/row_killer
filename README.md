# row_killer: an Excel Row Cleaner

## Overview
row_killer is a Python script designed to efficiently clean Excel files by removing all blank rows from each worksheet. This tool is particularly useful for preprocessing Excel files before analysis or distribution.

## Features
- Processes all worksheets within an Excel workbook.
- Generates a new Excel file with "_no_blanks.xlsx" appended to the original filename.
- Ensures the original Excel file remains unchanged.

## Requirements
- Python 3
- Libraries: pandas, openpyxl, numpy, et-xmlfile, python-dateutil, pytz, six, tzdata

## Installation
1. Clone the repository or download the source code.
2. Navigate to the project directory and create a virtual environment: `python -m venv .venv`
4. Activate the virtual environment:
- Windows: `.venv\Scripts\activate`
- Linux/macOS: `source .venv/bin/activate`
4. Install the required dependencies: `pip install -r requirements.txt`

## Usage
1. Run the script with Python: `python main.py`
2. When prompted, enter the full path to your Excel file.
3. The script will process the file and create a new Excel file in the same directory without blank rows.

## Contributions
Contributions are welcome! Please feel free to submit pull requests or open issues for any bugs or feature requests.

## License
MIT License
