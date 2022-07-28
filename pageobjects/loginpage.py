from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time


class Login:
    textbox_usrename_id = "Email"
    textbox_password_id = "Password"
    button_login_xpath = "/html/body/div[6]/div/div/div/div/div[2]/div[1]/div/form/div[3]/button"
    link_logout = "Logout"
    def __init__(self, driver):
        self.driver = driver

    def setusername(self, username):
        time.sleep(5)
        self.driver.find_element(By.ID, self.textbox_usrename_id).clear()
        self.driver.find_element(By.ID, self.textbox_usrename_id).send_keys(username)

    def setpassword(self, password):
        self.driver.find_element(By.ID, self.textbox_password_id).clear()
        self.driver.find_element(By.ID, self.textbox_password_id).send_keys(password)

    def clicklogin(self):
        self.driver.find_element(By.XPATH, self.button_login_xpath).click()

    def clicklogout(self):
        self.driver.find_element(By.LINK_TEXT, self.link_logout).click()
