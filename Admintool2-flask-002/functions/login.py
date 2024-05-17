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

login = Blueprint('login', __name__)
load_dotenv()  # take environment variables from .env.
SECRET_KEY = os.environ.get("SECRET_KEY")

def decrypt(enc):
    enc = b64decode(enc)
    cipher = AES.new(SECRET_KEY.encode('utf-8'), AES.MODE_ECB)
    return unpad(cipher.decrypt(enc), AES.block_size)

@login.route('/login', methods=['POST'])
def login_func():
    decryptedPassword = decrypt(request.json.get('password')).decode("utf-8", "ignore")
    # print('decryptedPassword: ', decryptedPassword)
    
    decryptedEmail = decrypt(request.json.get('email')).decode("utf-8", "ignore")
    # print('decryptedEmail: ', decryptedEmail)

    driver = g.driver
    browser = driver.get_browser()

    # Finding the input with type="text" and entering the email
    email_input = browser.find_element(By.CSS_SELECTOR, 'input[type="text"]')
    email_input.send_keys(decryptedEmail)

    # Finding the submit button and clicking it
    submit_button = browser.find_element(By.CSS_SELECTOR, 'input[type="submit"][value="Next"]')
    submit_button.click()

    # Use WebDriverWait along with expected_conditions to wait until the password input field appears
    wait = WebDriverWait(browser, 10)  # Wait up to 10 seconds
    password_input = wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, 'input[type="password"]')))

    # Now send_keys to the newly appeared input field
    password_input.send_keys(decryptedPassword)

    # Finding another submit button and clicking it
    next_submit_button = browser.find_element(By.CSS_SELECTOR, 'input[type="submit"]')
    next_submit_button.click()

    return jsonify(status="Received login info"), 200
