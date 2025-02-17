import datetime
import re
from flask import Flask, render_template, request, redirect, url_for, flash
import pandas as pd
from selenium import webdriver
from selenium.webdriver.common.by import By
import os
import time
from werkzeug.utils import secure_filename
from selenium.webdriver.chrome.options import Options

app = Flask(__name__)
app.config["UPLOAD_FOLDER"] = "static/uploads"
app.secret_key = "supersecretkey"

# Ensure Upload & Screenshot folders exist
os.makedirs(app.config["UPLOAD_FOLDER"], exist_ok=True)
SCREENSHOT_FOLDER = os.path.join(app.root_path, "static", "screenshots")
os.makedirs(SCREENSHOT_FOLDER, exist_ok=True)


# Function to automate result checking
def automate_result_check(register_number, dob, result_page_url, submit_button_id):
    chrome_options = Options()
    chrome_options.add_argument("--headless")  # Run in headless mode

    driver = webdriver.Chrome(options=chrome_options)

    try:
        driver.get(result_page_url)

        # Locate input fields
        register_number_field = driver.find_element(By.ID, "txtRollNo")
        dob_field = driver.find_element(By.ID, "txtDoB")

        # Clear fields and enter values
        register_number_field.clear()
        dob_field.clear()

        if isinstance(dob, datetime):

            # If dob is a datetime object, convert to the required format
            dob_str = dob.strftime("%d/%m/%Y")
        else:
            # If dob is a string, check if it's already in the required format
            if re.match(r"^\d{2}/\d{2}/\d{4}$", dob):
                # It's already in dd/mm/yyyy format
                dob_str = dob
            else:
                # If the format is not dd/mm/yyyy, replace - with / and format
                dob_str = datetime.strptime(dob, "%d-%m-%Y").strftime("%d/%m/%Y")

        register_number_field.send_keys(register_number)
        dob_field.send_keys(dob_str)

        # Handle CAPTCHA manually
        cap_ele = driver.find_element(By.ID, "mainCaptcha")
        cap_inp_ele = driver.find_element(By.ID, "txtInput")
        cap_inp_ele.clear()
        cap_inp_ele.send_keys(cap_ele.text)

        # Click Submit
        submit_button = driver.find_element(By.ID, submit_button_id)
        submit_button.click()
        time.sleep(2)

        # Adjust view for screenshot
        driver.execute_script("window.scrollTo(0, 800);")
        time.sleep(2)

        # Save Screenshot
        screenshot_filename = f"result_{register_number}.png"
        screenshot_path = os.path.join(SCREENSHOT_FOLDER, screenshot_filename)
        driver.save_screenshot(screenshot_path)

        return screenshot_filename  # Only return filename, not full path

    except Exception as e:
        return None

    finally:
        driver.quit()


# Home Page - Upload Form
@app.route("/", methods=["GET", "POST"])
def index():
    results = []
    if request.method == "POST":
        if "file" not in request.files:
            flash("No file part")
            return redirect(request.url)

        file = request.files["file"]
        result_page_url = request.form.get("result_page_url")
        submit_button_id = request.form.get("submit_button_id")

        if file.filename == "":
            flash("No selected file")
            return redirect(request.url)

        if file:
            filename = secure_filename(file.filename)
            file_path = os.path.join(app.config["UPLOAD_FOLDER"], filename)
            file.save(file_path)

            # Read Excel file
            df = pd.read_excel(file_path)

            for _, row in df.iterrows():
                register_number = row["Register No"]
                dob = row["DOB"]

                # Process each entry
                screenshot_filename = automate_result_check(
                    register_number, dob, result_page_url, submit_button_id
                )

                results.append(
                    {
                        "register_number": register_number,
                        "screenshot": screenshot_filename,
                    }
                )

            return render_template("results.html", results=results)

    return render_template("index.html", results=results)


if __name__ == "__main__":
    app.run(debug=True)
