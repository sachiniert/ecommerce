import time
from selenium import webdriver
from selenium.webdriver.chrome.service import Service

driver = webdriver.Chrome()

driver.get("https://rahulshettyacademy.com/")


time.sleep(2)
