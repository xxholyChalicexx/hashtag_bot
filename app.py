from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.firefox.options import Options

import time

class InstagramBot:
    def __init__(self, tag):
        options = Options()
        options.headless = True
        self.tag = tag
        self.bot = webdriver.Firefox(options=options)

    def get_like(self):
        bot = self.bot
        url = f'https://www.instagram.com/explore/tags/{self.tag}/'
        bot.get(url)
        time.sleep(3)
        images = bot.find_elements_by_class_name('v1Nh3')
        time.sleep(3)
        sum = 0
        for i in range(0,9):
            images[i].click()
            time.sleep(3)
            # this try tag is used because sometime it seems like the top 9 post, if video is included, it seems to not able to recognize some element
            try:
                likes = bot.find_element_by_class_name('_8A5w5').text
            except:
                continue
            likes_number = likes.split(' ')[0].replace(',','')#spliting string to extract number of likes 
            sum += int(likes_number)
            close = bot.find_element_by_class_name('ckWGn')
            close.click()

        avg = sum/9
        print(avg)  
        # images[0].click()
        # time.sleep(3)
        # likes = bot.find_element_by_class_name('_8A5w5').text
        # print(likes)
        # a = likes.split(' ')[0].replace(',','')#spliting string to extract number of likes 
        # print(int(a) + 1)

        # username = bot.find_element_by_name('username')
        # password = bot.find_element_by_name('password')
        # username.clear()
        # password.clear()
        # username.send_keys(self.username)
        # password.send_keys(self.password)
        # password.send_keys(Keys.RETURN)
        # time.sleep(3)
        # not_now = bot.find_element_by_class_name('HoLwm')
        # not_now.click()


file = open('tags.txt')
tags = file.read()
tags_list = tags.splitlines()
print(tags_list)
for i in tags_list:
    chibi = InstagramBot(i)
    chibi.get_like()
