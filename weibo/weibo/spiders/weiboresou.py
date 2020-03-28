# -*- coding: utf-8 -*-
import scrapy
import time
from ..items import WeiboItem

header = 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/70.0.3538.77 Safari/537.36'

class WeiboresouSpider(scrapy.Spider):
    name = 'weiboresou'
    allowed_domains = ['s.weibo.com']
    start_urls = ['https://s.weibo.com/top/summary?cate=realtimehot']

    def parse(self, response):
        base_url = 'https://s.weibo.com/'
        resouurlList = []
        templist = response.xpath('//*[@id="pl_top_realtimehot"]/table/tbody/tr')

        #将广告删掉
        #广告判断标准：后边标志是‘荐’
        for temp in templist[:40]:
            if(len(temp.xpath('./td[3]//text()').extract()) and temp.xpath('./td[3]/i/text()').extract()[0] == '荐'):
                pass
            else:    
                resouurlList.append(temp.xpath('./td[2]/a/@href').extract()[0])
                
                ##print(temp.xpath('./td[2]/a/@href').extract())
            
        for resouurl in resouurlList:
            url = base_url + resouurl
            yield scrapy.Request(url=url,callback=self.parse_html,dont_filter=True,headers={"User-Agent":header})
            time.sleep(3)
        
        
    def parse_html(self,response):
        url = str(response.url)
        leadNews = ''
        if(len(response.xpath('//*[@id="pl_feedlist_index"]/div[1]/div[1]/div/p/text()'))>0):
            leadNews = response.xpath('//*[@id="pl_feedlist_index"]/div[1]/div[1]/div/p/text()').extract()[0]      
        else:
            if(len(response.xpath('//*[@id="pl_feedlist_index"]//div[2]/div[1]/div[2]/p[1]'))>0):
                temps = response.xpath('//*[@id="pl_feedlist_index"]//div[2]/div[1]/div[2]/p[1]')[0]
                for i in temps.xpath('.//text()').extract():
                    leadNews += i
                leadNews = leadNews.strip()[:-10]
            #leadNews = 'i dont know'
        if(len(response.xpath('//*[@id="pl_topic_header"]/div[1]/div/div[1]/h1/a//text()').extract())>0):
            title = response.xpath('//*[@id="pl_topic_header"]/div[1]/div/div[1]/h1/a//text()').extract()[0]
        else:
            title = '我也不知道为什么没有'
        
        item = WeiboItem()
        item['url'] = url 
        item['leadNews'] = leadNews
        item['title'] = title 
        yield item

    