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


    # Creation of data folder if necessary
    if os.path.exists('data'):
        pass
    else:
        os.mkdir('data')


    # Creation of manga name folder if necessary
    manga_folder_name = f"data/{manga}"
    if os.path.exists(manga_folder_name):
        pass
    else:
        os.mkdir(manga_folder_name)
    manga_folder_name_book = f"data/{manga}/book_{book}"


    # Creation of manga book folder if necessary
    if os.path.exists(manga_folder_name_book):
        pass
    else:
        os.mkdir(manga_folder_name_book)
    manga_folder_name_book_chapter = f"data/{manga}/book_{book}/chapter_{chapter}"


    # Creation of manga chapter folder if necessary
    if os.path.exists(manga_folder_name_book_chapter):
        pass
    else:
        os.mkdir(manga_folder_name_book_chapter)

    req = requests.get(headers=headers, url=url)

    with open(f'{manga_folder_name_book_chapter}.html', 'w', encoding='utf-8') as file:
        file.write(req.text)

    with open(f'{manga_folder_name_book_chapter}.html', 'r', encoding='utf-8') as file:
        scrap = file.read()

    soup = BeautifulSoup(scrap, 'lxml')

    page_image_urls_list = []


    # get cover url
    page_image_url_cover = soup.find(class_='img-fluid page-image').get('src')
    page_image_urls_list.append(page_image_url_cover)


    # get pages urls
    page_image_urls = soup.find_all(class_='img-fluid page-image lazy lazy-preload')


    # get page urls
    for i in range(0, len(page_image_urls)-1):
        page_image_urls_list.append(page_image_urls[i+1].get('data-src'))

    img_list = []
    for i in range(0, len(page_image_urls_list)):
        r = requests.get(headers=headers, url=page_image_urls_list[i])
        response = r.content
        with open(f'data/{manga}/book_{book}/chapter_{chapter}/Page{i+1}.jpg', 'wb') as f:
            f.write(response)
            img_list.append(f'data/{manga}/book_{book}/chapter_{chapter}/Page{i+1}.jpg')
            print(f'Downloaded {i+1} of {len(page_image_urls_list)}')


    # create PDF file
    with open(f"data/{manga}/book_{book}/chapter_{chapter}.pdf", "wb") as fl:
        fl.write(img2pdf.convert(img_list))

    print(f"PDF file with chapter {chapter} was created successfully!")


manga = input('Enter the name of the manga: ')
book = input('Enter the number of the book: ')
chapter = input('Enter the number of the chapter: ')


get_data(manga, book, chapter)