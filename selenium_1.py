import time

from selenium import webdriver
url = "https://www.bing.com/search?q=install+python&qs=LS&pq=install+&sc=10-8&cvid=4F2E0881485C48699587E93827B222B6&FORM=QBRE&sp=1&ghc=1&lq=0&sm=csrmain"
driver = webdriver.Chrome()
driver.maximize_window()
driver.get(url)
time.sleep(5)

