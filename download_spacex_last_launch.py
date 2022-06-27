import argparse
import logging
import os

import requests

from dotenv import load_dotenv

from general_functions import download_image


def fetch_spacex_last_launch(dir_to_download: str, launch_id='latest') -> None:
    url = f"https://api.spacexdata.com/v3/launches/{launch_id}"
    response = requests.get(url)
    response.raise_for_status()

    launch_photos = response.json()['links']['flickr_images']

    for photo_number, photo_url in enumerate(launch_photos):
        image_name = f'spacex_{photo_number}.jpg'
        image_path = os.path.join(dir_to_download, image_name)
        download_image(photo_url, image_path)


if __name__ == '__main__':
    load_dotenv()
    dir_to_download = os.environ['DOWNLOAD_DIR']

    parser = argparse.ArgumentParser(description='Download image from SpaceX.')
    parser.add_argument('launch_id', help='Launch id which you want download photos.', const='latest',
                        nargs='?', default='latest')
    args = parser.parse_args()

    logging.basicConfig(format='[%(levelname)s]: %(message)s', datefmt='%m.%d.%Y %H:%M:%S', level=logging.INFO)
    try:
        fetch_spacex_last_launch(dir_to_download, args.launch_id)
    except requests.exceptions.JSONDecodeError:
        logging.info("Can't find latest launch id. Try run script with number of launch id.")
    except ConnectionError:
        logging.error('ConnectionError, try again.')
    except requests.HTTPError:
        logging.warning('Get HTTPError, some troubles with host?')