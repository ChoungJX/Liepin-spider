# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: http://doc.scrapy.org/en/latest/topics/item-pipeline.html


class LiepinPipeline(object):
    def process_item(self, item, spider):
        z = item['All']
	y = z.split('_')
        x = ('Annual_salary','Work_location','Education','Hands_on_background')
        for i in range(0,len(y)):
            item[x[i]] = y[i]
        return item
