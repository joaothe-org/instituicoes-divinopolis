# -*- coding: utf-8 -*-
import scrapy


class needyDivi(scrapy.Spider):
    name = 'needyDivi'
    start_urls = ['https://www.telelistas.net/mg/divinopolis/associacoes+beneficentes']

    def parse(self, response):
      #results = response.css('.text_resultado_ib a ::text').extract()
      #enderecos = response.css('.text_endereco_ib ::text').extract()
      teste = response.css('#Content_Regs table')
      name = scrapy.Field()
      address = scrapy.Field()
      print('NEEDY')
      for result in teste:
        name = result.css('.text_resultado_ib a ::text').get(),
        address = result.css('.text_endereco_ib ::text').get()
        yield {
          'name': name,
          'address': address
        }
      ''' for result in results:
        print(result)
      for endereco in enderecos:
        print(endereco) '''  
