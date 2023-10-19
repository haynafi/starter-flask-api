from flask import Flask, jsonify, request
import os

# crawling
import pandas as pd
from datetime import datetime
import requests
from bs4 import BeautifulSoup

app = Flask(__name__)

@app.route('/')
def hello_world():
    return 'Hello, world!'

@app.route('/boom')
def boom():
    return 'duar!'

# user define function
# Scrape the data
def getdata(url):
	r = requests.get(url)
	return r.text

@app.route('/alfa')
def alfa():
#     # url
    url = "https://alfamart.co.id/promo/hot-promo"

#     # pass the url
#     # into getdata function
    htmldata = getdata(url)
    soup = BeautifulSoup(htmldata, 'html.parser')
    
#     list_promo = soup.findAll('div', attrs={'id':'program-list'})
#     # display html code
#     # print(soup)
    return 'alfa'

# driver function 
if __name__ == '__main__': 
  
    app.run(debug = True) 