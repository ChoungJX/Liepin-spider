# -*- coding: utf-8 -*-
import scrapy
from scrapy.http import Request
from LiePin.items import LiepinItem
import re

class LiepinSpider(scrapy.Spider):
    name = "liepin"
    allowed_domains = ["liepin.com"]
    KaGi = '客户经理' #输入想搜索的职位
    start_urls = (
        'https://www.liepin.com/zhaopin/?key='+KaGi,
    )

    def parse(self, response):
        url_x = response.xpath('//a[@class="last"]').extract()
        ZZ = 'curPage=[0-9]{1,20}'
        url_xx = re.compile(ZZ).findall(url_x[0])
        ZZ2 = '[0-9]{1,20}'
        url_xxx = re.compile(ZZ2).findall(url_xx[0])
        print url_xx
        for i in range(0,int(url_xxx[0])):
            url2 = 'https://www.liepin.com/zhaopin/?key='+LiepinSpider.KaGi+'&curPage='+str(i)
            yield Request(url2, callback=self.next)


    def next(self,response):
        self.item = LiepinItem()
        e=[]
        f=[]
        g=[]
        h = []
        Position_x = response.xpath('//div[@class="job-info"]/span/@title')
        for i in Position_x:
            e.append(i.extract())
        Company_x = response.xpath('//p[@class="company-name"]/a/@title')
        for j in Company_x:
            f.append(j.extract())
        All_x = response.xpath('//p[@class="condition clearfix"]/@title')
        for k in All_x:
            g.append(k.extract())
        d = ("Position","Company","All")
        h = [e,f,g]
        for l in range(0,len(e)):
            for m in range(0,len(h)):
                self.item[d[m]] = h[m][l]
            yield self.item

