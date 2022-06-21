import os
import random
import time
import logging

import telegram

from dotenv import load_dotenv


if __name__ == '__main__':
    load_dotenv()
    telegram_token = os.environ['TELEGRAM_BOT_TOKEN']
    telegram_group_id = os.environ['TELEGRAM_GROUP_ID']
    if os.environ.get('POST_DELAY'):
        posting_delay = float(os.environ['POST_DELAY'])
    else:
        posting_delay = 14400

    bot = telegram.Bot(telegram_token)
    images = os.walk('images').__next__()[2]
    max_file_size = 20000000

    logging.basicConfig(format='[%(levelname)s]: %(message)s', datefmt='%m.%d.%Y %H:%M:%S', level=logging.INFO)

    while True:
        try:
            random_image = random.choice(images)
            image_path = f'images/{random_image}'
            file_size = os.path.getsize(image_path)
            if file_size >= max_file_size:
                continue

            bot.send_photo(chat_id=telegram_group_id, photo=open(image_path, 'rb'))
            time.sleep(posting_delay)
        except ConnectionError:
            logging.error('ConnectionError. Going to sleep 1 min.')
            time.sleep(60)
