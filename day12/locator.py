from selenium import webdriver
from selenium.webdriver.common.by import By

driver = webdriver.Chrome()
# driver.get("https://www.amazon.in/")

# # find element BY xpath
# ele = driver.find_element(By.XPATH,"/html[1]/body[1]/div[2]/header[1]/div[1]/div[1]/div[2]/div[1]/form[1]/div[2]/div[1]/input[1]")
# ele.click()
# ele.send_keys("redmi")

# cssselecor by class name
# ele = driver.find_element(By.CSS_SELECTOR,"input.nav-input")
# ele.click()
# ele.send_keys("redmi")

# cssselector By id
# driver.get("https://m.facebook.com/")
# ele = driver.find_element(By.CSS_SELECTOR,"#m_login_email").send_keys("7875006913")

#############################################BY CSS SELECTOR TAG ATTRIBUTE ################################
# # cssselector tag and attribute
# driver.get("https://www.facebook.com/")
# driver.find_element(By.CSS_SELECTOR,'input[data-testid=royal_email]').send_keys("email address")
# driver.close()

################################## BY XPATH ##########################################
# driver.get("https://www.facebook.com/")
# driver.find_element(By.XPATH,'//*[@id="email"]').send_keys("email.com")
# driver.close()


##############################BY TAG NAME#################################
# driver.get("https://www.facebook.com/")
# driver.find_element(By.NAME,'email').send_keys("email")

# <input type="text" class="inputtext _55r1 _6luy" name="email" id="email" data-testid="royal_email"
# placeholder="Email address or phone number" autofocus="1" aria-label="Email address or phone number">

####################################### BY LINK_TEXT ##################################
driver.get("https://www.facebook.com/")
##########################search path using starts-with() method ###############################
driver.find_element(By.XPATH,"//input[starts-with(@id,'em')]").send_keys("1234568")
############################ Search Xpath using contains() method
driver.find_element(By.XPATH,'//input[contains(@id,"pa")]').send_keys("123456789")
###########################





