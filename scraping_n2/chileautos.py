from scrapy.item import Field
from scrapy.item import Item
from scrapy.spiders import CrawlSpider, Rule
from scrapy.selector import Selector
from scrapy.loader.processors import MapCompose
from scrapy.linkextractors import LinkExtractor
from scrapy.loader import ItemLoader



#scraping Vertical

class FordF150(Item):
    precio = Field()
    modeloMarca = Field()
    especificaciones = Field()
    comentarios = Field()
    
class ChileAutos(CrawlSpider):
    name = "SpiderChileAutos"
    
    custom_settings = {
        'USER_AGENT': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Ubuntu Chromium/71.0.3578.80 Chrome/71.0.3578.80 Safari/537.36'
    }   
    start_urls = ["https://www.chileautos.cl/vehiculos/autos-veh%C3%ADculo/ford/f-150/"]
    
    download_delay = 2
    
    rules = (
        Rule(
            LinkExtractor(
                allow=r'/detalles/'
            ), follow=True, callback="parse_fordf150"
        ),
    )
    def quitarSimboloPeso(self, texto):
        nuevoTexto = texto.replace("$", "")
        return nuevoTexto
    
    def parse_fordf150(self, response):
        sel = Selector(response)
        item = ItemLoader(FordF150(), sel)
        item.add_xpath('precio', '//section[@class="price-display-wrapper"]//div[@class="price"]/text()', MapCompose(self.quitarSimboloPeso))
        item.add_xpath('modeloMarca','//section/div[@class="details-wrapper"]//div//div[@class="col-lg-8 col-sm-10"]/h1/text()')
        item.add_xpath('especificaciones', '//div[@class="key-details-wrapper"]//div[@class="key-details-item-title"]/text()')
        item.add_xpath('comentarios', '//section[@class= "comments"]//div[@class="view-more-target"]/p/text()')
        yield item.load_item()
        
        
# EJECUCION EN TERMINAL:
# scrapy runspider chileautos.py -o chileautosfinal.csv -t csv   
# scrapy runspider chileautos.py -o chileautostitulares.csv -t csv  
# scrapy runspider chileautos.py -o chileautosdescripcion.csv -t csv 
# scrapy runspider chileautos.py -o chileautosfinal.json -t json
        
        
       
        
        
        