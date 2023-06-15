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

    new = driver.find_element(By.XPATH, '//div[@class="x1i10hfl x6umtig x1b1mbwd xaqea5y xav7gou x9f619 x1ypdohk xe8uvvx xdj266r x11i5rnm xat24cr x1mh8g0r x16tdsg8 x1hl2dhg xggy1nq x87ps6o x1lku1pv x1a2a7pz x6s0dn4 xmjcpbm x107yiy2 xv8uw2v x1tfwpuw x2g32xy x78zum5 x1q0g3np x1iyjqo2 x1nhvcw1 x1n2onr6 xt7dq6l x1ba4aug x1y1aw1k xn6708d xwib8y2 x1ye3gou"]')
    new.click()
    time.sleep(5)

    text = "To jest mój nowy post!"

    post_field = driver.find_element(By.XPATH,
        '//div[@class="x1o1ewxj x3x9cwd x1e5q0jg x13rtm0m x1ey2m1c xds687c xg01cxk x47corl x10l6tqk x17qophe x13vifvy x1ebt8du x19991ni x1dhq9h x1wpzbip"]')
    post_field.send_keys(text)

    time.sleep(5)

Open_HomePage_and_Enter()
Open_MyPage_And_Crear_News()

