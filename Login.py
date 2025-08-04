
from selenium import webdriver
import sys
print(sys.executable)
driver= webdriver.Chrome()
driver.maximize_window()
driver.get("https://opensource-demo.orangehrmlive.com/web/index.php/auth/login")
print(driver.title)
driver.get("http://www.rahulshettyacademy.com/")
driver.back()
driver.close()
