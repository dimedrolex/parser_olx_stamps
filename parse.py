from bs4 import BeautifulSoup
import requests

URL = 'https://www.olx.ua/d/hobbi-otdyh-i-sport/antikvariat-kollektsii/kollektsionirovanie/q-%D0%BC%D0%B0%D1%80%D0%BA%D0%B8-%D1%80%D1%83%D1%81%D1%81%D0%BA%D0%B8%D0%B9-%D0%BA%D0%BE%D1%80%D0%B0%D0%B1%D0%BB%D1%8C/?currency=UAH'
HEADERS = {'user-agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10.15; rv:99.0) Gecko/20100101 Firefox/99.0', 'accept': '*/*'}


def save():
    with open('parse.txt', 'a') as file:
        file.write(f'{comp["title"]} -> Price: {comp["price"]} \nImg: {comp["img"]}\n')


def parse():
    response = requests.get(URL, headers = HEADERS)
    soup = BeautifulSoup(response.content, 'html.parser')
    items = soup.findAll('div', class_ = 'css-wmzjt6')
    comps = []

    for item in items:
        comps.append({
            'title': item.find('h6', class_ = 'css-v3vynn-Text eu5v0x0').get_text(strip = True),
            'price': item.find('p', class_ = 'css-l0108r-Text eu5v0x0').get_text(strip = True),
            'img': item.find('img', class_ = 'css-8wsg1m').get('src')
            })

    global comp
    for comp in comps:
        print(f'{comp["title"]} -> Price: {comp["price"]} \nImg: {comp["img"]}\n')
        save()

parse()
