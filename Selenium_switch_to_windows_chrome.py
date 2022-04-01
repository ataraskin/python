from selenium import webdriver
import time
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By


driver_service = Service(executable_path="/Users/alextaraskin/Desktop/pythonProject/venv/chromedriver/chromedriver")
driver = webdriver.Chrome(service = driver_service)
#driver = webdriver.Chrome("/Users/alextaraskin/Desktop/pythonProject/venv/chromedriver/chromedriver")
try:
    driver.get("https://www.avito.ru/moskva/tovary_dlya_kompyutera/komplektuyuschie/videokarty-ASgBAgICAkTGB~pm7gmmZw?cd=1")
    time.sleep(5)
    items = driver.find_elements(by=By.XPATH, value="//div[@data-marker='item-photo']")
    items[0].click()
    time.sleep(5)
except Exception as ex:
    print(ex)
finally:
    driver.close()
    driver.quit()