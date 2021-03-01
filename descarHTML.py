from bs4 import BeautifulSoup
from requests_html import HTMLSession
import xlwings as xl
import codecs

url = 'https://www.cyberpuerta.mx/Computo-Hardware/Monitores/Monitores/2/Filtro/Forma-de-la-pantalla/Curva/'

session = HTMLSession()
container = session.get(url).html

htmlCode = BeautifulSoup(container.html, 'html.parser')

data = f'{htmlCode}'

file = codecs.open('sample.html', 'w', 'utf-8')

file.write(data)

file.close()