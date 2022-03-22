import requests
from time import sleep
from bs4 import BeautifulSoup

def get_data(url):
    headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/99.0.4844.74 Safari/537.36'}
    q = requests.get(url, headers=headers)

    if q.status_code == 200:
        q.encoding = "utf-8"
        result = q.text
        soup = BeautifulSoup(result, "lxml")
        search_alert = soup.find("div", class_="alert-warning")

        if search_alert is not None:
            print('Местов нет')
            sleep(1)
            return("Товар не найден")
        else:
            print(url)
            sleep(1)
            return(url)
    elif q.status_code == 404:
        print('Block')
        sleep(1)
        return("Запрос заблокирован")

if __name__ == "__main__":
    list_url = []
    with open('list_url.txt') as f:
        list_url = f.read().splitlines()

    while True:
        for x in list_url:
            if x == '':
                print("Передана пустая строка в файле list_url.txt")
            else:
                get_data(x)
        print("Сон на 12 часов")
        sleep(43200)