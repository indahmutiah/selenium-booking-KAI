from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.support import expected_conditions as EC
# from webdriver_manager.chrome import ChromeDriverManager
from webdriver_manager.firefox import GeckoDriverManager


import time

driver = webdriver.Firefox(service=Service(GeckoDriverManager().install()))
driver.get('https://booking.kai.id/')
driver.implicitly_wait(1000) 

input_asal= WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.ID, "origination-flexdatalist")))
input_asal.send_keys("Bandung")