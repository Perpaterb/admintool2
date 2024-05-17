from flask import Blueprint
from flask import g
open_or_alert = Blueprint('open_or_alert', __name__)

@open_or_alert.route('/open_or_alert', methods=['POST'])
def open_or_alert_func():
    driver = g.driver
    print("running /open_or_alert")
    try:
        url = 'https://login.uts.edu.au'
        browser = driver.get_browser()
        browser.set_window_size(1024, 768)
        if browser and isinstance(url, str):
            if 'login.uts.edu.au' in browser.current_url:
                browser.execute_script("alert('Here I am');")
            else:
                browser.get(url)
            return "handled", 200
        else:
            return "Invalid browser instance or URL", 500
    except Exception as e:
        print(f"Exception occurred: {e}")  
        return "An error occurred", 500
