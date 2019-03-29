# -*- coding: utf-8 -*-
import scrapy
from unidecode import unidecode

import json

class needyDivi(scrapy.Spider):
    name = 'needyDivi'
    start_urls = ['https://www.telelistas.net/mg/divinopolis/associacoes+beneficentes']
    my_list = []
    def parse(self, response):
      _list = response.css('#Content_Regs table')
      name = scrapy.Field()
      address = scrapy.Field()
      print('NEEDY')
      for result in _list:
        name = result.css('.text_resultado_ib a::text').extract_first()
        address = result.css('.text_endereco_ib ::text').extract_first()
        if name is not None and address is not None :
          name = unidecode(name.strip())
          address = unidecode(address.strip())
        self.my_list.append({'name': name, 'address': address})
    
      self.my_list = filter(self.myFunc, self.my_list)
      print(self.Remove(self.my_list))

      next_url = self.next_page(response)
      if next_url:
        yield scrapy.Request(url=next_url, callback=self.parse)

      with open('data.json', 'w') as outfile:
        json.dump(self.Remove(self.my_list), outfile)     

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

    def next_page(self, response):
      href = response.css(".text_medio a.resultado_roda::attr('href')").extract_first()
      url = response.urljoin(href)
      return url if href else None    