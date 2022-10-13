from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

import pandas as pd
import xlwings as xw
import os
import dfpw as pww
import time
import glob


#from subprocess import CREATE_NO_WINDOW
from subprocess import call

xw.App(visible=False)
app_excel = xw.App(visible = False)

wb = xw.books.open(r'  .xlsm')
macro = wb.macro("Get_Query")
macro()

# app_excel = xw.App(visible = False)
# wbk = xw.Book( 'D:\stuff\file.xlsx' )
# wbk.api.RefreshAll()
# wbk.save( 'file.xlsx')


wb.save(r'test.xlsx')
wb.close()
# kill Excel
# app_excel.kill()
# del app_excel

chrome_options = Options()
#chrome_options.add_argument("--headless")
chrome_options.add_argument('--ignore-certificate-errors-spki-list')
chrome_options.add_argument('start-maximized')
chrome_options.add_argument("--disable-notifications")
chrome_options.add_experimental_option("prefs", {"download.default_directory": r"C:\Users\xxxx\Desktop\Py_Auto\raw_data"})

#This package can help update Chrome, so your code won't fk when chrome update
driver = webdriver.Chrome(ChromeDriverManager(path=r"C:\Users\xxxx\Desktop\Py_Auto").install(), options=chrome_options) 
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
        wait.until(EC.element_to_be_clickable((By.XPATH, "//button[contains(., 'Sync')]"))).click()
        time.sleep(10)
    except Exception:
        continue

 #Love this code so much for mirr or copy files      
 #call(["robocopy", r"Path A", r"Path B", "/mir"])
    
    
driver.quit()
sys.exit()
