import time
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
class DemoSelenium():
    def demoCommands(self):
        driver=webdriver.Chrome(executable_path=ChromeDriverManager().install())
        driver.get("https://www.moengage.com/")
        print(driver.current_url)
        print(driver.title)
        driver.maximize_window()
        driver.fullscreen_window()
        driver.refresh()
        driver.find_element(By.XPATH,"/html[1]/body[1]/div[1]/div[1]/div[1]/header[1]/div[1]/nav[1]/ul[8]/li[8]/a[1]").click()
        driver.back()
        driver.forward()
        driver.minimize_window()
        time.sleep(4)
        driver.quit()
follow=DemoSelenium()
follow.demoCommands()
