import requests
from time import sleep
from bs4 import BeautifulSoup
from config import chat, token

def get_data(url):
    headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/99.0.4844.74 Safari/537.36'}
    q = requests.get(url, headers=headers)

    if q.status_code == 200:
        q.encoding = "utf-8"
        result = q.text
        soup = BeautifulSoup(result, "lxml")
        search_alert = soup.find("div", class_="alert-warning")

        if search_alert is not None:
            #print('Товар не найден')
            sleep(1)
            return(None)
        else:
            #print(url)
            sleep(1)
            return(url)
    elif q.status_code == 404:
        print('Block')
        sleep(1)
        return("Запрос заблокирован")

def send_telegram(text: str):
    url = "https://api.telegram.org/bot"
    url += token
    method = url + "/sendMessage"

    r = requests.post(method, data={
         "chat_id": chat,
         "text": text
          })

    if r.status_code != 200:
        raise Exception("post_text error")

if __name__ == "__main__":
    list_url = []
    with open('list_url.txt') as f:
        list_url = f.read().splitlines()
    f.close()

    while True:
        for x in list_url:
            if x == '':
                print("Передана пустая строка в файле list_url.txt")
            else:
                ret = get_data(x)
                if ret is not None:
                    data_find = """
💊 Кажется я что-то нашел, перейди по ссылке для проверки 💊
"""+ret+"""
Следущая проверка через 12 часов 🕓
                    """
                    send_telegram(data_find)
                    print(ret)
                else:
                    print(ret)
        print("Сон на 12 часов")
        sleep(28800)