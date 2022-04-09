from selenium import webdriver
import time
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By


driver_service = Service(executable_path="/Users/alextaraskin/Desktop/pythonProject/venv/chromedriver/chromedriver")
driver = webdriver.Chrome(service = driver_service)
#driver = webdriver.Chrome("/Users/alextaraskin/Desktop/pythonProject/venv/chromedriver/chromedriver")
try:
    driver.get("https://www.avito.ru/moskva/tovary_dlya_kompyutera/komplektuyuschie/videokarty-ASgBAgICAkTGB~pm7gmmZw?cd=1")
    print(driver.window_handles)
    print(f"Currently URL is:{driver.current_url}")
    #print(driver.window_handles )
    time.sleep(2)
    items = driver.find_elements(by=By.XPATH, value="//div[@data-marker='item-photo']")
    items[1].click()
    time.sleep(2)
    #print(driver.window_handles)
    driver.switch_to.window(driver.window_handles[1])
    print(f"Currently URL is:{driver.current_url}")
    username = driver.find_element(by=By.CLASS_NAME, value="seller-info-name js-seller-info-name")
    print(f"Username is: {username.text}")
    time.sleep(5)


except Exception as ex:
    print(ex)
finally:
    driver.close()
    driver.quit()