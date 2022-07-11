import time
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
class check_enabled():
    def enabled_state(self):
        driver = webdriver.Chrome(executable_path=ChromeDriverManager().install())
        driver.get("https://training.openspan.com/login")
        demo_state=driver.find_element(By.XPATH,"//input[@id='login_button']").is_enabled()
        print(demo_state)
find_state=check_enabled()
find_state.enabled_state()