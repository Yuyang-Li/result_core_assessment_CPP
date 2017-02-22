#!/usr/bin/env python
# encoding=utf-8

from bs4 import BeautifulSoup
import requests
import csv


import sys
reload(sys)
sys.setdefaultencoding('utf8')

DOWNLOAD_URL = 'https://book.douban.com/tag/经济学'

def DownloadPage(url):
    return requests.get(url, headers={
        'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_11_2) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/47.0.2526.80 Safari/537.36'
    }).content


def parse_html(html):
    soup = BeautifulSoup(html,'html.parser')
    body = soup.body
    fetch = body.find('div',attrs={'id':'wrapper'})
    fetch_more = fetch.find('div',attrs={'id':'subject_list'})
    book_list_soup = fetch_more.find('ul', attrs={'class': 'subject-list'})

    books_list = []
    global book_list

    for book_li in book_list_soup.find_all('li'):
        book_list = []
        info = book_li.find('div',attrs={'class': 'info'})

        detail = info.find('h2',attrs={'class':''})
        book_id = detail.a['href']
        book_name = detail.a['title']

        book_pub = info.find('div',attrs={'class':'pub'}).getText()

        rating_nums = info.find('div',attrs={'class':'star clearfix'})
        book_rating_nums = rating_nums.find('span',attrs={'class':'rating_nums'})
        if book_rating_nums is not None:
            book_rating = book_rating_nums.getText()
        else:
            book_rating = 'None'
        book_pl = rating_nums.find('span',attrs={'class':'pl'}).getText()

        find_price = info.find('div',attrs={'class':'ft'})
        fetch_price = find_price.find('div',attrs={'class':'cart-actions'})
        get_price = fetch_price.find('span',attrs = {'class':'buy-info'})
        if get_price is not None:
            book_price = get_price.getText()
        else: book_price = 'None'

        book_list.append(book_id)
        book_list.append(book_name)
        book_list.append(book_pub)
        book_list.append(book_rating)
        book_list.append(book_pl)
        book_list.append(book_price)

        books_list.append(book_list)

    page = fetch_more.find('div',attrs={'class':'paginator'})
    page_again = page.find('span',attrs={'class': 'next'})
    next_page = page_again.find('a')

    if next_page:
        return books_list,  'https://book.douban.com' + next_page['href']
    return books_list, None


def main():
    url = DOWNLOAD_URL

    with open('books_2.csv', 'wb') as f:
        writer = csv.writer(f)
        title = ['book_id', 'book_name','book_pub','book_rating','book_pl','book_price']
        writer.writerow(title)
        while url:
            html = DownloadPage(url)
            books, url = parse_html(html)
            for book in books:
                writer.writerow(book)

if __name__ == '__main__':
    main()