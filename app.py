from flask import Flask, jsonify, request
import os

# crawling
import pandas as pd
from datetime import datetime
import requests
from bs4 import BeautifulSoup

#for output json
import json
import jsonpickle


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

    #extract element
    list_promo = soup.findAll('div', attrs={'id':'program-list'})
    # print(list_promo)


    arr_json = []

    for datanya in list_promo:
        getClass = datanya.findAll('div', attrs={'class':'col-6 col-md-6 col-lg-3 filter-element'})
        for x in getClass:
            date_now = datetime.today().strftime('%Y-%m-%d-%H:%M:%S')
            url_promo_detail = x.find('a', attrs={'class':'card card-promo-item animated vp-fadeinup delayp1'}).get('href')
            nama_promo = x.find('h5', attrs={'class':'text-truncate-multiline'}).get_text()
            expiry_date = x.find('span').get_text()
            det_img = x.find('div', attrs={'class':'img-wrapper'})
            get_det_img = det_img.find('img', alt=True)
            # img_url = x.find('div', attrs={'class':'img-wrapper'})
            # img_title = x.find('div', attrs={'class':'img-wrapper'})
            link_gambar = get_det_img['src']
            arr_json.append('{ "name":'+nama_promo+', "exp_date":'+expiry_date+', "detail_promo":'+url_promo_detail+', "url_img":'+link_gambar+', "inserted_at":'+date_now+'}')

    s1 = json.dumps(arr_json)
    d2 = json.loads(s1)
    # print(d2)
    return jsonpickle.encode(d2)

# driver function 
if __name__ == '__main__': 
  
    app.run(debug = True) 