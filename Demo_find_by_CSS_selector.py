import time
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
class FindByCSS_selectors():
     def locate_element_by_css(self):
         driver=webdriver.Chrome(executable_path=ChromeDriverManager().install())
         driver.get("https://secure.yatra.com/social/common/yatra/register")
         driver.find_element(By.CSS_SELECTOR,"#login-input").send_keys("CSS_found")
         time.sleep(5)
findCSS=FindByCSS_selectors()
findCSS.locate_element_by_css()