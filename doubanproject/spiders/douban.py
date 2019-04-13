# -*- coding: utf-8 -*-
import scrapy
from doubanproject.items import DoubanprojectItem
from urllib import request


class DoubanSpider(scrapy.Spider):
    name = 'douban'
    allowed_domains = ['www.qiushibaike.com']
    start_urls = ['http://www.qiushibaike.com/text/']
    basic_url= "https://www.qiushibaike.com/text/page/{}/"
    items = []
    page=1

    def parse(self, response):

        div_list= response.xpath("//div[@id='content-left']/div")
        for odiv in div_list:
            item = DoubanprojectItem()
            item['name']=odiv.xpath(".//div//h2/text()").extract_first().strip()
            item['sex']=odiv.xpath(".//div/div/@class").extract_first()
            item['age']=odiv.xpath(".//div[@class='author clearfix']//div/text()").extract_first()
            if item['age']==None :
                item['age']='0'
            content=odiv.xpath(".//a[1]/div/span")
            item['content'] = content[0].xpath("string(.)").extract_first().strip()
            yield item
            self.items.append(item)
        if self.page <= 0:
            self.page+=1
            url=self.basic_url.format(self.page)

            yield scrapy.Request(url,callback=self.parse)




