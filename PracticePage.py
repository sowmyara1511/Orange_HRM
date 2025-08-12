#Open AutomationPractice page and fill the text fields
import time

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

#Assert no file selected
driver.implicitly_wait(10)
driver.find_element(By.XPATH,"//button[normalize-space()='Upload Multiple Files']").click()
NoFile_Element=driver.find_element(By.XPATH,"//p[contains(text(),'No files selected.')]")
assert NoFile_Element.text == "No files selected."

#Single file upload
file_path= "C:\\Users\\srini\\Downloads\\SRINIVAS-R.txt"
upload_file=driver.find_element(By.XPATH,"//input[@id='singleFileInput']")
upload_file.send_keys(file_path)
driver.implicitly_wait(10)
driver.find_element(By.XPATH,"//button[normalize-space()='Upload Single File']").click()

#multiple file upload
file_path1="C:\\Users\\srini\\Downloads\\SQL Syllabus.pdf"
file_path= "C:\\Users\\srini\\Downloads\\SRINIVAS-R.txt"
upload_file.send_keys(file_path1)
upload_file.send_keys(file_path)
driver.implicitly_wait(10)
driver.find_element(By.XPATH,"//button[normalize-space()='Upload Multiple Files']").click()

#Accessing data from statice web table
rows= driver.find_elements(By.XPATH,"//table[@name='BookTable']//tbody/tr")

#count the columns in the table
for i in rows:
  cols=i.find_elements(By.TAG_NAME,"td")
  for j in cols:
     #if j=="Selenium":
        print("|",j.text)


#Accessing data from dynamic web table
rows= driver.find_elements(By.XPATH,"//table[@id='taskTable']//tbody/tr")

#count the columns in the table
for row in rows:
  cols=row.find_elements(By.TAG_NAME,"td")
  for col in cols:
     #if j=="Selenium":
        print("|",col.text)

#pagination web table , select all the data in 3rd page
table_data =driver.find_elements(By.XPATH,"//table[@id='productTable']")
pages= driver.find_elements(By.XPATH,"//ul[@id='pagination']")
n=len(pages)

for page in pages:
    if page ==3:
        page.click()
        break
time.sleep(4)

driver.implicitly_wait(10)
checkboxes = driver.find_elements(By.XPATH, "//table[@id='productTable']//input[@type='checkbox']")
for checkbox in checkboxes:
    checkbox.click()
print("All checkboxes are selected")







