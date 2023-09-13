from scrapy.item import Field
from scrapy.item import Item
from scrapy.spiders import CrawlSpider, Rule
from scrapy.selector import Selector
from scrapy.loader.processors import MapCompose
from scrapy.linkextractors import LinkExtractor
from scrapy.loader import ItemLoader


class FordF150(Item):
    precio = Field()
    modeloMarca = Field()
    especificaciones = Field()
    comentarios = Field()
    
class ChileAutos(CrawlSpider):
    name = "SpiderChileAutos_02"

    custom_settings = {
            'USER_AGENT': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Ubuntu Chromium/71.0.3578.80 Chrome/71.0.3578.80 Safari/537.36',
            'CLOSESPIDER_PAGECOUNT': 10
        }
    
    #allowed_domains = ["", ""]
    start_urls = ["https://www.chileautos.cl/vehiculos/autos-veh%C3%ADculo/ford/f-150/?offset=0"]
    
    download_delay = 1
    
    rules = (
            Rule(
                LinkExtractor(
                    allow=r'/?offset=\d+'   
                ), follow=True),
            Rule(
                LinkExtractor(
                    allow=r'/detalles/'
                ), follow=True, callback="parse_fordf150"
            ),
        )

    def quitarSimboloPeso(self, texto):
        nuevoTexto = texto.replace("$", "").replace(",", "")
        return nuevoTexto
        
    def limpiarTexto(self, texto):
        nuevoTexto = texto.replace("\n", "").replace("\r", "").replace("\t", "").replace(" ", "").strip()
        return nuevoTexto
        
        
    def parse_fordf150(self, response):        
            item = ItemLoader(FordF150(), response)
            item.add_xpath('precio', '//section[@class="price-display-wrapper"]//div[@class="price"]/text()', MapCompose(self.quitarSimboloPeso), MapCompose(self.limpiarTexto))
            item.add_xpath('modeloMarca','//section/div[@class="details-wrapper"]//div//div[@class="col-lg-8 col-sm-10"]/h1/text()')
            item.add_xpath('especificaciones', '//div[@class="key-details-wrapper"]//div[@class="key-details-item-title"]/text()', MapCompose(self.limpiarTexto))
            item.add_xpath('comentarios', '//section[@class= "comments"]//div[@class="view-more-target"]/p/text()', MapCompose(self.limpiarTexto))
            yield item.load_item()



# EJECUCION EN TERMINAL:
# scrapy runspider chileautos_02.py -o chileautosfinal_02.csv -t csv   
# scrapy runspider chileautos.py -o chileautostitulares.csv -t csv  
# scrapy runspider chileautos.py -o chileautosdescripcion.csv -t csv 
# scrapy runspider chileautos.py -o chileautosfinal.json -t json
























