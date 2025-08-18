import time

import click
from select import select
from selenium import webdriver
from selenium.webdriver.common.by import By

import sys

from selenium.webdriver.support.select import Select

#edge_driver_path = "C:\Drivers\edgedriver_win64\msedgedriver.exe"
#driver = webdriver.Edge(edge_driver_path)
driver= webdriver.Chrome()
driver.maximize_window()
driver.get("https://testautomationcentral.com/demo/alerts.html")
driver.find_element(By.XPATH,"//button[@onclick='showAlert()']").click()
driver.switch_to.alert.accept()
#prompt

driver.find_element(By.XPATH,"//button[@data-target='prompt-tab']").click()
driver.find_element(By.XPATH,"//button[@onclick='showPrompt()']").click()
prompt = driver.switch_to.alert
prompt.send_keys("Test")
prompt.accept()

#confirm button
driver.find_element(By.XPATH,"//button[@data-target='confirm-tab']").click()
driver.find_element(By.XPATH,"//button[@onclick='showConfirm()']").click()
prompt = driver.switch_to.alert
t=prompt.text
print(t)
prompt.accept()

#iframes
driver.get("https://testautomationcentral.com/demo/frames_iframes.html")
time.sleep(5)
frame_message=driver.find_element(By.XPATH,"//iframe[contains(@src, 'example.com')]")
driver.switch_to.frame(frame_message)
heading = driver.find_element(By.TAG_NAME, "p")
print(heading.text)
driver.switch_to.default_content()


