from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time
import os

class Tinderbot:
    def __init__(self, username, password):
        self.username = username
        self.password = password
        self.bot = webdriver.Chrome()

    def closeBrowser(self):
        self.bot.close()

    def login(self):
        bot = self.bot
        bot.get('https://tinder.com/')
        time.sleep(15)
        bot.find_element_by_css_selector("[aria-label='Zaloguj się przez Google']").click()
        base_window = self.bot.window_handles[0]
        self.bot.switch_to_window(self.bot.window_handles[1])
        time.sleep(10)
        email_in = self.bot.find_element_by_xpath('//*[@id="identifierId"]')
        email_in.send_keys(self.username)
        self.bot.find_element_by_xpath('//*[@id="identifierNext"]').click()
        time.sleep(10)
        password_in = self.bot.find_element_by_name("password")
        password_in.send_keys(self.password)
        self.bot.find_element_by_xpath('//*[@id="passwordNext"]').click()
        time.sleep(10)
        self.bot.switch_to_window(base_window)
        time.sleep(5)
        bot.find_element_by_css_selector("[aria-label='Zezwól']").click()
        time.sleep(5)
        bot.find_element_by_css_selector("[aria-label='Nie interesuje mnie to']").click()
        time.sleep(5)
        bot.find_element_by_xpath("//span[text()='Wyrażam zgodę']").click()
        time.sleep(5)

    def like(self):
        bot = self.bot
        bot.find_element_by_css_selector("[aria-label='Polub']").click()
    
    def dislike(self):
        bot = self.bot
        bot.find_element_by_css_selector("[aria-label='Żegnam']").click()

    def close_match(self):
        bot = self.bot
        bot.find_element_by_xpath("//a[text()='Wróć do Tindera']").click()

    def close_popup(self):
        bot = self.bot
        bot.find_element_by_xpath("//span[text()='Nie interesuje mnie to']").click()

    def close_popup_premium(self):
        bot = self.bot
        bot.find_element_by_xpath("//span[text()='Nie, dziękuję']").click()

    def auto_swipe(self):
        from random import random
        while True:
            time.sleep(.5)
            try:
                rand = random()
                if rand < .73:
                    user.like()
                else:
                    user.dislike()
            except Exception:
                try:
                    user.close_match()
                except Exception:
                    try:
                        user.close_popup()
                    except Exception:
                        user.close_popup_premium()

# The bot log in Tinder with Google, so your Tinder account must be connceted with your google account.
# Change "username" and "password" on your Gmail username and password to log in to your Tinder account.
user = Tinderbot('username', 'password')

user.login()
user.auto_swipe()

# If you wanna use the bot change website language on Polish.