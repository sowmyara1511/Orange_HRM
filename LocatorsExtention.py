
from selenium import webdriver
from selenium.webdriver.common.by import By
driver= webdriver.Chrome()
driver.maximize_window()
driver.get("https://login.salesforce.com/?locale=in")
driver.find_element(By.ID,"username").send_keys("Test")
driver.find_element(By.LINK_TEXT,"Forgot Your Password?").click()
driver.find_element(By.NAME,"cancel").click()

