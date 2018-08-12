# -*- coding: utf-8 -*-
import scrapy
from ScrapyDemo.items import ScrapydemoItem


class DoupanSpiderSpider(scrapy.Spider):
    name = 'doupan_spider'
    allowed_domains = ['movie.douban.com']
    start_urls = ['https://movie.douban.com/top250']

    def parse(self, response):
        movie_list = response.xpath("//div[@class='article']//ol[@class='grid_view']/li")
        for i_item in movie_list:
            douban_item = ScrapydemoItem()
            douban_item['serial_number'] = i_item.xpath('.//div[@class="item"]//em//text()').extract_first()
            douban_item['movie_name'] = i_item.xpath(".//div[@class='info']//div[@class='hd']//a//span[1]//text()").extract()[0]
            content = i_item.xpath(".//div[@class='info']//div[@class='bd']//p[1]//text()").extract()
            for i_content in content:
                content_s = "".join(i_content.split())
                douban_item['introduce']=content_s
            douban_item['star'] = i_item.xpath(".//span[@class='rating_num']//text()").extract()[0]
            douban_item['evaluate'] = i_item.xpath(".//div[@class='star']//span[4]//text()").extract()[0]
            douban_item['describe'] = i_item.xpath(".//p[@class='quote']//span//text()").extract()[0]
            print(douban_item)
