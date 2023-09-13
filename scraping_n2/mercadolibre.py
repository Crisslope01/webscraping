from scrapy.item import Field
from scrapy.item import Item
from scrapy.spiders import CrawlSpider, Rule
from scrapy.selector import Selector
from scrapy.loader.processors import MapCompose
from scrapy.linkextractors import LinkExtractor
from scrapy.loader import ItemLoader
from bs4 import BeautifulSoup

class Articulo(Item):
    titulo = Field()
    descripcion = Field()
    precio = Field()
 

class MercadoLibreCrawler(CrawlSpider):
    name = "mercadoLibre"
    custom_settings = {
        'USER_AGENT': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Ubuntu Chromium/71.0.3578.80 Chrome/71.0.3578.80 Safari/537.36',
        'CLOSESPIDER_PAGECOUNT': 5
    }
    
    download_delay = 1
    
    allowed_domains = ["https://listado.mercadolibre.cl/", "https://www.mercadolibre.cl/"]
    
    start_urls = ["https://listado.mercadolibre.cl/animales-mascotas/gatos/juguetes/juguetes-para-gatos_NoIndex_True#applied_filter_id%3Dcategory%26applied_filter_name%3DCategor%C3%ADas%26applied_filter_order%3D4%26applied_value_id%3DMLC174134%26applied_value_name%3DJuguetes%26applied_value_order%3D7%26applied_value_results%3D20502%26is_custom%3Dfalse"]
    
    #corregir aca por si las moscas
    rules = (
        Rule(
            LinkExtractor(
                allow=r'/juguetes-para-gatos_'   
            ), follow=True
        ),
        Rule(
            LinkExtractor(
                allow=r'/MLC-'
            ), follow=True, callback="parse_items"
        ),
    )
    
    def parse_items(self, response):
     
        item = ItemLoader(Articulo(), response)
        item.add_xpath('titulo', '//h1/text()')
        item.add_xpath('descripcion', '//div//p["ui-pdp-description__content xpather-highlight"]/text()')
        item.add_xpath('precio', '')
       
        yield item.load_item()
    
    
    # EJECUCION EN TERMINAL:
# scrapy runspider mercadolibre.py -o mercadolibre.csv -t csv   
# scrapy runspider mercadolibre.py -o mercadolibretitulares.csv -t csv  
# scrapy runspider mercadolibre.py -o mercadolibredescripcion.csv -t csv 
# scrapy runspider mercadolibre.py -o mercadolibrefinal.json -t json