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

class test_Login_001():
    username = "//input[@id='txtUsername']"
    password = "//input[@id='txtPassword']"
    login_button = "//input[@id='btnLogin']"

    def __init__(self,driver):
        self.driver = driver
        self.driver.get("https://opensource-demo.orangehrmlive.com/")

    def set_username(self):
        self.driver.find_element(By.XPATH,self.username).send_keys("Admin")

    def set_password(self):
        self.driver.find_element(By.XPATH,self.password).send_keys("admin123")

    def click_login(self):
        self.driver.find_element(By.XPATH,self.login_button).click()

    def close_browser(self):
        self.driver.quit()


driver = webdriver.Chrome()

def test_001_login():
    obj = test_Login_001(driver)
    obj.set_username()
    obj.set_password()
    obj.click_login()
    obj.close_browser()





