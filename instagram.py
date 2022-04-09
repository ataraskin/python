from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from auth_date import username, password
import time
import random


# def login(username, password):
#browser_service=Service(executable_path='/Users/alextaraskin/Desktop/learning_python/chromedriver')
#browser=webdriver.Chrome(service=browser_service)

#         try:
#             browser_service=Service(executable_path='/Users/alextaraskin/Desktop/learning_python/chromedriver')
#             browser=webdriver.Chrome(service=browser_service)
#             browser.get("https://www.instagram.com/")
#             time.sleep(random.randrange(3, 5))
#             button_cookies=browser.find_element(by=By.XPATH, value="//button[@class='aOOlW  bIiDR  ']").click()
#             time.sleep(3)
#
#             login_input=browser.find_element(by=By.XPATH, value="//input[@name='username']")
#             login_input.send_keys(username)
#
#             password_input=browser.find_element(by=By.XPATH, value="//input[@name='password']")
#             password_input.send_keys(password)
#             password_input.send_keys(Keys.ENTER)
#             time.sleep(7)
#
#             notification_button=browser.find_element(by=By.XPATH, value="//button[@class='aOOlW   HoLwm ']").click()
#             time.sleep(5)
#
#             browser.close()
#             browser.quit()
#         except Exception as ex:
#             print(ex)
#             browser.close()
#             browser.quit()
# login(username, password)

def hashtag_search(userrname, password, hashtag):
    browser_service=Service(executable_path='/Users/alextaraskin/Desktop/learning_python/chromedriver')
    browser=webdriver.Chrome(service=browser_service)

    try:
        browser.get("https://www.instagram.com/")
        time.sleep(random.randrange(3, 5))
        button_cookies=browser.find_element(by=By.XPATH, value="//button[@class='aOOlW  bIiDR  ']").click()
        time.sleep(3)

        login_input=browser.find_element(by=By.XPATH, value="//input[@name='username']")
        login_input.send_keys(username)

        password_input=browser.find_element(by=By.XPATH, value="//input[@name='password']")
        password_input.send_keys(password)
        password_input.send_keys(Keys.ENTER)
        time.sleep(7)

        notification_button=browser.find_element(by=By.XPATH, value="//button[@class='aOOlW   HoLwm ']").click()
        time.sleep(5)

        try:
            browser.get(f'https://www.instagram.com/{hashtag}')
            time.sleep(5)
            for i in range(1, 4):
                browser.execute_script("window.scrollTo(0, document.body.scrollHeight);")
                time.sleep(random.randrange(3, 5))

            hrefs=browser.find_elements(by=By.TAG_NAME, value='a')

            posts_urls=[]
            for item in hrefs:
                href=item.get_attribute('href')
                if "/p/" in href:
                    posts_urls.append(href)
            print(posts_urls)

            for url in posts_urls:
                try:
                    browser.get(url)

                    like_button=browser.find_element(by=By.XPATH, value="//span[@class='fr66n']").click()
                    time.sleep(random.randrange(1, 5))
                except Exception as ex:
                    print(ex)


        except Exception as ex:
            print(ex)



            browser.close()
            browser.quit()
    except Exception as ex:
        print(ex)
        browser.close()
        browser.quit()

hashtag_search(username, password, 'surfing')

