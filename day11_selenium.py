# Test Case
# 1) Open WebBrowser(Chrome/firefox/edge)
# 2) oprn the url "https://opensource-demo.orangehrmlive.com/"
# 3) enter username = "Admin"
# 4) enter password = "admin123"
# 5) click on login
# 6) capture the title of dash bord page (Actual title)
# 7) varify the title of the page actual vs expected
# 8) close
from selenium import webdriver
from selenium.webdriver.common.by import By
import pytest


class TS_Login_001:
    username = "//input[@id='txtUsername']"
    password = "//input[@id='txtPassword']"
    login_button = "//input[@id='btnLogin']"
    driver = webdriver.Chrome()

    def __init__(self):
        self.driver.get("https://opensource-demo.orangehrmlive.com/")

    def set_username(self):
        self.driver.find_element(By.XPATH,self.username).send_keys("Admin")

    def set_password(self):
        self.driver.find_element(By.XPATH,self.password).send_keys("admin123")

    def click_login(self):
        self.driver.find_element(By.XPATH,self.login_button).click()

    def close_browser(self):
        self.driver.close()


# obj.close_browser()

class test_dashbord(TS_Login_001):
    def test_001_login(self):
        obj = TS_Login_001()
        obj.set_username()
        obj.set_password()
        obj.click_login()


# obj1 = test_dashbord()
# obj1.test_001_login()