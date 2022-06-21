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
    logging.basicConfig(format='[%(levelname)s]: %(message)s', datefmt='%m.%d.%Y %H:%M:%S', level=logging.INFO)

    while True:
        try:
            random_image = random.choice(images)
            image_path = os.path.join(os.environ['DOWNLOAD_DIR'], random_image)

            bot.send_photo(chat_id=telegram_group_id, photo=open(image_path, 'rb'))
        except ConnectionError:
            logging.error('ConnectionError. Going to sleep 1 min.')
            time.sleep(60)
            continue
        except telegram.error.BadRequest:
            logging.info('Image size is big, try new one...')
            continue

        time.sleep(posting_delay)
