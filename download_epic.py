import argparse
import os
import logging
from urllib.parse import urlparse, parse_qsl, urlencode, urlunparse

from datetime import datetime

import requests

from dotenv import load_dotenv

from general_functions import get_file_extension, download_image


def download_epic(api_key: str, dir_to_download: str) -> None:
    all_images_url = 'https://api.nasa.gov/EPIC/api/natural/images'
    params = {
        'api_key': api_key,
    }
    response = requests.get(all_images_url, params=params)
    response.raise_for_status()

    for image_number, image in enumerate(response.json()):
        image_name = image['image']
        photo_created_year, photo_created_month, photo_created_day = \
            datetime.fromisoformat(image['date']).strftime("%Y/%m/%d").split('/')
        url = f'https://api.nasa.gov/EPIC/archive/natural/{photo_created_year}/' \
              f'{photo_created_month}/{photo_created_day}/png/{image_name}.png'

        url_parse = urlparse(url)
        query = url_parse.query
        url_dict = dict(parse_qsl(query))
        url_dict.update(params)
        url_new_query = urlencode(url_dict)
        url_parse = url_parse._replace(query=url_new_query)
        full_url = urlunparse(url_parse)

        image_extension = get_file_extension(url)
        saved_image_name = f'EPIC_{image_number}{image_extension}'
        image_path = os.path.join(dir_to_download, saved_image_name)
        download_image(full_url, image_path)


if __name__ == '__main__':
    load_dotenv()
    nasa_api_key = os.environ['NASA_API_KEY']
    dir_to_download = os.environ['DOWNLOAD_DIR']

    parser = argparse.ArgumentParser(description='Script for download EPIC photos.')
    parser.parse_args()
    logging.basicConfig(format='[%(levelname)s]: %(message)s', datefmt='%m.%d.%Y %H:%M:%S', level=logging.INFO)

    try:
        download_epic(nasa_api_key, dir_to_download)
    except ConnectionError:
        logging.error('ConnectionError. Try again.')
    except requests.HTTPError:
        logging.warning('Get HTTPError, some troubles with host?')
