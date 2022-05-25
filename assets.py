import pygame
import os
from config import *


def load_assets():

    background = pygame.image.load(path.join(IMG_DIR,'fundo1.png')).convert()
    background = pygame.transform.scale(background, (WIDTH, HEIGHT))
    personagem_img = pygame.image.load(path.join(IMG_DIR,'dino.png')).convert_alpha()
    dino_img = pygame.transform.scale(personagem_img, (personagem_width, personagem_height))
    cacto_img = pygame.image.load(path.join(IMG_DIR,'Cacto.png')).convert_alpha() 
    cacto_img = pygame.transform.scale(cacto_img, (cacto_width, cacto_height))

    assets = {}
    assets[background] = pygame.image.load(os.path.join(IMG_DIR, 'fundo1.png')).convert()
    assets[dino_img] = pygame.image.load(os.path.join(IMG_DIR, 'dino.png')).convert_alpha()
    assets[cacto_img] = pygame.image.load(os.path.join(IMG_DIR, 'Cacto.png')).convert_alpha()

    # Carrega os sons do jogo
    return assets
