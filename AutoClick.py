from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import Select
from selenium.webdriver.chrome.service import Service as ChromeService
import pandas as pd
import xlwings as xw
import os
import dfpw as pww
import time
#from subprocess import CREATE_NO_WINDOW
from subprocess import call


chrome_options = Options()
#chrome_options.add_argument("--headless")
chrome_options.add_argument('--ignore-certificate-errors-spki-list')
chrome_options.add_argument('start-maximized')
chrome_options.add_argument("--disable-notifications")

driver = webdriver.Chrome(options=chrome_options)
driver.delete_all_cookies()
wait = WebDriverWait(driver, 10)


while True:
    try:
        driver.get("     ")
        wait.until(EC.visibility_of_element_located((By.XPATH, "//*[@id='i0116']"))).send_keys("   ")
        wait.until(EC.visibility_of_element_located((By.ID, ' '))).click()
        wait.until(EC.visibility_of_element_located((By.ID, "username"))).send_keys(pww.secret_id)
        wait.until(EC.visibility_of_element_located((By.ID, "password"))).send_keys(pww.secret_pw)
        driver.find_element(By.XPATH, "    ").click()
        time.sleep(5)
        driver.get("     ")
        wait.until(EC.element_to_be_clickable((By.XPATH, "//button[contains(., '同步')]"))).click()
        time.sleep(10)
    except Exception:
        continue

 #call(["robocopy", r"Path A", r"Path B", "/mir"])

