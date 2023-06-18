from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time

driver = webdriver.Chrome()
driver.maximize_window()


def open_homepage_and_enter():
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


def open_mypage_and_creat_news():
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


def find_and_add_friend():
    # Click on the "Friends" button
    friends_button = WebDriverWait(driver, 5).until(
        EC.element_to_be_clickable((By.XPATH, '//a[@aria-label="Znajomi"]'))
    )
    friends_button.click()
    time.sleep(2)

    # Click on the "Confirm" button to add the friend
    accept_button = WebDriverWait(driver, 5).until(
        EC.element_to_be_clickable((By.XPATH, '//button[contains(text(), "Potwierdź")]'))
    )
    accept_button.click()
    time.sleep(2)

    print("Test 3")


def find_person_and_send_message():
    # Search for a specific person
    search = driver.find_element(By.CSS_SELECTOR, '.x1i10hfl.xggy1nq.x1s07b3s.x1kdt53j.x1yc453h.xhb22t3.xb5gni.xcj1dhv.x2s2ed0.xq33zh.xjyslct.xjbqb8w.x6umtig.x1b1mbwd.xaqea5y.xav7gou.xnwf7zb.x40j3uw.x1s7lred.x15gyhx8.x9f619.xzsf02u.xdl72j9.x1iyjqo2.xs83m0k.xjb2p0i.x6prxxf.xeuugli.x1a2a7pz.x1n2onr6.x15h3p50.xm7lytj.x1sxyh0.xdvlbce.xurb0ha.x1vqgdyp.xo6swyp.x1ad04t7.x1glnyev.x1ix68h3.x19gujb8')
    search.send_keys('Ruslan Cheberdyn')
    search.send_keys(Keys.RETURN)
    time.sleep(2)

    # Click on the profile of the found person
    element = WebDriverWait(driver, 5).until(
        EC.element_to_be_clickable((By.XPATH, '//a[@aria-label="Rusłan Cheberdyn"]'))
    )
    element.click()
    time.sleep(2)

    # Click on the "Send message" button
    send_button = WebDriverWait(driver, 3).until(
        EC.element_to_be_clickable((By.XPATH, '//div[@aria-label="Wyślij wiadomość"]'))
    )
    send_button.click()
    time.sleep(2)

    # Enter the message content and send it
    message = "Test Selenium 2023!!!"
    message_field = driver.find_element(By.XPATH, '//div[@aria-label="Wiadomość"]')
    message_field.send_keys(message)
    message_field.send_keys(Keys.ENTER)

    time.sleep(2)
    print("Test 3")


open_homepage_and_enter()
#open_mypage_and_creat_news()
#find_and_add_friend()
find_person_and_send_message()
