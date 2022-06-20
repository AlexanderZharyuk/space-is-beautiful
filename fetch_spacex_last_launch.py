import argparse

import requests

from main_functions import download_image


def fetch_spacex_last_launch(launch_id='latest') -> None:
    url = f"https://api.spacexdata.com/v3/launches/{launch_id}"
    response = requests.get(url).json()
    launch_photos = response['links']['flickr_images']

    for photo_number, photo_url in enumerate(launch_photos):
        image_name = f'spacex_{photo_number}.jpg'
        download_image(photo_url, image_name=image_name)


if __name__ == '__main__':
    parser = argparse.ArgumentParser(description='Download image from SpaceX.')
    parser.add_argument('launch_id', help='Launch id which you want download photos.', const='latest',
                        nargs='?', default='latest')
    args = parser.parse_args()
    try:
        fetch_spacex_last_launch(args.launch_id)
    except requests.exceptions.JSONDecodeError:
        print('Не найдены данные о последнем вылете, укажите айди')
