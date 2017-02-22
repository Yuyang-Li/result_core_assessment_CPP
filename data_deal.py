# -*- coding: utf-8 -*-
"""
Created on Thu Feb 09 16:53:24 2017

@author: Lily
"""

# -*- coding: utf-8 -*-

import csv
import re
import pandas as pd

f = file('books_2.csv','rb')
reader = csv.reader(f)
id = []
name = []
score = []
pl = []
price = []
web_price = []
    
for line in reader:

    if line[0] == 'book_id':
        pass
    else:
        detail_id = line[0]
        mode = re.compile(r'\d+')
        if mode is not None:
            datas_id = mode.findall(detail_id)
            for data_id in datas_id:
                id.append(data_id)

    if line[1] == 'book_name':
        pass
    else:
        name.append(line[1])

    if line[3] == 'book_rating':
        pass
    elif line[3] == 'None':
        score.append(None)
    else:
        score_num = float(line[3])
        score.append(score_num)

    detail_pl = line[4]
    mode_pl = re.compile(r'\d+')
    if mode_pl is not None:
        datas_pl = mode_pl.findall(detail_pl)
        for data_pl in datas_pl:
            data_pl_num = int(data_pl)
            pl.append(data_pl_num)
    else: 
        pl.append(None)
    
    
    detail_wp = line[5]
    if detail_wp == 'None':
        web_price.append(None)
    else:
        mode_wp = re.compile(r'\d+.\d*')
        datas_wp = mode_wp.findall(detail_wp)
        for data_wp in datas_wp:
            data_wp_num = float(data_wp)
            web_price.append(data_wp_num)
    
    if line[2] == 'book_pub':
        pass
    else:
        detail_price = line[2]
        rate = 6.875
        if 'USD' in detail_price:
            m = '1'
        elif '$' in detail_price:
            m = '1'
        else:
            m = '0'
        mode_price = re.compile(r'\d+\.\d*')
        datas_price = mode_price.findall(detail_price)
    
        if datas_price == []:
            price.append(None)
        else:
            data_price_num = float(datas_price[-1])
            if m == '1':
                data_price_num = data_price_num * rate
                price.append(None)
            else:
                price.append(data_price_num)
        
s_name = pd.Series(name)
s_price = pd.Series(price)
s_wp = pd.Series(web_price)
s_score = pd.Series(score)
s_pl = pd.Series(pl)
s_id = pd.Series(id)


df = pd.DataFrame({'ID':s_id,
                   'NAME':s_name,
                   'PRICE':s_price,
                   'WEB_PRICE':s_wp,
                   'SCORE':s_score,
                   'PL':s_pl})

df.to_csv('book_data_2.csv')

   