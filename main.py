import logging
import os
import pprint

from datetime import datetime
from urllib.parse import urlparse

import telegram
import requests

from dotenv import load_dotenv


def download_image(image_url: str, image_name: str, image_folder: str = 'images/') -> None:
    response = requests.get(image_url)

    os.makedirs(image_folder, exist_ok=True)
    image_path = os.path.join(image_folder, image_name)

    with open(image_path, 'wb') as new_image:
        new_image.write(response.content)


def get_file_extension(image_url):
    parsed_image_url = urlparse(image_url)
    return os.path.splitext(parsed_image_url.path)[-1]


def download_apod():
    """Get Astronomy Picture Of Day"""
    url = 'https://api.nasa.gov/planetary/apod'
    params = {
        'api_key': os.environ['NASA_API_KEY'],
        'count': 30
    }

    response = requests.get(url, params=params).json()

    for image_number, image_url in enumerate(response):
        if image_url.get('hdurl'):
            image_url_from_api = image_url['hdurl']
            image_extension = get_file_extension(image_url_from_api)
            image_name = f'nasa_apod_{image_number}{image_extension}'
            download_image(image_url_from_api, image_name=image_name)


def download_epic():
    all_images_url = 'https://api.nasa.gov/EPIC/api/natural/images'
    params = {
        'api_key': os.environ['NASA_API_KEY'],
    }
    response = requests.get(all_images_url, params=params).json()

    for image_number, image in enumerate(response):
        date = image['date']
        image_name = image['image']
        photo_datetime = datetime.strptime(date, '%Y-%m-%d %H:%M:%S')

        url = f'https://api.nasa.gov/EPIC/archive/natural/{photo_datetime.year}/' \
              f'{photo_datetime.month:02}/{photo_datetime.day}/png/{image_name}.png'
        response = requests.get(url, params=params)

        image_extension = get_file_extension(response.url)
        saved_image_name = f'EPIC_{image_number}{image_extension}'
        download_image(response.url, saved_image_name)


if __name__ == '__main__':
    load_dotenv()
    # download_apod()
    # download_epic()
