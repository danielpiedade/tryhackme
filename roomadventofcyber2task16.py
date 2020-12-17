#!/usr/bin/env python3

from bs4 import BeautifulSoup
import requests 

html = requests.get(f'http://10.10.7.18:8000')
soup = BeautifulSoup(html.text, "lxml")
links = soup.find_all('a') 

for link in links: 
  if "href" in link.attrs:
      print(link["href"])
    
for api_key in range(1,100,2):
    print(api_key)
    html = requests.get(f'http://10.10.7.18:8000/api/{api_key}') 
    print(html.text)
