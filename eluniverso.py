from scrapy.item import Field
from scrapy.item import Item
from scrapy.spiders import Spider
from scrapy.selector import Selector
from scrapy.loader import ItemLoader
from bs4 import BeautifulSoup

#recordar siempre revisar el xpath en el navegador para poder extraer la informacion 
# y verificar si esta correcto o a cambiado algo

#Extraer el titulo y los resumenes de las noticias colgadas en la seccion de deportes del diario el universoseccion deportes


# EJECUCION EN TERMINAL:
# scrapy runspider nombre archivo.py -o nombre_de_salida.csv -t csv    