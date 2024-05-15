from flask import Blueprint, request, jsonify, g
from Crypto.Cipher import AES
from Crypto.Util.Padding import unpad
from base64 import b64decode
import os
from selenium import webdriver
from dotenv import load_dotenv
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.keys import Keys

open_sp = Blueprint('open_sp', __name__)

@open_sp.route('/open_sp', methods=['POST'])
def open_sp_func():

    driver = g.driver
    browser = driver.get_browser()

    user_id = request.json.get('user_id')

    browser.execute_script("window.open('');")
    browser.switch_to.window(browser.window_handles[-1])
    browser.get("https://identix.itu.uts.edu.au/identityiq/home.jsf")
    wait = WebDriverWait(browser, 10)  # Wait up to 10 seconds
    uts_icon = wait.until(EC.visibility_of_element_located((By.XPATH, '//img[@role="presentation"]')))
    browser.get("https://identix.itu.uts.edu.au/identityiq/define/identity/identities.jsf")
    
    wait = WebDriverWait(browser, 10)  # Wait up to 10 seconds
    input_field = wait.until(EC.visibility_of_element_located((By.ID, 'searchfield-1041-inputEl')))
    input_field.send_keys(user_id)
    input_field.send_keys(Keys.RETURN)

    # Finding 
    wait = WebDriverWait(browser, 10)  # Wait up to 10 seconds
    element = wait.until(EC.element_to_be_clickable((By.XPATH, '//div[text()="020144"]')))
    element.click()


    
    
    return jsonify(status="Opening SailPoint"), 200
