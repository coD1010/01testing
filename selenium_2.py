import time
from selenium import webdriver
from selenium.webdriver.common.by import By

driver = webdriver.Chrome()

def test_1():
    url = 'https://demoqa.com/text-box'
    driver.maximize_window()
    driver.get(url)
    full_name = driver.find_element(By.XPATH,"//label[@class='form-label'][contains(.,'Full Name')]")
    assert full_name.text == 'Full Name'
    email = driver.find_element(By.ID,'userEmail-label')
    assert email.text == 'Email'
    driver.quit()
