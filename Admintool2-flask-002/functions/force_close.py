from flask import Blueprint
from flask import g
force_close = Blueprint('force_close', __name__)

@force_close.route('/force_close', methods=['POST'])
def close_browser():
    driver = g.driver
    print("running /force_close")
    try:
        browser = driver.get_browser() 
        browser.quit()
        return "Browser closed successfully", 200
    except Exception as e:
        print(f"Exception occurred: {e}")  
        return "An error occurred", 500
