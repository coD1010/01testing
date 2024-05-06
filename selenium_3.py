import time
from selenium import webdriver
from selenium.webdriver import Keys
from selenium.webdriver.common.by import By

driver = webdriver.Chrome()
url = 'https://www.mercadolibre.com.mx/'
driver.get(url)
driver.maximize_window()
time.sleep(3)

def test_mercado_login():
   login = driver.find_element(By.XPATH,"//a[@href='https://www.mercadolibre.com/jms/mlm/lgz/login?platform_id=ML&go=https%3A%2F%2Fwww.mercadolibre.com.mx%2F&loginType=explicit#nav-header']")
   assert login.text == 'Ingresa'
   login.click()
   correo = driver.find_element(By.XPATH,"//input[contains(@data-testid,'user_id')]")
   correo.send_keys("andresrtomero@gmail.com")
   time.sleep(2)
   btn_continuar = driver.find_element(By.XPATH,"//span[@class='andes-button__content'][contains(.,'Continuar')]")
   assert btn_continuar.text == 'Continuar'
   btn_continuar.click()
   time.sleep(10)


def test_mercado_skull_agregar_carrito():
   search_box = (driver.find_element(By.ID,"cb1-edit"))
   search_box.click()
   search_box.send_keys("audifonos skullcandy")
   time.sleep(2)
   search_box.send_keys(Keys.ENTER)
   time.sleep(2)
   audifonos_mamalonns = driver.find_element(By.XPATH,"(//h2[@aria-level='3'][contains(.,'Audífonos Inalámbricos Over-ear Hesh Anc Skullcandy')])[1]")
   driver.execute_script("arguments[0].scrollIntoView();", audifonos_mamalonns)
   assert audifonos_mamalonns.text == "Audífonos Inalámbricos Over-ear Hesh Anc Skullcandy"
   time.sleep(3)
   audifonos_mamalonns.click()
   time.sleep(5)
   #driver.execute_script("window.scrollTo(0, document.body.scrollHeight);") #script de java para hacert scroll down para scrolear a un elemento en especifico, utiliza este codigo
   # Or to scroll to a specific element:
   # element = driver.find_element(By.XPATH, "//div[@id='my_element']")
   # driver.execute_script("arguments[0].scrollIntoView();", element)
   agregar_carrito = driver.find_element(By.XPATH,"(//span[@class='andes-button__content'][contains(.,'Agregar al carrito')])[1]")
   assert agregar_carrito.text == "Agregar al carrito"
   agregar_carrito.click()
   time.sleep(4)

def test_mercado_skull_compar_ahora():
   search_box = (driver.find_element(By.ID,"cb1-edit"))
   search_box.click()
   search_box.send_keys("audifonos skullcandy")
   time.sleep(2)
   search_box.send_keys(Keys.ENTER)
   time.sleep(2)
   audifonos_mamalonns = driver.find_element(By.XPATH,"(//h2[@aria-level='3'][contains(.,'Audífonos Inalámbricos Over-ear Hesh Anc Skullcandy')])[1]")
   driver.execute_script("arguments[0].scrollIntoView();", audifonos_mamalonns)
   assert audifonos_mamalonns.text == "Audífonos Inalámbricos Over-ear Hesh Anc Skullcandy"
   time.sleep(3)
   audifonos_mamalonns.click()
   time.sleep(5)
   comprar_ahora = driver.find_element(By.XPATH,"(//span[contains(.,'Comprar ahora')])[1]")
   assert comprar_ahora.text == "Comprar ahora"
   comprar_ahora.click()
   time.sleep(4)

#driver.quit()