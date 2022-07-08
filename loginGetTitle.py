from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager

import time

usernameStr = 'EashanGoel'
passwordStr = 'green2938'
driver = webdriver.Chrome(ChromeDriverManager().install())
driver.get(('https://en.wikipedia.org/w/index.php?title=Special:UserLogin&returnto=Main+Page'))

username = driver.find_element(By.ID, 'wpName1')
username.send_keys(usernameStr)
password = driver.find_element(By.ID, 'wpPassword1')
password.send_keys(passwordStr)
nextButton= driver.find_element(By.CSS_SELECTOR,"button.mw-htmlform-submit")
nextButton.click()
print(driver.title)
time.sleep(3)
driver.maximize_window()
driver.close()

