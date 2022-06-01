import pygame
import random
from config import *

#classes
class Dino(pygame.sprite.Sprite):
    def __init__(self, dino_img):
        pygame.sprite.Sprite.__init__(self)
        self.state = PARADO
        self.image = dino_img    
        self.rect = self.image.get_rect()
        self.rect.centerx = (WIDTH / 3)
        self.rect.top = 0
        self.speedy = 0
        self.rect.bottom = int(HEIGHT * 5 / 8)

    def update(self):
        self.speedy += GRAVIDADE
        if self.speedy > 0:
            self.state = CAINDO
        self.rect.y += self.speedy
        if self.rect.bottom > CHAO:
            self.rect.bottom = CHAO 
            self.speedy = 0
            self.state = PARADO

    def pulo(self):
        if self.state == PARADO:
            self.speedy -= TAM_PULO
            self.state = PULANDO



class Cacto(pygame.sprite.Sprite):
    def __init__(self, img, x, y, speedx):
        pygame.sprite.Sprite.__init__(self)
        self.image = img
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y
        self.speedx = speedx

    def update(self):
        self.rect.x += self.speedx

    def velocidade(self, speedx):
        self.speedx = speedx


