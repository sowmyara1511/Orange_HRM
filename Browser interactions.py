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

