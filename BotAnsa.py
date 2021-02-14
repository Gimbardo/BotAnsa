import sys
import time
from selenium import webdriver
from time import sleep
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


PATH = "C:\Program Files (x86)\chromedriver\chromedriver.exe"




class BotAnsa:
    """A bot that reades the first articles on ansa.it and writes them on a file"""
    def __init__(self,filter="",numberofnews=5,filename = 'news.txt'):
        self.driver = webdriver.Chrome(PATH)
        self.driver.get("https://www.ansa.it/")
        self.filter=filter
        self.numberofnews=numberofnews
        self.filename=filename

        self._closecookies()
        self._takenews()
        self._close()

    def _closecookies(self):
        """A function that closes cookies"""
        try:
            cookie = WebDriverWait(self.driver, 10).until(
                EC.presence_of_element_located((By.CLASS_NAME, "iubenda-cs-close-btn"))
            )
        except:
            self.driver.quit()
        
        link = self.driver.find_element_by_class_name("iubenda-cs-close-btn")
        link.click()
        
    def _takenews(self):
        """Core Function: this writes news on a file"""

        #encoding utf-8 is needed to write also italian accents
        fileNews = open(self.filename, "w",encoding='utf-8')

        fileNews.write(time.ctime(time.time())+'\n\n')

        try:
            all = WebDriverWait(self.driver, 10).until(
                EC.presence_of_element_located((By.CLASS_NAME, 'extra-container'))
            )
            articles = all.find_elements_by_tag_name('article')
            
            for i in range(self.numberofnews):

                #first news is different from the others
                if i==0:
                    information=articles[i].find_element_by_class_name('pp-img').text+'\n'+articles[i].find_element_by_class_name('pp-abs').text+'\n\n'
                    if self.filter in information:
                        fileNews.write(information)
                else:
                    information=articles[i].find_element_by_tag_name('header').text+'\n'+articles[i].find_element_by_class_name('pp-abs').text+'\n\n'
                    if self.filter in information:
                        fileNews.write(information)

        except:
            #only if site is unreachable in 10 seconds
            self.driver.quit()

        fileNews.close()

    def _close(self):
        """Function used to close chromedriver"""
        self.driver.quit()

    def print(self):
        """Function that prints want's inside our file"""
        fileNews = open(self.filename, "r",encoding='utf-8')
        print(fileNews.read())




#main of our script

if len(sys.argv) == 1:
    bot = BotAnsa()
else:
    if len(sys.argv) == 2:
        bot = BotAnsa(sys.argv[1])
    else:
        if len(sys.argv) == 3:
            bot = BotAnsa(sys.argv[1],int(sys.argv[2]))
        else:
            bot = BotAnsa(sys.argv[1],int(sys.argv[2]),sys.argv[3])