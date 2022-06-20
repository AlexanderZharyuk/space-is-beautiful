import logging
import os

import telegram
import requests

from dotenv import load_dotenv


def download_image(image_url: str, image_folder: str = 'images/') -> None:
    response = requests.get(image_url)

    os.makedirs(image_folder, exist_ok=True)
    image_name = 'hubble.jpeg'
    image_path = os.path.join(image_folder, image_name)

    with open(image_path, 'wb') as new_image:
        new_image.write(response.content)


if __name__ == '__main__':
    load_dotenv()
    download_image('https://upload.wikimedia.org/wikipedia/commons/3/3f/HST-SM4.jpeg', 'test/')
