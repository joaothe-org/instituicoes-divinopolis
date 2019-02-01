# -*- coding: utf-8 -*-
import scrapy


class needyDivi(scrapy.Spider):
    name = 'needyDivi'
    start_urls = ['https://www.telelistas.net/mg/divinopolis/associacoes+beneficentes']

    def parse(self, response):
      results = response.css('.text_resultado_ib a ::text').extract()
      print('NEEDY')
      for result in results:
        print (result) 