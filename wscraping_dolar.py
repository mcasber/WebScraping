import requests #para hacer una peticion a la pagina
from bs4 import BeautifulSoup as bs #para extraer el html y analizarlo
import datetime
import pandas as pd
import numpy as np
#selenium es una libreria para hacer webscraping
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
#para que la page web no detecte que soy un ordenador
import undetected_chromedriver as uc

browser = uc.Chrome() #creo el objeto pa navegar
url='https://dolarhoy.com/' #le paso una web 
browser.get(url) #y le digo que vaya a esa web
browser.implicitly_wait(10)

#browser.find_element('xpath','//*[@id="didomi-notice-agree-button"]').click()# para hacer click en el boton Aceptar 

html=browser.page_source #con este metodo guardo en una variable el codigo html de la pagina
#print(html) #no es un formato muy prolijo para leer

#uso beautifulsoup para darle un formato mas espaciado y procesado para trabajar bien con el 
soup=bs(html,'html') #'lxml') -------> lo utiliza Javi y le da resultado...
#print(f'esto es la data que bajo: \n {soup} \n y aca finaliza.')

#Al terminar el proceso cierro la pestaña
browser.close()
#Cierro el navegador
browser.quit()

#Comienzo a trabajar con la data --> el proceso es siempre el mismo
compra=soup.find('div', {'class':'val'}).text
        #en soup voy a buscar un span -> que es de tipo clase #con .text lo paso a texto
print(compra,'\n',type(compra))
precio_compra=int(compra[1:])
print(f'el precio de compra de u$ actual es:$ {precio_compra} \n y hoy es: {(datetime.datetime.today().strftime("%H:%M:%S--%A %d/%m/%y"))}')
