from bs4 import BeautifulSoup
from fake_useragent import UserAgent
import aiohttp
import asyncio

async def collect_data(city):
    ua = UserAgent(browsers=['edge', 'chrome'])
    headers = {
        'Accept': 'application/font-woff2;q=1.0,application/font-woff;q=0.9,*/*;q=0.8',
        'User-Agent': ua.random
    }

    async with aiohttp.ClientSession() as session:
        response = await session.get(url='https://farmlend.ru/'+city+'/search?keyword=эуритокс', headers=headers)
        response.encoding = 'utf-8'
        soup = BeautifulSoup(await response.text(), 'lxml')
        search_alert = soup.find("div", class_="pi-title")
        if search_alert is not None:
            print('Товар не найден')
        else:
            return(response.url)

def main():
    #city = ['beloreck', 'magnitogorsk', 'chelyabinsk']
    result_collect_data = asyncio.run(collect_data('beloreck'))
    print(result_collect_data)

if __name__ == '__main__':
    main()