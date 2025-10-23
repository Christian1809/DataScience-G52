#pip install selenium
from selenium import webdriver
from selenium.webdriver.common.by import By
import time

URL ='https://www.sunat.gob.pe/'

driver = webdriver.Chrome()

try:
    driver.get(URL)
    time.sleep(3)
    precio_venta = driver.find_element(By.ID,'sell-rate').text
    print(f'Precio de venta dolares : {precio_venta}')
    
except Exception as e:
    print(f'Error : {e}')
finally:
    driver.quit()