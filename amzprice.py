# -*- coding: utf-8 -*-
"""
Created on Mon Feb 22 23:56:13 2021

@author: pc user
"""

import requests
from bs4 import BeautifulSoup
import smtplib
URL = 'https://www.amazon.de/-/en/ILCE-7M3-Digital-Megapixel-Display-Viewfinder/dp/B07B4R8QGM'
headers ={"User-Agent":'Mozilla/5.0 (Windows NT 10.0) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/87.0.4280.141 Safari/537.36 OPR/73.0.3856.344'}
def check_price():
  page=requests.get(URL,headers=headers)

  soup = BeautifulSoup(page.content, 'html.parser')

  title = soup.find(id="productTitle").get_text()
  price = soup.find(id="priceblock_ourprice").get_text()
  converted_price=float(price[0:5])
  if (converted_price>17.000):
    send_mail()
  if(converted_price<17.000):
      send_mail()
    
  print(converted_price)
  print(title.strip())
def send_mail():
    server =smtplib.SMTP('smtp.gmail.com',587)
    server.ehlo()
    server.starttls()
    server.ehlo()
    
    server.login('tutorialschool7@gmail.com', 'Gostrider5')
    subject="prices fell down"
    body= 'check out the link https://www.amazon.de/-/en/ILCE-7M3-Digital-Megapixel-Display-Viewfinder/dp/B07B4R8QGM'  
    msg = f"Subject : {subject}\n\n{body}"
    
    server.sendmail(
            'shahzebiftikhar4@gmail.com',
            'zaibigujjar@hotmail.com',
            msg)
    print("eMAIL HAS BEEN SENT")
    server.quit()
check_price()