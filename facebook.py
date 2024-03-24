from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
from selenium.common.exceptions import *
from selenium.webdriver.common.keys import Keys
from time import sleep
import json

def get_email_from_facebook(postLink):
    email = []
    phone_number = ""
    address = ""
    firefox_profile_directory = 'C:/Users/Administrator/AppData/Roaming/Mozilla/Firefox/Profiles/5p9qij3y.default-release'
    firefox_options = webdriver.FirefoxOptions()
    firefox_options.profile = webdriver.FirefoxProfile(firefox_profile_directory)

    driver = webdriver.Firefox(options=firefox_options)
    driver.maximize_window()
    driver.get(postLink)
    
    sleep(5)
    
    try:
        email_button= driver.find_element(By.CSS_SELECTOR, 'img.x1b0d499.xuo83w3[src="https://static.xx.fbcdn.net/rsrc.php/v3/yE/r/2PIcyqpptfD.png"]').find_element(By.XPATH, 'ancestor::div[2]')
        email_div = email_button.find_element(By.CSS_SELECTOR, "div[class=\"x9f619 x1n2onr6 x1ja2u2z x78zum5 xdt5ytf x193iq5w xeuugli x1r8uery x1iyjqo2 xs83m0k xamitd3 xsyo7zv x16hj40l x10b6aqq x1yrsyyn\"]")
        email_data = email_div.find_element(By.TAG_NAME, "span").text
        email.append(email_data)
    except:
        pass
    
    try:
        phone_button= driver.find_element(By.CSS_SELECTOR, 'img.x1b0d499.xuo83w3[src="https://static.xx.fbcdn.net/rsrc.php/v3/yT/r/Dc7-7AgwkwS.png"]').find_element(By.XPATH, 'ancestor::div[2]')
        phone_div = phone_button.find_element(By.CSS_SELECTOR, "div[class=\"x9f619 x1n2onr6 x1ja2u2z x78zum5 xdt5ytf x193iq5w xeuugli x1r8uery x1iyjqo2 xs83m0k xamitd3 xsyo7zv x16hj40l x10b6aqq x1yrsyyn\"]")
        phone_number = phone_div.find_element(By.TAG_NAME, "span").text
    except:
        pass
    
    try:
        address_button= driver.find_element(By.CSS_SELECTOR, 'img.x1b0d499.xuo83w3[src="https://static.xx.fbcdn.net/rsrc.php/v3/yW/r/8k_Y-oVxbuU.png"]').find_element(By.XPATH, 'ancestor::div[2]')
        address_div = address_button.find_element(By.CSS_SELECTOR, "div[class=\"x9f619 x1n2onr6 x1ja2u2z x78zum5 xdt5ytf x193iq5w xeuugli x1r8uery x1iyjqo2 xs83m0k xamitd3 xsyo7zv x16hj40l x10b6aqq x1yrsyyn\"]")
        address = address_div.find_element(By.TAG_NAME, "span").text
    except:
        pass
    print(f'facebook email first = ', email)
    driver.quit()    
    return email, phone_number, address

