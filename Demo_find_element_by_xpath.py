import time
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
class ElementByXpath():
    def locateByXpath(self):
        driver=webdriver.Chrome(executable_path=ChromeDriverManager().install())
        driver.get("https://secure.yatra.com/social/common/yatra/register")
        driver.find_element(By.XPATH,"//input[@id='login-input']").send_keys("found.com")
        time.sleep(8)
findPath=ElementByXpath()
findPath.locateByXpath()