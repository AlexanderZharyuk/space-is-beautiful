import argparse
import os
import logging

import requests

from dotenv import load_dotenv

from general_functions import get_file_extension, download_image


def download_apod(api_key: str) -> None:
    """Get Astronomy Picture Of Day"""
    url = 'https://api.nasa.gov/planetary/apod'
    params = {
        'api_key': api_key,
        'count': 30
    }

    response = requests.get(url, params=params)
    response.raise_for_status()

    for image_number, image_url in enumerate(response.json()):
        if image_url.get('hdurl'):
            image_url_from_api = image_url['hdurl'].replace('%20', '')
            image_extension = get_file_extension(image_url_from_api)
            image_name = f'nasa_apod_{image_number}{image_extension}'
            try:
                download_image(image_url_from_api, image_name=image_name)
            except requests.HTTPError:
                continue


if __name__ == '__main__':
    load_dotenv()
    nasa_api_key = os.environ['NASA_API_KEY']

    parser = argparse.ArgumentParser(description='Script for download APOD photos.')
    parser.parse_args()

    logging.basicConfig(format='[%(levelname)s]: %(message)s', datefmt='%m.%d.%Y %H:%M:%S', level=logging.INFO)
    try:
        download_apod(nasa_api_key)
    except ConnectionError:
        logging.error('ConnectionError. Try again.')
