# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://doc.scrapy.org/en/latest/topics/item-pipeline.html


class DoubanprojectPipeline(object):
    def open_spider(self,spider):

        print("*" * 50)

    def process_item(self, item, spider):

        return item


    def close_spider(self,spider):
        print("4146")