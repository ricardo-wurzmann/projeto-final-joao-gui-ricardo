'''import pygame
import os
from config import IMG_DIR
from gamescreen import Dino


BACKGROUND = 'fundo1.png'
SHIP_IMG = 'dino.png'
#BULLET_IMG = 'bullet_img'


def load_assets():
    assets = {}
    assets[BACKGROUND] = pygame.image.load(os.path.join(IMG_DIR, 'starfield.png')).convert()
    assets[] = pygame.image.load(os.path.join(IMG_DIR, 'playerShip1_orange.png')).convert_alpha()
    assets[SHIP_IMG] = pygame.transform.scale(assets['ship_img'], (SHIP_WIDTH, SHIP_HEIGHT))
    assets[] = pygame.image.load(os.path.join(IMG_DIR, 'laserRed16.png')).convert_alpha()

    # Carrega os sons do jogo
    return assets'''
