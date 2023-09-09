import time
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
import os





chrome_options = Options()
chrome_options.add_experimental_option("detach", True)

# Adding argument to disable the AutomationControlled flag
chrome_options.add_argument("--disable-blink-features=AutomationControlled")

# Exclude the collection of enable-automation switches
chrome_options.add_experimental_option("excludeSwitches", ["enable-automation"])

# Turn-off userAutomationExtension
chrome_options.add_experimental_option("useAutomationExtension", False)

# Setting the driver path and requesting a page

driver = webdriver.Chrome(options=chrome_options)
driver.get('https://chat.openai.com/auth/login')
time.sleep(3)
try:
    WebDriverWait(driver, 2).until(EC.element_to_be_clickable((By.XPATH, '//*[@id="__next"]/div[1]/div[2]/div[1]/div/button[1]'))).click()
    WebDriverWait(driver,5).until(EC.visibility_of_element_located((By.XPATH,'//*[@id="username"]'))).send_keys(os.environ["CHATGTP_EMAIL"])
    WebDriverWait(driver,5).until(EC.visibility_of_element_located((By.XPATH,'/html/body/div/main/section/div/div/div/div[1]/div/form/div[2]/button'))).click()
    WebDriverWait(driver,5).until(EC.visibility_of_element_located((By.XPATH,'// *[ @ id = "password"]'))).send_keys(os.environ['CHATGTP_PASS'])
    WebDriverWait(driver,5).until(EC.element_to_be_clickable((By.XPATH,'/html/body/div/main/section/div/div/div/form/div[3]/button'))).click()
    WebDriverWait(driver, 5).until(EC.element_to_be_clickable((By.XPATH, '// *[ @ id = "radix-:rf:"] / div[2] / div / div[4] / button'))).click()


except:
    pass