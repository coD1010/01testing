import time
from selenium import webdriver
from selenium.webdriver import Keys, ActionChains
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

driver = webdriver.Chrome()
url = 'https://www.costco.com/'
driver.get(url)
driver.maximize_window()
time.sleep(3)

def test_costo_login():
    Sign_in = driver.find_element(By.XPATH,"//a[contains(@id,'in')][@class='myaccount'][contains(.,'Sign In / Register')]")
    assert Sign_in.text == "Sign In / Register"
    Sign_in.click()
    time.sleep(3)
    EMAIL_ADRESS = driver.find_element(By.XPATH,"//input[contains(@id,'signInName')]")
    EMAIL_ADRESS.click()
    EMAIL_ADRESS.send_keys("salvador121@live.com")
    time.sleep(3)
    password = driver.find_element(By.XPATH,"//input[contains(@id,'password')]")
    password.click()
    password.send_keys("Sp101495!")
    time.sleep(3)
    sign_in_button = driver.find_element(By.XPATH,"//button[contains(@id,'next')]")
    sign_in_button.click()
    time.sleep(5)

def test_buscar_un_producto():
    search = driver.find_element(By.XPATH,"//input[@id='search-field']")
    search.click()
    search.send_keys("Bacon",Keys.ENTER)
    time.sleep(3)
    element_1 = driver.find_element(By.XPATH,"//img[contains(@automation-id,'productImageLink_3')]")
    driver.execute_script("arguments[0].scrollIntoView();",element_1)
    time.sleep(3)
    actions = ActionChains(driver)
    actions.move_to_element(element_1).perform()
    time.sleep(3)
    quick_view = driver.find_element(By.XPATH,"(//div[contains(.,'Quick View')])[28]")
    quick_view.click()
    time.sleep(3)
    view_details = driver.find_element(By.XPATH,"//a[@href='https://www.costco.com/northwest-fish%e2%80%99s-2030-bacon-wrapped-scallops%2c-(32-lbs.-per-pack)%2c-3-total-packs%2c-6-lbs.-total.product.100696175.html']")
    view_details.click()
    time.sleep(3)
    add_to_cart = driver.find_element(By.XPATH,"//input[@id='add-to-cart-btn']")
    add_to_cart.click()
    time.sleep(10)
    view_cart_button = driver.find_element(By.XPATH,"//a[@automation-id='viewCartButton']")
    view_cart_button.click()
    time.sleep(5)
    home = driver.find_element(By.XPATH,"//img[@automation-id='headerCostcoLogo']")
    home.click()
    time.sleep(5)

"""
este es mismo procedieminto que el de arriba, solo busca un objeto diferente y uso una explicit wait
el explicit wait es para esperar a que se genere el carrito en la parte final del script
"""
def test_buscar_un_producto_con_explicitwait():
    search = driver.find_element(By.XPATH,"//input[@id='search-field']")
    search.click()
    search.send_keys("Meat",Keys.ENTER)
    time.sleep(3)
    element_1 = driver.find_element(By.XPATH,"//img[contains(@automation-id,'productImageLink_5')]")
    driver.execute_script("arguments[0].scrollIntoView();",element_1)
    time.sleep(3)
    actions = ActionChains(driver)
    actions.move_to_element(element_1).perform()
    time.sleep(3)
    quick_view = driver.find_element(By.XPATH,"(//div[@class='quick-view-button'])[6]")
    quick_view.click()
    time.sleep(3)
    view_details = driver.find_element(By.XPATH,"//a[@href='https://www.costco.com/great-southern-grass-fed-beef%2c-abf-ny-strip-cc-steak%2c(1412-oz.-per-steak)%2c-14-total-packs%2c-10.5-lbs.-total.product.100229631.html']")
    view_details.click()
    time.sleep(3)
    add_to_cart = driver.find_element(By.XPATH,"//input[contains(@id,'add-to-cart-btn')]")
    add_to_cart.click()
    WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.XPATH, "//a[@automation-id='viewCartButton']")))
    #WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.ID, "myElement")))
    view_cart_button = driver.find_element(By.XPATH, "//a[@automation-id='viewCartButton']")
    view_cart_button.click()
    time.sleep(5)
    home = driver.find_element(By.XPATH,"//img[@automation-id='headerCostcoLogo']")
    home.click()
    time.sleep(5)

#def test_navigate_tabs():

##driver.close()