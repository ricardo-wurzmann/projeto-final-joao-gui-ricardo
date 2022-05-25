import pygame
import os
from config import *



def load_assets(IMG_DIR):
    assets = {}
    assets['dino'] = pygame.image.load(path.join(IMG_DIR, 'dino.png')).convert_alpha()
    assets['cacto'] = pygame.image.load(path.join(IMG_DIR, 'Cacto.png')).convert()
    assets['fundo'] = pygame.image.load(path.join(IMG_DIR, 'fundo1.png')).convert()
    return assets