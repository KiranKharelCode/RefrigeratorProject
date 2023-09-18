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
driver.get('https://www.bing.com/search?q=Bing+AI&showconv=1&FORM=hpcodx')
time.sleep(5)
button = driver.execute_script('return document.querySelector("#b_sydConvCont > cib-serp").shadowRoot.querySelector("#cib-conversation-main").shadowRoot.querySelector("#cib-chat-main > cib-welcome-container").shadowRoot.querySelector("div.controls > cib-tone-selector").shadowRoot.querySelector("#tone-options > li:nth-child(3) > button")')
driver.execute_script('arguments[0].click();',button)
text_box = driver.execute_script('return document.querySelector("#b_sydConvCont > cib-serp").shadowRoot.querySelector("#cib-action-bar-main").shadowRoot.querySelector("div > div.main-container > div > div.input-row > cib-text-input").shadowRoot.querySelector("#searchbox").value = "TestNG";')





