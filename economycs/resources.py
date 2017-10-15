import pygame


IMAGES = {}

IMG_CITY = 'data/city.png'

IMAGES_TO_LOAD = [
    IMG_CITY
]


def load_resources():
    for path in IMAGES_TO_LOAD:
        img = pygame.image.load(path)
        IMAGES[path] = img
