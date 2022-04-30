Поиск лекарств в аптеке Фармленд
================================
*For live CJ, for live❤️*
-- --
![PyPI - Python Version](https://img.shields.io/badge/python-%3D%3E3.10.4-green) ![Ubuntu:20.04](https://img.shields.io/badge/test-Ubuntu%3A22.04-orange)
-- --
## Установка

***Для того, чтобы программа запустилась и работала. Нужно передать ENV переменную TOKEN***

***Для корректной работы требуется личный Telegram [бот](https://core.telegram.org/bots)***

### Установка зависимотей

`pip3 install -r requirements.txt`

### Запуск

`python3 main.py`

## Docker

### Docker build

`docker build -t vikrusban/searchhealth:latest .`

### Docker run

`docker run -t -i -d --name searchHealth --restart=always -e TOKEN=5245807676:AAEGookGUKEq3BqdNGKcjfSNGumPKW5wdCc vikrusban/searchhealth:latest`