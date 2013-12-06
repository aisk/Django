# coding: utf-8

import os

from PIL import Image

IMAGE_WIDTH = 630
IMAGE_HEIGHT = 460

def change_image_size(image_path):
    image = Image.open(image_path)
    image_path = str(image_path)
    width, height = image.size
    image.thumbnail((IMAGE_WIDTH, IMAGE_HEIGHT))
    os.remove(os.path.join('media', image_path))
    image.save(image_path)
