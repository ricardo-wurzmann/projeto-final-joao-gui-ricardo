import pygame
import os
from config import *


def load_assets():
    assets = {}
    assets[background] = pygame.image.load(os.path.join(IMG_DIR, 'fundo1.png')).convert()
    assets[dino_img] = pygame.image.load(os.path.join(IMG_DIR, 'dino.png')).convert_alpha()
    assets[dino_img] = pygame.transform.scale(assets['ship_img'], (personagem_width, personagem_height))
    assets[cacto_img] = pygame.image.load(os.path.join(IMG_DIR, 'Cacto.png')).convert_alpha()

    # Carrega os sons do jogo
    return assets
