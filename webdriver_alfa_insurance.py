

from selenium import webdriver
import time
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.action_chains import ActionChains

driver_service=Service(executable_path="/Users/alextaraskin/Desktop/learning_python/chromedriver")
driver=webdriver.Chrome(service=driver_service)
driver.maximize_window()


try:
    driver.get("https://www.alfastrah.ru/individuals/auto/eosago/calc/min/")
    driver.execute_script("window.scrollTo(0, 300)")
    city = driver.find_element(by=By.ID, value="city")
    city.send_keys("Москва")
    city.send_keys(Keys.ENTER)

    time.sleep(1)
    auto = driver.find_element(by=By.CSS_SELECTOR, value='#mark')
    auto.send_keys("УАЗ")
    time.sleep(1)
    auto_model = driver.find_element(by=By.CSS_SELECTOR, value='#model')
    auto_model.send_keys('PATRIOT')
    time.sleep(1)
    auto_year = driver.find_element(by=By.CSS_SELECTOR, value='#year-release')
    auto_year.send_keys('2021')

    time.sleep(3)
    driver.execute_script("window.scrollTo(0, 600)")
    auto_modification = driver.find_element(by=By.XPATH, value="//span[@class='select2-selection__rendered']").click()
    time.sleep(3)
    auto_modification_choice = driver.find_element(by=By.XPATH, value="//li[@class='select2-results__option'][1]").click()

    time.sleep(3)
    age = driver.find_element(by=By.CSS_SELECTOR, value='#age')
    age.send_keys(40)


    time.sleep(3)
    drive_age = driver.find_element(by=By.CSS_SELECTOR, value='#experience')
    drive_age.send_keys(20)
    driver.execute_script("window.scrollTo(0, 800)")

    time.sleep(3)
    price_osago = driver.find_element(by=By.XPATH, value="//button[@type='button']").click()


    time.sleep(10)
except Exception as ex:
    print(ex)
finally:
    driver.close()
    driver.quit()