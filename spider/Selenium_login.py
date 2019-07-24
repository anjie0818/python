# -*- coding:utf-8 -*-

# douban.py
#coding=utf-8
import time
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.options import Options

class Douban():
    def __init__(self):
        chrome_options = Options()
        chrome_options.add_argument('--headless')
        chrome_options.add_argument('--disable-gpu')

        # export PATH=$PATH:/Users/v_anjie01/PycharmProjects/python/spider/chromedriver
        self.url = "https://www.douban.com/"
        # self.driver = webdriver.PhantomJS(
        #     executable_path="/Users/v_anjie01/PycharmProjects/python/phantomjs-2.1.1-macosx/bin/phantomjs")
        self.driver = webdriver.Chrome(executable_path="/Users/v_anjie01/PycharmProjects/python/spider/chromedriver",options=chrome_options)
    def log_in(self):
        self.driver.get(self.url)
        time.sleep(3)#睡3分钟，等待页面加载
        self.driver.switch_to.frame(self.driver.find_element_by_tag_name("iframe"))
        self.driver.find_element_by_class_name("account-tab-account").click()
        self.driver.save_screenshot("01.jpg")

        #输入账号
        self.driver.find_element_by_id('username').send_keys("18636657014")
        #输入密码
        self.driver.find_element_by_id('password').send_keys("anjie123B")
        #点击登陆
        self.driver.find_element_by_class_name("account-form-field-submit").click()
        time.sleep(2)
        self.driver.save_screenshot("douban.jpg")
        #输出登陆之后的cookies
        print(self.driver.get_cookies())

    def __del__(self):
        '''调用内建的稀构方法，在程序退出的时候自动调用
        类似的还可以在文件打开的时候调用close，数据库链接的断开
        '''
        self.driver.quit()

if __name__ == "__main__":
    douban = Douban() #实例化
    douban.log_in() #之后调用登陆方法