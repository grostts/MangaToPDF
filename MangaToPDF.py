import requests
from bs4 import BeautifulSoup
import img2pdf
import os

def get_data(manga, book, chapter):
    headers = {
        'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/93.0.'
                      '4577.63 Safari/537.36'
    }

    url = f'https://mangapoisk.ru/manga/{manga}/chapter/{book}-{chapter}'
    print(url)

# manga = input('Enter the name of the manga: ')
# book = input('Enter the number of the book: ')
# chapter = input('Enter the number of the chapter: ')

manga = "berserk"
book = 42
chapter = 368

get_data(manga, book, chapter)