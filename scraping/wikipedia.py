import requests
from lxml import html

#OBJETIVOS: 
    #- Extraer los idiomas de la pagina principal de WIKIPEDIA
    #- Aprender a utilizar requests para hacer requerimientos
    #- Aprender a utilizar lxml para parsear el arbol HTML

#revision de paginas en dos fases primero se realiza el request y luego se parsea(se analiza el codigo html para extraer los datos que se necesitan)

#CONCEPTO "user-agent" 
#es una cadena de tecto con la cual se puede identificar el navegador y el sistema operativo del cliente. por defecto es:ROBOT 
# e identifica la maquina de inmediato que se esta haciendo escrapeo por lo que hay que modificarla antes de hacer la consulta o request


 #- Aprender a utilizar requests para hacer requerimientos
encabezados = {
    "user-agent": "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Ubuntu Chromium/71.0.3578.80 Chrome/71.0.3578.80 Safari/537.36",
}
# Empezamos definiedo la URL semilla de la página que queremos escrapear
url= "https://www.wikipedia.org/"

#aca estamos capturando la consulta a la pagina
respuesta = requests.get(url, headers=encabezados)

#print(respuesta.text) 

 #- Aprender a utilizar lxml para parsear el arbol HTML
 
parser = html.fromstring(respuesta.text)

ingles =parser.get_element_by_id("js-link-box-en")
 
#print(ingles.text_content())

ex_ingles = parser.xpath("//a[@id='js-link-box-en']/strong/text()") #xpath es una forma de buscar en el arbol html

#print(ex_ingles)

extraer_idiomas = parser.xpath("//div[contains(@class, 'central-featured-lang')]//strong/text()") #contains es una funcion de xpath que permite buscar por una cadena de texto

#print(extraer_idiomas)

for idioma in extraer_idiomas:
    print(idioma)

extraer_idiomas_otra_forma = parser.find_class("central-featured-lang") #find_class es una funcion de lxml que permite buscar por una clase

for idiomas in extraer_idiomas_otra_forma:
    print(idiomas.text_content())
    
