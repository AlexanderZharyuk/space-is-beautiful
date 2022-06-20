import argparse
import os

import requests

from dotenv import load_dotenv

from main_functions import get_file_extension, download_image


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
    parser = argparse.ArgumentParser(description='Script for download APOD photos.')
    parser.parse_args()
    download_apod()
