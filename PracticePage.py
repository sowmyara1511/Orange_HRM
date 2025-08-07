#Open AutomationPractice page and fill the text fields
import click
from selenium import webdriver
from selenium.webdriver.common.by import By

import sys
#edge_driver_path = "C:\Drivers\edgedriver_win64\msedgedriver.exe"
#driver = webdriver.Edge(edge_driver_path)
driver= webdriver.Chrome()
driver.maximize_window()
driver.get("https://testautomationpractice.blogspot.com/")
driver.implicitly_wait(10)
#text field
driver.find_element(By.ID,"name").send_keys("Test")
#check-box
driver.find_element(By.CSS_SELECTOR,"input[value='sunday']").click()
#radio-button
driver.find_element(By.XPATH ,"//input[@id='male']").click()
#click on dropdown
driver.find_element(By.XPATH ,"//select[@id='country']/option[@value='france']").click()
driver.implicitly_wait(10)

#driver.find_element(By.XPATH ,"//Select/option[@value='France']").click()
#print text in the webpage
driver.implicitly_wait(10)
print(driver.find_element(By.XPATH ,"//h1[normalize-space()='Automation Testing Practice']").text)
driver.find_element(By.XPATH, "//option[@value='red']").click()

driver.find_element(By.XPATH, "//option[@value='cheetah']").click()
#fill date
driver.implicitly_wait(10)
driver.find_element(By.XPATH, "//input[@id='datepicker']").send_keys("08/18/2025")
driver.implicitly_wait(10)
driver.find_element(By.XPATH, "//input[@id='txtDate']").send_keys("08/18/2025")
# Set start date
driver.find_element(By.XPATH, "//input[@id='start-date']").send_keys("2025-08-01")

# Set end date
driver.find_element(By.XPATH, "//input[@id='end-date']").send_keys("2025-08-07")

# Click submit
driver.find_element(By.XPATH, "//button[@class='submit-btn' and text()='Submit']").click()

#Single file upload
file_path= "C:\\Users\\srini\\Downloads\\SRINIVAS-R.txt"
upload_file=driver.find_element(By.XPATH,"//input[@id='singleFileInput']")
upload_file.send_keys(file_path)
driver.implicitly_wait(10)
driver.find_element(By.XPATH,"//button[normalize-space()='Upload Single File']").click()
