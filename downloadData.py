from bs4 import BeautifulSoup
from requests_html import HTMLSession
import xlwings as xl
import codecs
from pprint import pprint
from tqdm import tqdm


monitorData = []


for i in tqdm(range(1,6)):
  if i == 1:
    url = 'https://www.cyberpuerta.mx/Monitores-Curvo/'
  else:
    url = f'https://www.cyberpuerta.mx/Computo-Hardware/Monitores/Monitores/{i}/Filtro/Forma-de-la-pantalla/Curva/'

  session = HTMLSession()
  container = session.get(url).html
  htmlCode = BeautifulSoup(container.html, 'html.parser')

  eachContainer = htmlCode.find_all('div', {'class': 'emproduct_right'})

  for x in eachContainer:
    try:
      wholeData = x.find('div', {'class':'clear emproduct_left_attribute_price'})
      wholeDataPriceContainer = x.find('div', {'class': 'emproduct_right_price'})
      pricesPath = 'div.clear div.emproduct_right_price_left'
      currentPriceField = wholeDataPriceContainer.select(pricesPath)


      oldPrice = f"{wholeDataPriceContainer.find('span',{'class': 'oldPrice'}).text}".strip()
      currentPrice = f"{currentPriceField[0].select('label.price')[0].text}".strip()
      deliveryPrice = currentPriceField[0].select('div.emdeliverycost span.deliveryvalue')[0].text

      productName = f"{x.find('a').text}".strip()
      urlProduct = x.find("a").attrs['href']
      especifications = '.emproduct_right_attribute ul li'
      inches = f"{wholeData.select(especifications)[0].text}".replace("Diagonal de la pantalla: ","")
      hdType = f"{wholeData.select(especifications)[1].text}".replace("Tipo HD: ", "")
      resolution = f"{wholeData.select(especifications)[2].text}".replace("Resolución: ", "")
      refreshVelocity = f"{wholeData.select(especifications)[4].text}".replace("Velocidad de actualización: ", "")
      
      monitorData.append(tuple([productName, urlProduct, inches, hdType, resolution, refreshVelocity, oldPrice, currentPrice, deliveryPrice ]))

    except:
      pass

wb = xl.Book()
ws = wb.sheets[0]

xl.books.active
xl.sheets.active

headers = ["Desc. Producto", "URL", "Pulgadas (medida)", "Pixeles", "Resolución", "Tasa de refresco", "Precio original", "Precio descuento", "Precio entrega"]

ws.range((1,1)).value = headers
ws.range((2,1)).value = monitorData





    

print('fin del programa')