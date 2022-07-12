import time
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By

class demo_radio():
    def check_radio(self):
        driver=webdriver.Chrome(executable_path=ChromeDriverManager().install())
        driver.get("https://demos.jquerymobile.com/1.4.5/checkboxradio-radio/")
        driver.find_element(By.XPATH,"//div[@class='ui-radio']//label[@class='ui-btn ui-corner-all ui-btn-inherit ui-btn-icon-left ui-radio-off'][normalize-space()='One']").click()
        time.sleep(3)
check=demo_radio()
check.check_radio()
