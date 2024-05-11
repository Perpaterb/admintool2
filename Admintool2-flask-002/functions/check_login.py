from flask import Blueprint
from selenium.webdriver.common.by import By
check_login = Blueprint('check_login', __name__)
from flask import g 

@check_login.route('/check_login', methods=['POST'])
def check_login_func():
    driver = g.driver
    print("running /check_login")
    browser = driver.get_browser()
    try:
        logo_img = browser.find_element(By.CSS_SELECTOR, 'img.logo[alt="University of Technology Sydney logo"]')
        print("you are logged in")
        return {"status": "you are logged in"}, 200
    except Exception as e: 
        print(f"Error occurred: {e}")
        print("you are not logged in - please login")
        return {"status": "you are not logged in - please login"}, 200
