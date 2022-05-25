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

'''class Cacto(pygame.sprite.Sprite):
    def __init__(self, cacto_img):
        pygame.sprite.Sprite.__init__(self)



        self.rect.x = random.randint(HEIGHT/2, 20)
        self.rect.y = random.randint(HEIGHT/2, 0)
        self.speedx = random.randint(-3, 3)
        self.speedy = random.randint(2, 9)

    def update(self):
        # Atualizando a posição do meteoro
        self.rect.x += self.speedx
        self.rect.y += self.speedy
        # Se o meteoro passar do final da tela, volta para cima e sorteia
        # novas posições e velocidades
        if self.rect.top > HEIGHT or self.rect.right < 0 or self.rect.left > WIDTH:
            self.rect.x = random.randint(0, WIDTH-METEOR_WIDTH)
            self.rect.y = random.randint(-100, -METEOR_HEIGHT)
            self.speedx = random.randint(-3, 3)
            self.speedy = random.randint(2, 9)'''
