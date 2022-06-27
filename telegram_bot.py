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
    dir_with_images = os.environ['DOWNLOAD_DIR']
    posting_delay = int(os.getenv('POST_DELAY', 14400))

    bot = telegram.Bot(telegram_token)
    images = os.listdir(dir_with_images)
    logging.basicConfig(format='[%(levelname)s]: %(message)s', datefmt='%m.%d.%Y %H:%M:%S', level=logging.INFO)

    while True:
        try:
            random_image = random.choice(images)
            image_path = os.path.join(os.environ['DOWNLOAD_DIR'], random_image)

            with open(image_path, 'rb') as image:
                bot.send_photo(chat_id=telegram_group_id, photo=image)

        except ConnectionError:
            logging.error('ConnectionError. Going to sleep 1 min.')
            time.sleep(60)
            continue
        except telegram.error.BadRequest:
            logging.info('Image size is big, try new one...')
            continue
        except telegram.error.NetworkError:
            logging.info('Network error... Reloading')
            continue

        time.sleep(posting_delay)
