import time
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By


class Text_element():
    def get_text(self):
        driver = webdriver.Chrome(executable_path=ChromeDriverManager().install())
        driver.get("https://www.yatra.com/")
        text1 = driver.find_element(By.XPATH,"//a[@class='dropdown-toggle eventTrackable list-dropdownNull ytBusinessTrack']").text
        #text = driver.find_element(By.XPATH,"//a[@class='dropdown-toggle eventTrackable list-dropdownNull ytBusinessTrack']").get_attribute"innerHTML")
        print(text1)
        time.sleep(2)


locate = Text_element()
locate.get_text()
