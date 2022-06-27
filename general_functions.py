import os

from urllib.parse import urlparse

import requests

from dotenv import load_dotenv


load_dotenv()


def download_image(image_url: str, image_name: str, image_folder: str = os.environ['DOWNLOAD_DIR']) -> None:
    response = requests.get(image_url)
    response.raise_for_status()

    os.makedirs(image_folder, exist_ok=True)
    image_path = os.path.join(image_folder, image_name)

    with open(image_path, 'wb') as new_image:
        new_image.write(response.content)


def get_file_extension(image_url: str) -> str:
    parsed_image_url = urlparse(image_url)
    return os.path.splitext(parsed_image_url.path)[-1]
