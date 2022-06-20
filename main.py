import logging
import os
import pprint

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


if __name__ == '__main__':
    load_dotenv()
    download_apod()

