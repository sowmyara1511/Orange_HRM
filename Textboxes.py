#Simple dropdowns
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
driver.get("https://testautomationcentral.com/demo/textboxes.html")
driver.implicitly_wait(10)
driver.find_element(By.XPATH,"//input[@type='text']").send_keys("Test")

#placeholder text
place_text= driver.find_element(By.XPATH,"//button[@data-target='placeholder-textbox']")
place_text.click()
driver.find_element(By.XPATH,"//input[@placeholder='Placeholder text']").send_keys("Test")

#Password textbox
pass_text= driver.find_element(By.XPATH,"//button[@data-target='password-textbox']")
pass_text.click()
driver.find_element(By.XPATH,"//input[@type='password']").send_keys("password")

#Text Area
text_area=pass_text= driver.find_element(By.XPATH,"//button[@data-target='text-area']")
text_area.click()
driver.find_element(By.XPATH,"//textarea[@placeholder='Enter detailed text']").send_keys("This is the python seleinium")

#Read only text
read_only=pass_text= driver.find_element(By.XPATH,"//button[@data-target='readonly-textbox']")
read_only.click()
Read_text=driver.find_element(By.XPATH,"//input[@value='Read-only text']").text()
print(Read_text)

#Disabled Textbox

disabled_text=pass_text= driver.find_element(By.XPATH,"//button[@data-target='disabled-textbox']")
disabled_text.click()
driver.find_element(By.XPATH,"//input[@value='Disabled text']").text()

