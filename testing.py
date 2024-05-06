import time
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.common.exceptions import NoSuchElementException

driver = webdriver.Chrome()
url = 'https://www.amazon.com.mx'
driver.get(url)
driver.maximize_window()
time.sleep(5)

def test_amazon_1():
    try:
        search_box = driver.find_element(By.XPATH, "//input[contains(@id,'twotabsearchtextbox')]")
        search_box.click()
        search_box.send_keys("audifonos skullcandy")
        time.sleep(2)  # Let's add a small delay for stability
        search_box.send_keys(Keys.ENTER)
        print("Search performed successfully!")

        # Let's wait for a brief moment for the page to load
        time.sleep(4)

    except NoSuchElementException as e:
        print("Element not found:", str(e))

    except Exception as e:
        print("An error occurred:", str(e))

test_amazon_1()