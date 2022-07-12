import time
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By

class hidden_element():
    def find_hidden(self):
        driver=webdriver.Chrome(executable_path=ChromeDriverManager().install())
        driver.get("https://www.w3schools.com/howto/howto_js_toggle_hide_show.asp")
        element=driver.find_element(By.XPATH,"//div[@id='myDIV']").is_displayed()
        print(element)
        time.sleep(2)
        driver.find_element(By.XPATH,"//button[@class='ws-btn w3-hover-black w3-dark-grey']").click()
        element1 = driver.find_element(By.XPATH, "//div[@id='myDIV']").is_displayed()
        print(element1)
        time.sleep(3)
        driver.find_element(By.XPATH,"//a[normalize-space()='Fullscreen Window']").click()
        time.sleep(4)
find_el=hidden_element()
find_el.find_hidden()
