import os

from urllib.parse import urlparse

import requests


def download_image(image_url: str, image_path: str) -> None:
    response = requests.get(image_url)
    response.raise_for_status()

    image_folder = os.path.split(image_path)[0]
    os.makedirs(image_folder, exist_ok=True)

    with open(image_path, 'wb') as new_image:
        new_image.write(response.content)


def get_file_extension(image_url: str) -> str:
    parsed_image_url = urlparse(image_url)
    return os.path.splitext(parsed_image_url.path)[-1]
