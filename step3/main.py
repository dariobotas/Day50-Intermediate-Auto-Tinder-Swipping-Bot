from selenium import webdriver
from time import sleep

from selenium.webdriver import Keys
from selenium.webdriver.common.by import By

FB_EMAIL = ""
FB_PASSWORD = ""

driver = webdriver.Chrome()

driver.get("http://www.tinder.com")

sleep(2)
login_button = driver.find_element(By.XPATH,
                    value='//*[@id="content"]/div/div[1]/div/main/div[1]/div/div/header/div[1]/div[2]/div/button')
login_button.click()

sleep(2)
fb_login = driver.find_element(By.XPATH,
                               value='//*[@id="modal-manager"]/div/div/div[1]/div/div[3]/span/div[2]/button')
fb_login.click()

# Switch to Facebook login window
sleep(2)
base_window = driver.window_handles[0]
fb_login_window = driver.window_handles[1]
driver.switch_to.window(fb_login_window)
print(driver.title)

# Login and hit enter
email = driver.find_element(By.XPATH, value='//*[@id="email"]')
password = driver.find_element(By.XPATH, value='//*[@id="pass"]')
email.send_keys(FB_EMAIL)
password.send_keys(FB_PASSWORD)
password.send_keys(Keys.ENTER)

# Switch back to Tinder window
driver.switch_to.window(base_window)
print(driver.title)