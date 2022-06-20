import logging
import os
import pprint

import telegram
import requests

from dotenv import load_dotenv


def download_image(image_url: str, image_name: str, image_folder: str = 'images/') -> None:
    response = requests.get(image_url)

    os.makedirs(image_folder, exist_ok=True)
    image_path = os.path.join(image_folder, image_name)

    with open(image_path, 'wb') as new_image:
        new_image.write(response.content)


def get_photos_from_launch() -> list:
    url = "https://api.spacexdata.com/v3/launches/67"
    response = requests.get(url).json()
    launch_photos = response['links']['flickr_images']
    return launch_photos


def fetch_spacex_last_launch() -> None:
    launch_photos = get_photos_from_launch()

    for photo_number, photo_url in enumerate(launch_photos):
        image_name = f'spacex_{photo_number}.jpg'
        download_image(photo_url, image_name=image_name)


if __name__ == '__main__':
    load_dotenv()
    fetch_spacex_last_launch()
