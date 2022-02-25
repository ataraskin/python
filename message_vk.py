from selenium import webdriver
import time
from selenium.webdriver.common.keys import Keys
from auth_date import vk_password, message
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

driver_service = Service(executable_path="/Users/alextaraskin/Desktop/pythonProject/venv/chromedriver/chromedriver")
driver = webdriver.Chrome(service = driver_service)
#driver = webdriver.Chrome("/Users/alextaraskin/Desktop/pythonProject/venv/chromedriver/chromedriver")
try:
    driver.get("https://vk.com")
    time.sleep(1)
    email_input = driver.find_element(By.ID, "index_email")
    email_input.clear()
    email_input.send_keys("89850938509")
    time.sleep(1)

    password_input = driver.find_element(By.ID, "index_pass")
    password_input.clear()
    password_input.send_keys(vk_password)
    time.sleep(1)

    login_button = driver.find_element(By.ID, "index_login_button").click()
    time.sleep(2)
    friends = driver.find_element(By.ID, "l_fr").click()
    time.sleep(2)
    search_people = driver.find_element(By.ID, "s_search")
    search_people.send_keys("Алексей Тараскин")
    time.sleep(2)
    enter_friends = driver.find_element(By.CLASS_NAME, "friends_field_act").click()
    time.sleep(2)
    message_friend = driver.find_element(By.CSS_SELECTOR, "#mail_box_editable")
    message_friend.send_keys(message)
    message_friend.send_keys(Keys.ENTER)
    time.sleep(2)
    message_send = driver.find_element(By.ID, "mail_box_send").click()
    time.sleep(2)
except Exception as ex:
    print(ex)
finally:
    driver.close()
    driver.quit()