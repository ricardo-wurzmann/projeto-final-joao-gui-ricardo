#import bibliotecas
from distutils.util import change_root
from email.utils import parsedate_to_datetime
from turtle import Screen
import pygame
import random
from os import path
from config import IMG_DIR, BLACK, FPS, GAME, QUIT, WIDTH, HEIGHT, PARADO, PULANDO, CAINDO, GRAVIDADE, CHAO
import telainicial



pygame.init()

tempo = pygame.time.Clock()

window = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption('Jogo do Dino')

personagem_width = 40
personagem_height = 35
background = pygame.image.load(path.join(IMG_DIR,'fundo1.png')).convert()
personagem_img = pygame.image.load(path.join(IMG_DIR,'dino.png')).convert_alpha()
dino_img = pygame.transform.scale(personagem_img, (personagem_width, personagem_height))


#classes
class Dino(pygame.sprite.Sprite):
    def _init_(self, dino_img):
        pygame.sprite.Sprite._init_(self)
        self.state = PARADO
        dino_img = pygame.transform.scale(dino_img, (80, 140))
        self.image = dino_img    
        self.rect = self.image.get_rect()
        self.rect.center = (WIDTH / 3, HEIGHT / 3)
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
            self.speedy -= 0
            self.state = PULANDO

    
def gamescreen(Screen):
    tempo = pygame.time.Clock()
    player = Dino(dino_img)
    all_sprites = pygame.sprite.Group()
    player = personagem_img()
    all_sprites.add(player)
        


#repetir
    GAME = True
    #ajuste de velocidade


    while GAME:
        tempo.tick(FPS)
        for i in pygame.event.get():
            if i.type == pygame.QUIT():
                game = False
            
            if i.type == pygame.KEYDOWN:
                if i.key == pygame.K_SPACE or i.key == pygame.K_UP:
                    Dino.pulo()

    #Update
        all_sprites.uptade()
        window.fill((BLACK))  # Preenche com a cor preta
        all_sprites.draw(Screen)
        
    # Depois de desenhar tudo, inverte o display.
    pygame.display.flip()

pygame.init()
pygame.mixer.init()

try:
    gamescreen(Screen)
finally:
    pygame.quit()