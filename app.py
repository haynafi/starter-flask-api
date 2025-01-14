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
	headers = {
    'authority': 'www.google.com',
    'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7',
    'accept-language': 'en-US,en;q=0.9',
    'cache-control': 'max-age=0',
    'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/115.0.0.0 Safari/537.36',
    # Add more headers as needed
	}
	response = requests.get(url, headers=headers)
	if response.status_code == 200:
			return response.text
	else:
			return (f'Request failed with status code: {response.status_code}')

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
    
@app.route('/mcd')
def mcd():
#     # url
    url = "https://www.mcdonalds.co.id/promo"

#     # pass the url
#     # into getdata function
    htmldata = getdata(url)
    soup = BeautifulSoup(htmldata, 'html.parser')

    #extract element
    list_promo = soup.findAll('div', attrs={'class':'card-general-list animated fadeInUp delayp2'})
    # print(list_promo)


    arr_json = []

    for datanya in list_promo:
        det_img = datanya.findAll('div', attrs={'class':'col-md-6 col-lg-4 filter-element'})
        for x in det_img:
            date_now = datetime.today().strftime('%Y-%m-%d-%H:%M:%S')
            det_img2 = x.findAll('div', attrs={'class':'img-container'})
            card_body = x.find('div', attrs={'class':'card-body'})
            nama_promo = x.find('h5').get_text()
            exp_date = x.find('p', attrs={'class':'exp-date'}).get_text()
            url_promo_detail = x.find('a', attrs={'class':'card card-general'}).get('href')
            # print(judul)
            # print(exp_date)
            for y in det_img2:
                get_det_img = x.find('img', attrs={'class':'img-fluid'})
                gmbr = get_det_img['src']
                # print(get_det_img['src'])

            arr_json.append('{ "name":'+nama_promo+', "exp_date":'+exp_date+', "detail_promo":'+url_promo_detail+', "url_img":'+gmbr+', "inserted_at":'+date_now+'}')

    s1 = json.dumps(arr_json)
    d2 = json.loads(s1)
    # print(d2)
    return jsonpickle.encode(d2)

def db_insert(insert_val):
    import psycopg2

    #establishing the connection
    conn = psycopg2.connect(
    database="postgres", user='postgres', password='QkH8YLdkuXOwxSFA', host='db.fztsfukhwcsjecygkwjg.supabase.co', port= '5432'
    )

    #Setting auto commit false
    conn.autocommit = True
    
    #Creating a cursor object using the cursor() method
    cursor = conn.cursor()

    # list of rows to be inserted
    # values = insert_val
    
    # executing the sql statement
    cursor.executemany("INSERT INTO public.alfa VALUES(%s,%s,%s,%s)", insert_val)
    
    # # select statement to display output
    # sql1 = '''select * from classroom;'''
    
    # # executing sql statement
    # cursor.execute(sql1)
    
    # fetching rows
    for i in cursor.fetchall():
        print(i)
    
    # committing changes
    conn.commit()
    
    # closing connection
    conn.close()
    return 'insert'

@app.route('/insert_alfa')
def insert_alfa():
    import psycopg2

    #establishing the connection
    conn = psycopg2.connect(
    database="postgres", user='postgres', password='QkH8YLdkuXOwxSFA', host='db.fztsfukhwcsjecygkwjg.supabase.co', port= '5432'
    )

    #Setting auto commit false
    conn.autocommit = True
    
    #Creating a cursor object using the cursor() method
    cursor = conn.cursor()

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
            # arr_json.append('("'+nama_promo+'", "'+expiry_date+'", "'+url_promo_detail+'", "'+link_gambar+'")')
            # Preparing SQL queries to INSERT a record into the database.
            # cursor.execute('''INSERT INTO public.alfa ("name", exp_date, detail_promo, url_img) VALUES ("'''+nama_promo+'''", "'''+expiry_date+'''", "'''+url_promo_detail+'''", "'''+link_gambar+'''");''')
            cursor.execute("INSERT INTO public.alfa (name, exp_date, detail_promo, url_img) VALUES ('"+nama_promo+"', '"+expiry_date+"', '"+url_promo_detail+"', '"+link_gambar+"')")
    
    # cursor.executemany("INSERT INTO public.alfa (name, exp_date, detail_promo, url_img) VALUES(%s,%s,%s,%s)", arr_json)
    
    conn.commit()

    # Closing the connection
    conn.close()
    return 'ok'
    

# driver function 
if __name__ == '__main__': 
  
    app.run(debug = True) 