import os
from dotenv import load_dotenv, find_dotenv

import datetime

if not find_dotenv():
    exit('Environment variables not loaded because .env file is missing')
else:
    load_dotenv()

BOT_TOKEN = os.getenv('BOT_TOKEN')
MONGO_DB_USERNAME = os.getenv('MONGO_DB_USERNAME')
MONGO_DB_PASSWORD = os.getenv('MONGO_DB_PASSWORD')

time_offset = datetime.timezone(datetime.timedelta(hours=3))

DEFAULT_COMMANDS = (
    ('start', "Запуск"),
    ('help', "Помощь"),
    ('lowprice', "Узнать топ самых дешёвых отелей в городе"),
    ('highprice', "Узнать топ самых дорогих отелей в городе"),
    ('bestdeal', "Узнать топ отелей, наиболее подходящих по цене и расположению от центра"),
    ('history', 'История'),
    ('favorites', 'Избранное')
)
