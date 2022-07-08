import time
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
class FindByLink():
     def locate_element_by_link(self):
         driver=webdriver.Chrome(executable_path=ChromeDriverManager().install())
         driver.get("https://www.yatra.com/")
         driver.find_element(By.LINK_TEXT,"Yatra for Business").click()
         time.sleep(5)
findCSS=FindByLink()
findCSS.locate_element_by_link()