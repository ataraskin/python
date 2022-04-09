from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from auth_date import username, password
import time
import random
from selenium.common.exceptions import NoSuchElementException


class InstagramBot():
    def __init__(self, username, password):

        self.username = username
        self.password = password
        self.browser_service=Service(executable_path='/Users/alextaraskin/Desktop/learning_python/chromedriver')
        self.browser = webdriver.Chrome(service=browser_service)

    def close_browser(self):

        self.browser.close()
        self.browser.quit()

    def login(self):

        browser = self.browser
        browser_service = Service(executable_path='/Users/alextaraskin/Desktop/learning_python/chromedriver')
        browser=webdriver.Chrome(service=browser_service)
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

    def like_photo_by_hashtag(self, hashtag):
        browser = self.browser
        browser.get(f'https://www.instagram.com/{hashtag}')
        time.sleep(5)
        for i in range(1, 4):
            browser.execute_script("window.scrollTo(0, document.body.scrollHeight);")
            time.sleep(random.randrange(3, 5))

        hrefs = browser.find_elements(by=By.TAG_NAME, value='a')

        posts_urls = []
        for item in hrefs:
            href = item.get_attribute('href')
            if "/p/" in href:
                posts_urls.append(href)
        print(posts_urls)

        for url in posts_urls:
            try:
                browser.get(url)

                like_button = browser.find_element(by=By.XPATH, value="//span[@class='fr66n']").click()
                time.sleep(random.randrange(80, 100))
            except Exception as ex:
                print(ex)
                self.close_browser()
    #проверяем существует ли  элемент на странице
    def xpath_exists(self, url):

        browser = self.browser
        try:
            browser.find_element(by=By.XPATH, value=url)
            exist = True
        except NoSuchElementExeption:
            exist = False
        return exist
    def put_exatly_like(self, userpost):
        browser = self.browser
        browser.get(userpost)
        time.sleep(4)

        wrong_userpage = "//h2[@class='_7UhW9      x-6xq     qyrsm KV-D4          uL8Hv     l4b0S    ']"
        if self.xpath_exists(wrong_userpage):
            print("Такого поста не существуетб проверьте URL ")
            self.close_browser()
        else:
            print("Пост успешно найден, ставим лайк!")
            time.sleep(2)

            like_button =






