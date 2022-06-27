import argparse
import os
import logging
import urllib.parse

import requests

from dotenv import load_dotenv

from general_functions import get_file_extension, download_image


def download_apod(api_key: str, dir_to_download: str, photos_count: int = 30) -> None:
    """Get Astronomy Picture Of Day"""
    url = 'https://api.nasa.gov/planetary/apod'
    params = {
        'api_key': api_key,
        'count': photos_count
    }

    response = requests.get(url, params=params)
    response.raise_for_status()

    for image_number, image_url in enumerate(response.json()):
        if image_url.get('hdurl'):
            image_url_from_api = urllib.parse.unquote(image_url['hdurl'], encoding='utf-8')
            image_extension = get_file_extension(image_url_from_api)
            image_name = f'nasa_apod_{image_number}{image_extension}'
            image_path = os.path.join(dir_to_download, image_name)
            try:
                download_image(image_url_from_api, image_path)
            except requests.HTTPError:
                continue


if __name__ == '__main__':
    load_dotenv()
    nasa_api_key = os.environ['NASA_API_KEY']
    dir_to_download = os.environ['DOWNLOAD_DIR']

    parser = argparse.ArgumentParser(description='Script for download APOD photos.')
    parser.add_argument('count', help='Count photos for download', const=30,
                        nargs='?', default=30)
    args = parser.parse_args()

    logging.basicConfig(format='[%(levelname)s]: %(message)s', datefmt='%m.%d.%Y %H:%M:%S', level=logging.INFO)
    try:
        download_apod(nasa_api_key, dir_to_download, args.count)
    except ConnectionError:
        logging.error('ConnectionError. Try again.')
