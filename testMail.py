# coding: utf-8
import pymongo
import smtplib
import email.mime.multipart
import email.mime.text

def query_count():
    mongo_uri = '183.174.228.25:38018'
    mongodb = 'zhihu'
    collection_name = 'users'

    client = pymongo.MongoClient(mongo_uri)
    db = client[mongodb]
    #db[collection_name].update({'url_token': item['url_token']}, item, True)
    count = db[collection_name].find().count()#?
    client.close()
    print(count)
    return count

def send_email(count,toMail):
        msg = email.mime.multipart.MIMEMultipart()
        msgFrom = 'crawlzhihu@163.com'  # 从该邮箱发送
        msgTo = toMail  # 发送到该邮箱
        smtpSever = 'smtp.163.com'  # 163邮箱的smtp Sever地址
        smtpPort = '25'  # 开放的端口
        sqm = 'crawlzhihu666'  # 在登录smtp时需要login中的密码应当使用授权码而非账户密码

        msg['from'] = msgFrom
        msg['to'] = msgTo
        msg['subject'] = 'Python自动-' + str(count) + '\t统计user_token数目'
        name = '记录数：'
        content = name + ' ' + str(count)
        txt = email.mime.text.MIMEText(content)
        msg.attach(txt)
        smtp = smtplib.SMTP()
        smtp.connect(smtpSever, smtpPort)
        smtp.login(msgFrom, sqm)
        smtp.sendmail(msgFrom, msgTo, str(msg))
        smtp.quit()
def main():
	count = query_count()
	send_email(count, 'mikewxp@163.com')
	print("sendMain Done")

import time
import os
while True:
	main()
	time.sleep(3*3600)  #每3小时统计一次 发邮件
