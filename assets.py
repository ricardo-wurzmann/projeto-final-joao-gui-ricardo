import pygame
import os
from config import *



def load_assets(IMG_DIR):
    assets = {}
    assets['dino'] = pygame.image.load(path.join(IMG_DIR, 'dino.png')).convert_alpha()
    assets['dino'] = pygame.transform.scale(assets['dino'], (80,100))
    assets['cacto'] = pygame.image.load(path.join(IMG_DIR, 'Cacto.png')).convert()
    assets['cacto'] = pygame.transform.scale(assets['cacto'], (80,tam_cact))
    assets['fundo'] = pygame.image.load(path.join(IMG_DIR, 'fundo1.png')).convert()
    assets['fundo'] = pygame.transform.scale(assets['fundo'], (2800,1400))
    
    return assets