from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
import time
import os

#chrome_options = webdriver.ChromeOptions()
#chrome_options.add_experimental_option("detach", True)
#driver = webdriver.Firefox()#.Chrome()

chrome_options = Options()
chrome_options.add_argument('--no-sandbox')
chrome_options.add_argument('--disable-dev-shm-usage')
driver = webdriver.Chrome(options=chrome_options)

driver.get(
    "https://www.linkedin.com/jobs/search/?f_LF=f_AL&geoId=102257491"
    "&keywords=python%20developer"
    "&location=London%2C%20England%2C%20United%20Kingdom"
    "&redirect=false&position=1&pageNum=0"
)
"""import os

os.system("pip install selenium==3.141.0")
from webbot import Browser

web = Browser()
web.go_to('https://github.com/SeleniumHQ/selenium ')
website = input('Service has audio')"""