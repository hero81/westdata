# TG频道@fffffx2
from selenium.webdriver import Chrome
import time
import os

os.environ["http_proxy"] = "http://127.0.0.1:10809"
localtime = time.asctime( time.localtime(time.time()) )
print ("任务开始的时间为 :", localtime)

class spider():
    def __init__(self):
        self.url = 'https://westdata.cf/'

    def search_save_sub(self):
        chrome = Chrome()
        chrome.get(self.url)
        for i in range(1, 20000):
            parent = chrome.find_element_by_css_selector("[class='main']")
            sections = parent.find_elements_by_css_selector("[class='p']")
            file = open("OK_sub.txt", "a", encoding='UTF-8')
            urls = chrome.find_elements_by_xpath("//a")
            for suburl in urls:
                file.write(str(suburl.get_attribute("href")+ '\n'))
                print(f'=======已保存{i}条订阅=======')
                time.sleep(2)
                chrome.refresh()
            file.close()

if __name__ == '__main__':
    spider1 = spider()
    spider1.search_save_sub()
