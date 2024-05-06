import time
from selenium import webdriver
from selenium.webdriver import Keys, ActionChains
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

driver = webdriver.Chrome()
url = "https://testpages.eviltester.com/styled/page?app=testpages&t=Others#demo-blaze-product-store"
driver.get(url)
driver.maximize_window()
t = 3
time.sleep(t)

def move_to_another_hadler(driver,new_page_handler):
    for window_handle in driver.current_window_handle:
        if window_handle != new_page_handler:
            driver.switch_to.window(window_handle)
            break
def test_multipple_tabs():
    original_page_handler = driver.current_window_handle
    new_page_hendler = driver.find_element(By.XPATH,"https://thepulper.herokuapp.com/apps/pulp/]")
    new_page_hendler.click()

    move_to_another_hadler(driver,original_page_handler)

    movies_torrents = driver.find_element(By.XPATH)
