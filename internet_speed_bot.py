import os
import time

from selenium import webdriver
from selenium.webdriver import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC



class InternetSpeedTwitterBot:
    def __init__(self):
        options = webdriver.ChromeOptions()
        options.add_experimental_option('detach', True)
        self.driver = webdriver.Chrome(options=options)
        self.down = 0
        self.up = 0

    def get_internet_speed(self):
        self.driver.get("https://www.highspeedinternet.com/tools/speed-test")
        self.driver.maximize_window()
        go_button = self.driver.find_element(By.CLASS_NAME, "start-speed-test")
        go_button.click()
        time.sleep(30)
        self.up = float(self.driver.find_element(By.CLASS_NAME, "speed-upload").text.split(" ")[0])
        self.down = float(self.driver.find_element(By.CLASS_NAME, "speed-download").text.split(" ")[0])
        print(f"Download speed: {self.down} Mbps")
        print(f"Upload speed: {self.up} Mbps")

    def tweet_at_provider(self):
        self.driver.get("https://twitter.com/")

        time.sleep(10)
        sign_in_button = self.driver.find_element(By.XPATH, '//*[@id="react-root"]/div/div/div[2]/main/div/div/div['
                                                            '1]/div[1]/div/div[3]/div[5]/a/div')
        sign_in_button.click()

        # time.sleep(10)
        # sign_in_window = self.driver.window_handles[1]
        # self.driver.switch_to.window(sign_in_window)

        google_button = WebDriverWait(self.driver, 15).until(EC.presence_of_element_located((By.XPATH, '//*[@id="container"]/div/div[2]/span[1]')))
        google_button.click()

        time.sleep(10)
        sign_in_window = self.driver.window_handles[1]
        self.driver.switch_to.window(sign_in_window)

        email = os.environ.get("email", "Couldn't find email address")
        username = os.environ.get("username", "Couldn't find username")
        password = os.environ.get("password", "Couldn't find password")

        email_input = self.driver.find_element(By.XPATH, '//*[@id="identifierId"]')
        email_input.send_keys(email)
        email_input.send_keys(Keys.ENTER)
