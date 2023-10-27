from selenium import webdriver
from time import sleep
import os
from sys import platform as _platform

# define chromedriver path
if _platform == "win32" or _platform == "win64":
    # Windows
    chromedriver_path = os.path.abspath('../../drivers') + '\chromedriver_win32\chromedriver.exe'

# create a chrome (driver)
driver = webdriver.Chrome(chromedriver_path)

# Open portal
driver.get("http://www.example.com")

# Accepting cookies (click button)
driver.find_element_by_xpath('//button[contains(@data-test-id, \'accept-cookies-button\')]').click()

# Wait
sleep(5)

# Close driver
driver.close()
