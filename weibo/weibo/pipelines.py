# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html
from  scrapy import signals
from scrapy.mail import MailSender

class WeiboPipeline(object):
    def __init__(self):
        pass

    
    def process_item(self, item, spider):
        fpath = 'E:\\Compile Tools\\python\\virEnvProject\\test\\Scripts\\weibo\\weibo.txt'
        with open(fpath,'a',encoding='utf-8') as f:
            
            f.write('标题: '+str(item['title'])+'\n')
            f.write('导语：'+str(item['leadNews'])+'\n')
            f.write('链接：'+str(item['url'])+'\n')
            f.write('\n')
        
        return item
    def close_spider(self,spider):
        mailer = MailSender(
            smtphost='smtp.qq.com',
            mailfrom='xxxxx@qq.com',
            smtpuser='xxxxx@qq.com',
            smtppass='授权码',
            smtpport=25
        )
        body = ''
        fpath = 'E:\\Compile Tools\\python\\virEnvProject\\test\\Scripts\\weibo\\weibo.txt'
        with open(fpath,'r',encoding='utf-8') as f:
            body = f.read()
        
        subject = u'微博热搜'
        mailer.send(to=['920873304@qq.com'],subject=subject,
                    body=body)
        #with open(fpath,'r+') as f:
        #    f.seek(0)
        #    f.truncate()
        #self.clien.close()

