

---

# Result Extractor using Selenium 🤖📸

## Overview

The **Result Extractor** is a **Flask-based automation tool** that leverages **Selenium** to extract results from a specified website. It supports processing bulk data using an uploaded **Excel file** 📊, automates form filling ✍️, captures **screenshots** of results 📸, and presents them in a simple web interface 💻.

### Key Features:
- Automates result checking via **Selenium** 🤖
- **Batch processing** using Excel file uploads 📤
- **Screenshot capture** for each result 📸
- **Flask-based web interface** for easy interaction 🌐
- **Manual CAPTCHA entry** support (if required) 🔒

---

## Prerequisites ⚙️

Before you begin, ensure the following tools are installed on your machine:

- **Python** (>= 3.7) 🐍
- **Flask**: Lightweight web framework 🖥️
- **Selenium WebDriver**: For automating browser interaction 🧑‍💻
- **Google Chrome** or **Firefox** (and the corresponding WebDriver) 🌍
- **Pandas**: For Excel file handling 📊
- **OpenPyXL**: To read Excel files 📖

---

## Installation Steps 🔧

### 1. Clone the Repository

```bash
git clone https://github.com/SAKTHI7R/Result_ScreenShort_extractor
cd Result_ScreenShort_extractor
```

### 2. Install Dependencies

Install the required libraries using **pip**:

```bash
pip install -r requirements.txt
```

### 3. Download the WebDriver

- Download the **ChromeDriver** or **GeckoDriver** (for Firefox) compatible with your browser version.
- Place the WebDriver executable in your system path.

---

## File Structure 📂

Here's the project file structure to help you navigate through the directory:

```plaintext
Result_ScreenShort_extractor/
├── app.py                     # Main Flask application file
├── requirements.txt           # Python dependencies
├── static/
│   ├── screenshots/           # Folder to store screenshots of results
│   └── uploads/               # Optional: Custom CSS files for styling (if applicable)
├── templates/
│   └── index.html
│   └── results.html           # The HTML template for the web interface
└── LICENSE                    # License information
```

### Key Files and Directories:
- **app.py**: The main Python file that runs the Flask server and handles the automation logic.
- **requirements.txt**: Contains the list of dependencies (e.g., Flask, Selenium, Pandas, etc.).
- **static/screenshots/**: Directory where the screenshots of the extracted results will be stored.
- **templates/index.html**: The HTML template for the user interface where you can upload Excel files and view the results.
- **result_data.xlsx**: Sample Excel file to use for testing (this should be replaced with your own data).
- **README.md**: This documentation file.
- **LICENSE**: License for the project.

---

## Usage 🚀

### 1. Start the Flask Application

Run the Flask app to start the web server:

```bash
python app.py
```

### 2. Open the Web Interface

- Open your browser and visit: `http://127.0.0.1:5000/` 🌐

### 3. Upload Your Excel File 📤

The Excel file should contain the following columns:

- **Register No** 🆔
- **DOB** (Date of Birth) 🎂

```plaintext
| Register No | DOB        |
|-------------|------------|
| 12345678    | 01-01-2000 |
| 87654321    | 15-05-1998 |
```

> **Note**: The **DOB** can be in `dd-mm-yyyy` or `dd/mm/yyyy` format.

### 4. Enter Required Details

- **Result page URL** 🌍: Provide the URL where results are displayed.
- **Submit button ID** 🔘: Enter the ID of the submit button to trigger the search.

### 5. View the Extracted Results 📝

- After processing, results along with their screenshots will be displayed on the webpage.
- Screenshots will be saved in the `static/screenshots/` directory 📂.

---

## Configuration Details ⚙️

Ensure that the Excel file you upload has the exact column headers:

| **Register No** | **DOB**      |
|-----------------|--------------|
| 12345678        | 01-01-2000   |
| 87654321        | 15-05-1998   |

### Web Element Configuration 🕹️

- **CSS Selectors**: The CSS selectors for the input fields and CAPTCHA elements must be configured correctly in `app.py`.
- **CAPTCHA Handling**: If the website requires CAPTCHA solving, you must enter it manually when prompted 🧩.

---

## Screenshots and Output 📸

- After successful extraction, you’ll see results along with screenshots for each query.
- Screenshots will be saved in the `static/screenshots/` folder 🗂️.


## Contributing 🤝

We welcome contributions to enhance this project. Feel free to fork the repository and submit pull requests to improve the functionality or add new features. 🌟

---

## Troubleshooting 🛠️

- **Problem**: The web page doesn't load correctly or the elements are not found.
  - **Solution**: Ensure the CSS selectors (input fields, CAPTCHA, etc.) match the elements on the website you're targeting. You can inspect elements in your browser's developer tools 🔍.

---
