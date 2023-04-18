import requests
from bs4 import BeautifulSoup
import time

def get_cars(url):
    response = requests.get(url)
    soup = BeautifulSoup(response.text, 'html.parser')

    cars = soup.find_all('div', class_='announcement-item')
    for car in cars:
        title = car.find('h3', class_='title')
        price = car.find('div', class_='price')
        if title and price:
            price = int(price.text.strip().replace('€', '').replace(' ', ''))
            if price <= 1000:
                print(title.text.strip(), '-', price, '€')

def main():
    url = 'https://autogidas.lt/skelbimai/automobiliai/?f_1=r_1.1_1000'
    while True:
        get_cars(url)
        print("\n--- Laukiama 30 min ---\n")
        time.sleep(1800)  # 30 minučių laukimas

if __name__ == '__main__':
    main()
