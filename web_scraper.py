# -*- coding: utf-8 -*-
"""
Created on Sun Jul 06 10:09:25 2014

@author: Paul
"""

import scrapy

class waterrights(scrapy.Item):
    title = scrapy.Field()
    link = scrapy.Field()
    desc = scrapy.Field()
    
class DmozSpider(scrapy.Spider):
    name = "wr"
    allowed_domains = ["http://www.waterrights.utah.gov/"]
    start_urls = [
        "http://waterrights.utah.gov/",
        "http://waterrights.utah.gov/docSys/v907/"
    ]
    def parse(self, response):
        filename = response.url.split("/")[-2]
        with open(filename, 'wb') as f:
            f.write(response.body)
    
    '''
    http://waterrights.utah.gov/docSys/v907/d907/d90704sy.htm
    http://waterrights.utah.gov/docSys/v907/e907/e907027q.htm
    http://waterrights.utah.gov/docSys/v907/d907/d90704z5.htm
    http://waterrights.utah.gov/cgi-bin/docview.exe?Folder=welllog3439
    http://waterrights.utah.gov/cblapps/wrprint.exe?wrnum=31-661
     <B>LITHOLOGY:</B>
   Depth(ft)  Lithologic Description                                                          Color        Rock Type
   From    To

    '''