import os
from selenium import webdriver
from internet_speed_bot import InternetSpeedTwitterBot

PROMISED_DOWN = 150
PROMISED_UP = 10
CHROME_DRIVER_PATH= ''
TWITTER_EMAIL= os.environ.get("email", "Couldn't find email address")
TWITTER_PASSWORD = os.environ.get("password", "Couldn't find password")


internet_speed_bot = InternetSpeedTwitterBot()
internet_speed_bot.get_internet_speed()
internet_speed_bot.tweet_at_provider()
