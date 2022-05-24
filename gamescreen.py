#import bibliotecas
from distutils.util import change_root
from email.utils import parsedate_to_datetime
from telnetlib import DO
from turtle import Screen
import pygame
import random
from os import path
from config import IMG_DIR, BLACK, FPS, GAME, QUIT, WIDTH, HEIGHT, PARADO, PULANDO, CAINDO, GRAVIDADE, CHAO, TAM_PULO
import telainicial


pygame.init()

tempo = pygame.time.Clock()

window = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption('Jogo do Dino')

personagem_width = 80
personagem_height = 140
background = pygame.image.load(path.join(IMG_DIR,'fundo1.png')).convert()
personagem_img = pygame.image.load(path.join(IMG_DIR,'dino.png')).convert_alpha()
dino_img = pygame.transform.scale(personagem_img, (personagem_width, personagem_height))


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

    
def gamescreen(Screen):
    tempo = pygame.time.Clock()
    player = Dino(dino_img)
    all_sprites = pygame.sprite.Group()
    all_sprites.add(player)

    PLAYING = 0
    DONE = 1
        


#repetir
    
    state = PLAYING
    GAME = True
    #ajuste de velocidade

    while state != DONE:
        tempo.tick(FPS)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                state = DONE
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE or event.key == pygame.K_UP:
                    player.pulo()
            
    #Update
        all_sprites.update()
        Screen.fill((BLACK))  # Preenche com a cor preta
        all_sprites.draw(Screen)
        
    # Depois de desenhar tudo, inverte o display.
    pygame.display.flip()

pygame.init()

Screen = pygame.display.set_mode((600, 300))

pygame.quit()