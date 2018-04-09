import time
import os

while True:
    os.system("scrapy crawl zhihu")
    time.sleep(24*3600)  #每个一天run一次
