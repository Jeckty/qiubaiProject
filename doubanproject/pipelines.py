# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://doc.scrapy.org/en/latest/topics/item-pipeline.html
import pymysql

class DoubanprojectPipeline(object):
    def open_spider(self,spider):

        self.db = pymysql.connect("192.168.171.129", "jeckty", "941010", "zty",charset='utf8')
        self.cursor = self.db.cursor()


    def process_item(self, item, spider):
        sql = 'insert into qiutu ( name, age,content) values("%s", "%s","%s")' % (item['name'], 25,item['content'] )

        try:
            self.cursor.execute(sql)
            print("#" * 50)
            self.db.commit()
        except Exception as e:
            print('*' * 10)
            print(e)
            self.db.rollback()

        return item


    def close_spider(self,spider):
        self.cursor.close()
        self.db.close()
