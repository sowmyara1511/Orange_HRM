#scenario1: Open a website , open another site and go back to same site
from sys import executable

from selenium import webdriver
import sys
#edge_driver_path = "C:\Drivers\edgedriver_win64\msedgedriver.exe"
#driver = webdriver.Edge(edge_driver_path)
driver= webdriver.Chrome()
driver.maximize_window()
driver.get("https://opensource-demo.orangehrmlive.com/web/index.php/auth/login")
print(driver.title)
driver.get("http://www.rahulshettyacademy.com/")
driver.back()
driver.close()
