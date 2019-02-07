# -*- coding: utf-8 -*-
import scrapy
from unidecode import unidecode

class needyDivi(scrapy.Spider):
    name = 'needyDivi'
    start_urls = ['https://www.telelistas.net/mg/divinopolis/associacoes+beneficentes']

    def parse(self, response):
      lista = response.css('#Content_Regs table')
      name = scrapy.Field()
      endereco = scrapy.Field()
      print('NEEDY')
      my_list = []
      for result in lista:
        name = result.css('.text_resultado_ib a::text').extract_first()
        endereco = result.css('.text_endereco_ib ::text').extract_first()
        my_list.append({'name': name, 'teste': endereco})
        '''yield {
          'name': name,
          'price': endereco
        }'''
      for e in my_list:
        if e['name'] is not None and e['teste'] is not None :
          e['name'] = unidecode(e['name'].strip())
          e['teste'] = unidecode(e['teste'].strip())
      print(my_list)    