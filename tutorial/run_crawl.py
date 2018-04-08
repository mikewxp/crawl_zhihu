import time
import os

while True:
    os.system("scrapy crawl zhihu")
    time.sleep(173800)  #每隔两天运行一次 24*60*60*2=173800s
