from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time

driver = webdriver.Chrome()
driver.maximize_window()

driver.get("https://www.facebook.com/")
email_field = driver.find_element(By.ID, "email")
email_field.send_keys("nukeawesom@gmail.com")
password_field = driver.find_element(By.ID, "pass")
password_field.send_keys("qwerty18")

password_field.send_keys(Keys.RETURN)
time.sleep(5)
print("Test 1")

