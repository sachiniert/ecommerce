import time

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select

driver = webdriver.Chrome()
driver.get("https://rahulshettyacademy.com/angularpractice/")
driver.find_element(By.CSS_SELECTOR,"input[name=name]").send_keys("Sachin")
driver.find_element(By.NAME,"email").send_keys("sachin@gmail.com")
driver.find_element(By.ID,"exampleInputPassword1").send_keys("chcfdhf")
driver.find_element(By.ID,"exampleCheck1").click()
#driver.find_element(By.ID,"exampleFormControlSelect1").click()
driver.find_element(By.XPATH,"//input[@type='submit']").click()
# Static Dropdown
# use with Select class

dropdown=Select(driver.find_element(By.ID,"exampleFormControlSelect1"))
dropdown.select_by_index(1)
dropdown.select_by_visible_text("Female")
#dropdown.select_by_index(0)
#dropdown.select_by_value()

message=driver.find_element(By.CLASS_NAME,"alert-success").text

print(message)
assert "successfully" in message
driver.find_element(By.XPATH,"(//input[@type='text'])[3]").send_keys("sachin")
driver.find_element(By.XPATH,"(//input[@type='text'])[3]").clear()
#driver.close()

time.sleep(2)
