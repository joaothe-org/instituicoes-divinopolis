# -*- coding: utf-8 -*-
import scrapy
from unidecode import unidecode

class needyDivi(scrapy.Spider):
    name = 'needyDivi'
    start_urls = ['https://www.telelistas.net/mg/divinopolis/associacoes+beneficentes']

    def parse(self, response):
      _list = response.css('#Content_Regs table')
      name = scrapy.Field()
      address = scrapy.Field()
      print('NEEDY')
      my_list = []
      for result in _list:
        name = result.css('.text_resultado_ib a::text').extract_first()
        address = result.css('.text_endereco_ib ::text').extract_first()
        my_list.append({'name': name, 'address': address})
      for item in my_list:
        if item['name'] is not None and item['address'] is not None :
          item['name'] = unidecode(item['name'].strip())
          item['address'] = unidecode(item['address'].strip())

    
      filteredList = filter(self.myFunc, my_list)
      print(self.Remove(filteredList)) 

    def myFunc(self, x):
      if x['name'] is None or x['address'] is None:
        return False
      else:
        return True
    
    def Remove(self, duplicate): 
      final_list = [] 
      for num in duplicate: 
        if num not in final_list: 
          final_list.append(num) 
      return final_list 
    