import os

import telegram

from dotenv import load_dotenv


if __name__ == '__main__':
    load_dotenv()
    telegram_token = os.environ['TELEGRAM_BOT_TOKEN']
    telegram_group_id = os.environ['TELEGRAM_GROUP_ID']
    bot = telegram.Bot(telegram_token)
    bot.send_photo(chat_id=telegram_group_id, photo=open('images/nasa_apod_4.jpg', 'rb'))
