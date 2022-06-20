import argparse
from datetime import datetime
import os

import requests

from dotenv import load_dotenv

from main_functions import get_file_extension, download_image


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
    parser = argparse.ArgumentParser(description='Script for download EPIC photos.')
    parser.parse_args()
    download_epic()
