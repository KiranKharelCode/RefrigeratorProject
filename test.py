
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
driver = webdriver.Chrome(options=chrome_options)
url = "https://www.bing.com/search?q=Bing+AI&showconv=1&FORM=hpcodx"

driver.get(url)
time.sleep(5)
button = driver.execute_script('return document.querySelector("#b_sydConvCont > cib-serp").shadowRoot.querySelector("#cib-conversation-main").shadowRoot.querySelector("#cib-chat-main > cib-welcome-container").shadowRoot.querySelector("div.controls > cib-tone-selector").shadowRoot.querySelector("#tone-options > li:nth-child(3) > button")')
driver.execute_script('arguments[0].click();',button)