# -*- coding: utf-8 -*-
import scrapy
from doubanproject.items import DoubanprojectItem
from urllib import request


class DoubanSpider(scrapy.Spider):
    name = 'douban'
    allowed_domains = ['www.qiushibaike.com']
    start_urls = ['http://www.qiushibaike.com/text/']
    basic_url= "https://www.qiushibaike.com/text/page/{}/"
    page=1

    def parse(self, response):

        div_list= response.xpath("//div[@id='content-left']/div")
        for odiv in div_list:
            item = DoubanprojectItem()
            #name
            item['name']=odiv.xpath(".//div//h2/text()").extract_first().strip()
            print(item['name'])

            #sex
            sex= odiv.xpath(".//div/div/@class").extract_first()
            if item['name'] !="匿名用户":
                sex= sex.split(' ')[1]
                sex=sex[:-4]
            print(sex)
            item['sex']=sex

            #age
            item['age']=odiv.xpath(".//div[@class='author clearfix']//div/text()").extract_first()
            if item['name'] == "匿名用户":
                item['age']='0'

            #content
            content=odiv.xpath(".//a[1]/div/span")
            item['content'] = content[0].xpath("string(.)").extract_first().strip()
            yield item

        if self.page <= 40:
            self.page+=1
            url=self.basic_url.format(self.page)

            yield scrapy.Request(url,callback=self.parse)




