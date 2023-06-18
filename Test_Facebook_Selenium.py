from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time

driver = webdriver.Chrome()
driver.maximize_window()


def Open_HomePage_and_Enter():
    # Open the Facebook homepage
    driver.get("https://www.facebook.com/")

    # Find and enter the email field
    email_field = driver.find_element(By.ID, "email")
    email_field.send_keys("nukeawesom@gmail.com")

    # Find and enter the password field
    password_field = driver.find_element(By.ID, "pass")
    password_field.send_keys("qwerty18")

    # Submit the login form by pressing Enter
    password_field.send_keys(Keys.RETURN)
    time.sleep(5)
    print("Test 1")


def Open_MyPage_And_Crear_News():
    # Open the user's profile page
    driver.get("https://www.facebook.com/profile.php?id=100093684337738")

    # Find and click on the new post button
    new = driver.find_element(By.XPATH,
                              '//div[@class="x1i10hfl x6umtig x1b1mbwd xaqea5y xav7gou x9f619 x1ypdohk xe8uvvx xdj266r x11i5rnm xat24cr x1mh8g0r x16tdsg8 x1hl2dhg xggy1nq x87ps6o x1lku1pv x1a2a7pz x6s0dn4 xmjcpbm x107yiy2 xv8uw2v x1tfwpuw x2g32xy x78zum5 x1q0g3np x1iyjqo2 x1nhvcw1 x1n2onr6 xt7dq6l x1ba4aug x1y1aw1k xn6708d xwib8y2 x1ye3gou"]')
    new.click()
    time.sleep(5)

    # Enter the text in the "Co słychać?" field
    text = "Test Selenium 2023!!!"
    post_field = driver.find_element(By.XPATH, '//div[@aria-label="Co słychać?"]')
    post_field.send_keys(text)
    time.sleep(2)

    # Find and click on the publish button
    button1 = WebDriverWait(driver, 5).until(
        EC.presence_of_element_located((By.XPATH, '//div[@aria-label="Opublikuj"]')))
    button1.click()

    print("Test 2")


Open_HomePage_and_Enter()
Open_MyPage_And_Crear_News()

