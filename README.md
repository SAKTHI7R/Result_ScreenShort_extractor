# Result Extractor using Selenium

## Overview
The **Result Extractor** is a Flask-based automation tool that uses Selenium to extract results from a given website. It processes data from an uploaded Excel file, automates input filling, captures screenshots of results, and presents them in a user-friendly interface.

## Features
- Automates result checking via Selenium
- Supports batch processing using Excel uploads
- Captures and saves screenshots of extracted results
- Provides a Flask-based web interface
- Supports CAPTCHA handling (manual entry required)

## Prerequisites
Ensure you have the following installed before running the script:
- Python (>= 3.7)
- Flask
- Selenium WebDriver
- Google Chrome / Firefox (and corresponding WebDriver)
- Pandas
- OpenPyXL (for Excel file handling)

## Installation
1. Clone the repository:
   ```sh
   git clone https://github.com/SAKTHI7R/Result_ScreenShort_extractor
   cd Result_ScreenShort_extractor
   ```
2. Install dependencies:
   ```sh
   pip install -r requirement.txt
   ```
3. Download and place the appropriate WebDriver (ChromeDriver) in your system path.

## Usage
1. Start the Flask application:
   ```sh
   python app.py
   ```
2. Open a browser and go to `http://127.0.0.1:5000/`
3. Upload an Excel file containing `Register No` and `DOB` columns.
4. Enter the result page URL and submit button ID.
5. Important: Ensure that the CSS selectors (id attributes) for input fields and CAPTCHA on the result website match the ones used in app.py. If they differ, inspect the website and replace them accordingly.
6. View extracted results along with their screenshots.

## Configuration
use this column header "Register No" & "DOB"
Ensure that the Excel file contains the required columns:
```plaintext
| Register No | DOB        |
|------------|------------|
| 12345678   | 01-01-2000 |
| 87654321   | 15-05-1998 |
```
- The **DOB** format can be `dd-mm-yyyy` or `dd/mm/yyyy`.
- Screenshots will be saved in `static/screenshots/`.

## Contributing
Feel free to fork this repository and submit pull requests to improve the functionality or add new features.



