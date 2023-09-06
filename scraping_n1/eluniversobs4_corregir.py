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
    
    titular = Field()
    descripcion = Field()
    
    
class ElUniversoSpider(Spider):
    
    name = "SpiderElUniverso"
    
    custom_settings = {
        'USER_AGENT': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Ubuntu Chromium/71.0.3578.80 Chrome/71.0.3578.80 Safari/537.36'
    }   
    
    start_urls = ["https://www.eluniverso.com/deportes/"]
    
    def parse(self, response):
        soup = BeautifulSoup(response.body)
        
        contenedor_noticias = soup.find_all('li', class_='relative ',recursive= True) #aca esta el error
        for noticia in contenedor_noticias:
            item = ItemLoader(Noticia(), response.body)
            titular = noticia.find('span', class_= 'relative').text
            descripcion = noticia.find('p', class_='summary | text-sm m-0 font-secondary').text
            item.add_value('titular', titular )
            item.add_value('descripcion', descripcion )
            
            yield item.load_item()
            
            
# EJECUCION EN TERMINAL:
# scrapy runspider eluniversobs4.py -o eluniversofinalbs4.csv -t csv   
            
    
# EJECUCION EN TERMINAL:
# scrapy runspider eluniverso.py -o eluniversofinal.csv -t csv   
# scrapy runspider eluniverso.py -o eluniversotitulares.csv -t csv  
# scrapy runspider eluniverso.py -o eluniversodescripcion.csv -t csv 
# scrapy runspider eluniverso.py -o eluniversofinal.json -t json