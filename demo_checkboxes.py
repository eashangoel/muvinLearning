import time
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By

class checkbox():
    def find_checkbox(self):
        driver=webdriver.Chrome(executable_path=ChromeDriverManager().install())
        driver.get("https://formstone.it/components/checkbox/")
        driver.maximize_window()
        driver.find_element(By.XPATH,"//div[@class='fs-row']//div[1]//form[1]//fieldset[2]//div[1]//div[1]//div[1]").click()
        time.sleep(10)
checkbox1=checkbox()
checkbox1.find_checkbox()