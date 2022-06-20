import os

from urllib.parse import urlparse

import requests


def download_image(image_url: str, image_name: str, image_folder: str = 'images/') -> None:
    response = requests.get(image_url)

    os.makedirs(image_folder, exist_ok=True)
    image_path = os.path.join(image_folder, image_name)

    with open(image_path, 'wb') as new_image:
        new_image.write(response.content)


def get_file_extension(image_url):
    parsed_image_url = urlparse(image_url)
    return os.path.splitext(parsed_image_url.path)[-1]
