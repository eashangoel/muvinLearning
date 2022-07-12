import time
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select

class dropbox():
    class handle_dropbox():
        driver=webdriver.Chrome(executable_path=ChromeDriverManager().install())
        driver.get("https://www.salesforce.com/in/form/signup/freetrial-sales/?d=jumbo1-btn-ft")
        drpdown=driver.find_element(By.NAME,"UserTitle")
        dd= Select(drpdown)
        dd.select_by_index(1)
        time.sleep(3)
        dd.select_by_visible_text("Marketing / PR Manager")
        time.sleep(3)
        dd.select_by_value("Customer_Service_Manager_AP")
        time.sleep(3)
dddemo=dropbox()
dddemo.handle_dropbox()
