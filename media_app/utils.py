import os

import cv2
import numpy as np
from PIL import Image

from app import settings

THUMBNAIL_STRING = '_thumbnail.'
THUMBNAIL_VALUE = (150, 150)

SIZE_WEBM = (640, 480)
TOP_TEN_LABEL = 'top_ten.webm'


def save_thumbnail_image(file):
    img = Image.open(file)
    photo_name = file.name.split('.')[0] + THUMBNAIL_STRING + img.format
    if img.height > THUMBNAIL_VALUE[0] or img.width > THUMBNAIL_VALUE[1]:
        img.thumbnail(THUMBNAIL_VALUE)
    img.save(settings.MEDIA_ROOT + '/' + photo_name)


def get_url_thumbnail_image(file):
    path, format_image = file.url.split('.')
    if format_image == 'jpg':
        format_image = 'JPEG'

    filename = path.split('/')[-1] + THUMBNAIL_STRING + format_image.upper()
    if not os.path.exists(settings.MEDIA_ROOT + '/' + filename):
        return 'media/default.jpeg'

    return path + THUMBNAIL_STRING + format_image.upper()


def save_webp_image(file):
    img = Image.open(file).convert("RGB")
    photo_name = file.name.split('.')[0] + ".webp"
    img.save(settings.MEDIA_ROOT + '/' + photo_name, "WEBP")


def get_url_format_image(file, format):
    path = file.url.split('.')[0]
    return path + '.' + format.upper()


def create_animation(files):
    img_array = []
    fourcc = cv2.VideoWriter_fourcc('v', 'p', '8', '0')
    out = cv2.VideoWriter(settings.MEDIA_ROOT + '/' + TOP_TEN_LABEL, fourcc, 1, SIZE_WEBM)

    for filename in files:
        img = cv2.imread(settings.MEDIA_ROOT + '/' + filename)
        img = cv2.resize(img, SIZE_WEBM)
        height, width, layers = img.shape
        size = (width, height)
        img_array.append(img)

    for i in range(len(img_array)):
        out.write(img_array[i])
    out.release()
    return settings.MEDIA_ROOT + '/' + TOP_TEN_LABEL
