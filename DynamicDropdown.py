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
driver.get("https://testautomationcentral.com/demo/dropdown.html")
driver.implicitly_wait(10)
simple_drop=driver.find_element(By.XPATH, "//select[@class='form-select block w-full mt-1']")
simple_drop.click()
simple_drop.value_of_css_property("option1")


#styled dropdown
driver.find_element(By.XPATH,"//button[@data-target='styled-dropdown']").click()
simple_drop=driver.find_element(By.XPATH, "//select[@class='form-select block w-full mt-1 border-blue-500 text-blue-500']")
simple_drop.click()
driver.implicitly_wait(10)
simple_drop.value_of_css_property("Styled Option 2")

#multiselect drodown
time.sleep(10)
driver.find_element(By.XPATH,"//button[normalize-space()='Multi-Select']").click()
select_option=driver.find_element(By.XPATH,"//select[@class='form-multiselect block w-full mt-1']")
multi_select= Select(select_option)
multi_select.select_by_visible_text("Option 1")
multi_select.select_by_visible_text("Option 2")
multi_select.select_by_visible_text("Option 3")

#Grouped dropdown
time.sleep(10)
driver.find_element(By.XPATH,"//button[normalize-space()='Grouped Dropdown']").click()
driver.implicitly_wait(10)
driver.find_element(By.XPATH,"//optgroup//option[@value='option2'][normalize-space()='Option 2']").click()

#dependent dropdown





