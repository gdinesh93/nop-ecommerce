from selenium import webdriver
from selenium.webdriver.common.by import By
driver=webdriver.Chrome(executable_path="E:\chromedriver_win32\chromedriver.exe")

driver.get("https://www.geeksforgeeks.org/")
element = driver.find_element(By.ID,"gsc-i-id2")
element.location




