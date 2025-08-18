import time

import driver
from selenium.webdriver import ActionChains
from selenium import webdriver
from selenium.webdriver.common.by import By

driver= webdriver.Chrome()
driver.maximize_window()
driver.get("https://testautomationpractice.blogspot.com/")
driver.implicitly_wait(10)
src= driver.find_element(By.XPATH,"//div[@id='draggable']")
trgt= driver.find_element(By.XPATH,"//div[@id='droppable']")
actions = ActionChains(driver)
actions.drag_and_drop(src,trgt).perform()

time.sleep(10)
sld=driver.find_element(By.XPATH,"//div[@id='slider-range']")
actions.click_and_hold(sld).move_by_offset(100, 0).release().perform()