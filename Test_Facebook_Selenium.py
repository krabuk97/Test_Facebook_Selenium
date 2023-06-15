from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time

driver = webdriver.Chrome()
driver.maximize_window()

def Open_HomePage_and_Enter():
    driver.get("https://www.facebook.com/")
    email_field = driver.find_element(By.ID, "email")
    email_field.send_keys("nukeawesom@gmail.com")
    password_field = driver.find_element(By.ID, "pass")
    password_field.send_keys("qwerty18")

    password_field.send_keys(Keys.RETURN)
    time.sleep(5)
    print("Test 1")

def Open_MyPage_And_Crear_News():
    driver.get("https://www.facebook.com/profile.php?id=100093684337738")
    time.sleep(5)

Open_HomePage_and_Enter()
Open_MyPage_And_Crear_News()

