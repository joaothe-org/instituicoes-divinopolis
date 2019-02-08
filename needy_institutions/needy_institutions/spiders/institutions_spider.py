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
      for e in my_list:
        if e['name'] is not None and e['teste'] is not None :
          e['name'] = unidecode(e['name'].strip())
          e['teste'] = unidecode(e['teste'].strip())

      def myFunc(x):
        if x['name'] is None or x['teste'] is None:
          return False
        else:
          return True

      filteredList = filter(myFunc, my_list)

      def Remove(duplicate): 
        final_list = [] 
        for num in duplicate: 
          if num not in final_list: 
            final_list.append(num) 
        return final_list 
      
      print(Remove(filteredList)) 
    