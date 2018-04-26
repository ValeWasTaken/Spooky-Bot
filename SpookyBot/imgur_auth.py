# Python 3.6.4
from imgurpython import ImgurClient
import configparser
from selenium import webdriver
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By


def authenticate():
    # Stores all secret authentication information
    # and logs in and generates PIN.
    config = configparser.ConfigParser()
    config.read('auth.ini')
    
    client_id = config.get('ImgurInfo', 'client_id')
    client_secret = config.get('ImgurInfo', 'client_secret')
    imgur_username = config.get('ImgurInfo', 'imgur_username')
    imgur_password = config.get('ImgurInfo', 'imgur_password')

    client = ImgurClient(client_id, client_secret)
    auth_url = client.get_auth_url('pin')

    driver = webdriver.Firefox()
    driver.get(auth_url)

    username = driver.find_element_by_xpath('//*[@id="username"]')
    password = driver.find_element_by_xpath('//*[@id="password"]')
    username.clear()  # Makes sure username box is empty.
    username.send_keys(imgur_username)  # Types in username.
    password.send_keys(imgur_password)

    driver.find_element_by_name("allow").click()

    timeout = 5 # Give the page time to load.
    try:
        # Wait for a page to be loaded that has an ID of "pin".
        element_presence = EC.presence_of_element_located((By.ID, 'pin'))
        WebDriverWait(driver, timeout).until(element_presence)

        pin_element = driver.find_element_by_id('pin')
        pin = pin_element.get_attribute('value')
    except TimeoutException:
        print('Timed out, waiting for page to load.')
    driver.close()

    ImgurInfo = client.authorize(pin, 'pin')
    client.set_user_auth(ImgurInfo['access_token'],
                         ImgurInfo['refresh_token'])
    return client


if __name__ == "__main__":
    authenticate()