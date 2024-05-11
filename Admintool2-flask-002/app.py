from flask import Flask
from flask import request
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
from flask_cors import CORS

app = Flask(__name__)
CORS(app, resources={r"/*": {"origins": "http://localhost:3000"}})

class SeleniumDriver:
    def __init__(self):
        options = Options()
        self.browser = None

    def get_browser(self):
        if self.browser is None:
            self.browser = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
        return self.browser

    def close_browser_session(self):
        if self.browser is not None:
            self.browser.quit()
            self.browser = None

driver =  SeleniumDriver()

@app.route('/open_or_alert', methods=['POST'])
def open_or_alert():
    print("running /open_or_alert")
    try:
        url = 'https://login.uts.edu.au'
        browser = driver.get_browser()
        if browser and isinstance(url, str):
            if 'login.uts.edu.au' in browser.current_url:
                browser.execute_script("alert('Here I am');")
            else:
                browser.get(url)
            return "handled", 200
        else:
            return "Invalid browser instance or URL", 500
    except Exception as e:
        print(f"Exception occurred: {e}")  # this will log the error
        return "An error occurred", 500


@app.route('/close', methods=['POST'])
def close_browser_session():
    print("running /close")
    driver.close_browser_session()
    return "closed", 200

@app.route('/force_close', methods=['POST'])
def close_browser():
    print("running /force_close")
    try:
        browser = driver.get_browser()  # get the current browser instance
        browser.quit()
        return "Browser closed successfully", 200
    except Exception as e:
        print(f"Exception occurred: {e}")  # log the error
        return "An error occurred", 500

## Check the login to login.uts.edu.au
@app.route('/check_login', methods=['POST'])
def check_login():
    print("running /check_login")
    # Assuming `driver` is your WebDriver instance
    browser = driver.get_browser()
    try:
        # Use the find_element method with the By.CSS_SELECTOR locator
        logo_img = browser.find_element(By.CSS_SELECTOR, 'img.logo[alt="University of Technology Sydney logo"]')
        print("you are logged in")
        return {"status": "you are logged in"}, 200
    except Exception as e: 
        print(f"Error occurred: {e}")
        print("you are not logged in - please login")
        return {"status": "you are not logged in - please login"}, 200




if __name__ == "__main__":
    app.run(port=5000)
