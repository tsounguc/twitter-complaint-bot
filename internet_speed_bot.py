import time

from selenium import webdriver
from selenium.webdriver.common.by import By


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
        pass

