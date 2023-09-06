from scrapy.item import Field
from scrapy.item import Item
from scrapy.spiders import Spider
from scrapy.selector import Selector
from scrapy.loader import ItemLoader
from bs4 import BeautifulSoup

#recordar siempre revisar el xpath en el navegador para poder extraer la informacion 
# y verificar si esta correcto o a cambiado algo

#Extraer el titulo y los resumenes de las noticias colgadas en la seccion de deportes del diario el universoseccion deportes

class Noticia(Item):
    id = Field()
    #titular = Field()
    descripcion = Field()
    
    
class ElUniversoSpider(Spider):
    
    name = "SpiderElUniverso"
    
    custom_settings = {
        'USER_AGENT': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Ubuntu Chromium/71.0.3578.80 Chrome/71.0.3578.80 Safari/537.36'
    }   
    
    start_urls = ["https://www.eluniverso.com/deportes/"]
    
    def parse(self, response):
        
        sel: Selector = Selector(response)
        
        noticias = sel.xpath('//div[@class="content-feed | space-y-2  "]/ul//li')
        
        i=0
        for noticia in noticias:
            item = ItemLoader(Noticia(), noticia)
            #item.add_xpath('titular', './/div[@class="card | card-sm story flex flex-row space-x-2 items-center   py-2  w-full   "]//div[@class= "card-content | space-y-1 "]/h2/span/a/text()')  
            item.add_xpath('descripcion', './/div[@class="card | card-sm story flex flex-row space-x-2 items-center   py-2  w-full   "]//div[@class= "card-content | space-y-1 "]/p/text()')
            item.add_value('id', i)
            i+=1
            yield item.load_item()
            
    
# EJECUCION EN TERMINAL:
# scrapy runspider eluniverso.py -o eluniversofinal.csv -t csv   
# scrapy runspider eluniverso.py -o eluniversotitulares.csv -t csv  
# scrapy runspider eluniverso.py -o eluniversodescripcion.csv -t csv 