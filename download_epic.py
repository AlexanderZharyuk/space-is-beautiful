import argparse
import os
import logging

from datetime import datetime

import requests

from dotenv import load_dotenv

from general_functions import get_file_extension, download_image


def download_epic(api_key: str) -> None:
    all_images_url = 'https://api.nasa.gov/EPIC/api/natural/images'
    params = {
        'api_key': api_key,
    }
    response = requests.get(all_images_url, params=params)
    response.raise_for_status()

    for image_number, image in enumerate(response.json()):
        date = image['date']
        image_name = image['image']
        photo_datetime = datetime.strptime(date, '%Y-%m-%d %H:%M:%S')

        url = f'https://api.nasa.gov/EPIC/archive/natural/{photo_datetime.year}/' \
              f'{photo_datetime.month:02}/{photo_datetime.day}/png/{image_name}.png'
        response = requests.get(url, params=params)
        response.raise_for_status()

        image_extension = get_file_extension(response.url)
        saved_image_name = f'EPIC_{image_number}{image_extension}'
        download_image(response.url, saved_image_name)


if __name__ == '__main__':
    load_dotenv()
    nasa_api_key = os.environ['NASA_API_KEY']

    parser = argparse.ArgumentParser(description='Script for download EPIC photos.')
    parser.parse_args()
    logging.basicConfig(format='[%(levelname)s]: %(message)s', datefmt='%m.%d.%Y %H:%M:%S', level=logging.INFO)

    try:
        download_epic(nasa_api_key)
    except ConnectionError:
        logging.error('ConnectionError. Try again.')
    except requests.HTTPError:
        logging.warning('Get HTTPError, some troubles with host?')
