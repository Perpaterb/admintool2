from flask import Flask
from flask import request
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
from flask_cors import CORS
from functions.check_login import check_login
from functions.force_close import force_close
from functions.open_or_alert import open_or_alert
from functions.login import login
from functions.open_sp import open_sp
from flask import g

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

@app.before_request
def before_request_func():
    g.driver = driver

app.register_blueprint(check_login)
app.register_blueprint(force_close)
app.register_blueprint(open_or_alert)
app.register_blueprint(login)
app.register_blueprint(open_sp)

@app.route('/close', methods=['POST'])
def close_browser_session():
    print("running /close")
    driver.close_browser_session()
    return "closed", 200

if __name__ == "__main__":
    app.run(port=5000)
