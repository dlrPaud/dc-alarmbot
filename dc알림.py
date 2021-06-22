from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import NoSuchElementException

import time
import threading
from threading import Thread

from timeit import default_timer as timer
from datetime import timedelta

from time import gmtime, strftime
import re
from getpass import getpass
from time import sleep
 
from selenium.common.exceptions import *

import discord
from discord.ext import commands
import asyncio
 
 
EXCEPTIONS = (NoSuchElementException, ElementNotInteractableException, ElementClickInterceptedException)

options = webdriver.ChromeOptions()
#options.add_argument('--user-agent=Mozilla/5.0 (iPhone; CPU iPhone OS 10_3 like Mac OS X) AppleWebKit/602.1.50 (KHTML, like Gecko) CriOS/56.0.2924.75 Mobile/14E5239e Safari/602.1')
options.add_argument('headless')
options.add_argument("window-size=1920x1080") 
options.add_argument("disable-gpu") 
options.add_argument("disable-infobars")
options.add_argument("--disable-extensions")

#이미지 제거
chrome_prefs = {}
options.experimental_options["prefs"] = chrome_prefs
chrome_prefs["profile.default_content_settings"] = {"images": 2}
chrome_prefs["profile.managed_default_content_settings"] = {"images": 2}
driver = webdriver.Chrome(options=options)
driver.maximize_window()


client = discord.Client()
counter = 0
title = 0
link = 0


#실행
def func1():

    #값
    numlist = [0,1,2]
    numr = 0
    numb = 0
    title1 = 0
    link1 = 0
    used_link1 = 0
    used_title1 = 0
    dc_xpath = '//*[@id="container"]/section[1]/article[2]/div[3]/table/tbody/tr[3]/td[2]/a'
    dc_custom_url ='https://gall.dcinside.com/board/lists?id=pridepc_new4&s_type=search_subject_memo&s_keyword=%EC%BF%A0%ED%8C%A1'
    dc_url = 'https://gall.dcinside.com/board/lists?id=pridepc_new4'
    used_url ='https://cafe.naver.com/joonggonara?iframe_url=/joonggonara/ArticleSearchList.nhn%3Fsearch.clubid=10050146%26search.searchBy=0%26search.query=rtx%203060'
    used_xpath = '//*[@id="main-area"]/div[5]/table/tbody/tr[1]/td[1]/div[2]/div/a'
    used_writer_xpath ='//*[@id="main-area"]/div[5]/table/tbody/tr[1]/td[2]/div/table/tbody/tr/td/a'

    
    
    driver.get(dc_custom_url)

    while True:
        numr = numr + 1
        
        global counter
        global title
        global link
        global used_title
        global used_link


        if numr == 3:
            numr = 0
        
        if numlist[numr] == 1:
            link = driver.find_element_by_xpath(dc_xpath).get_attribute('href')
            title = driver.find_element_by_xpath(dc_xpath).text
        elif numlist[numr] == 2:
            link1 = driver.find_element_by_xpath(dc_xpath).get_attribute('href')
            title1 = driver.find_element_by_xpath(dc_xpath).text
        else:
            driver.get(used_url)
            driver.switch_to.frame("cafe_main")
            used_writer = driver.find_element_by_xpath(used_writer_xpath).text
            numb = numb + 1

            if numb == 2:
                numb = 0
            
            if numlist[numb] == 1:
                used_link = driver.find_element_by_xpath(used_xpath).get_attribute('href')
                used_title = driver.find_element_by_xpath(used_xpath).text
            else:
                used_link1 = driver.find_element_by_xpath(used_xpath).get_attribute('href')
                used_title1 = driver.find_element_by_xpath(used_xpath).text
    
            if used_title == used_title1:
                numb = -1
            else:
                if '채굴기'or'매입'or '노트북' in used_title:
                     print('082')
                     counter = 3
                elif '오키컴1호점' or '스토어' or '몰' or'컴' in used_writer:
                    print('082')
                    counter = 3
                else:
                    print(used_title + '\n' + used_link + '\n')
                    counter = 2

    
        if numlist[numr] == 0:
            driver.implicitly_wait(10)
            driver.get(dc_custom_url)
            
        elif title == title1:
            driver.implicitly_wait(10)
            driver.refresh()
            
            numbr = 1
        else:
            print(title + '\n' + link + '\n')
            
            counter = 1
            driver.implicitly_wait(10)
            driver.refresh()


def func2():

    async def my_background_task():
        await client.wait_until_ready()
        channel = client.get_channel(856984604573040682)
        channel2 = client.get_channel(856984460196839508)
        channel3 = client.get_channel(856984427317297153)
        msg_sent = False
        
        global counter
 
        while True:
            if counter == 1:
                embed = discord.Embed(title=title,description=link, color = 0x00ff00)
                await channel.send(embed=embed)
                
                counter = 0
            elif counter == 2:
                embed2 = discord.Embed(title=used_title,description=used_link, color = 0x00ff00)
                await channel2.send(embed=embed2)

                counter = 0
            elif counter == 3:
                embed3 = discord.Embed(title=used_title,description=used_link, color = 0x00ff00)
                await channel3.send(embed=embed3)

                counter = 0
                

        await asyncio.sleep(1)


    client.loop.create_task(my_background_task())
    client.run('ODU2OTQ1MzA3MTgxNzc2ODk3.YNIagg.LQoopctRi30aFrOyGSaBBKLbAPw')

if __name__ == '__main__':
    Thread(target = func1).start()
    Thread(target = func2).start()
 


