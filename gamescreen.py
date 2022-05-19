#import bibliotecas
import pygame
import random
from os import path
from config import IMG_DIR, BLACK, FPS, GAME, QUIT, WIDTH, HEIGHT
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
    def _init_(self, img):
        pygame.sprite.Sprite._init_(self)
        self.image = img
        self.image = pygame.Surface(50, 50)
        self.image.fill(personagem_img)
        self.rect = self.image.get_rect()
        self.rect.center = (WIDTH / 3, HEIGHT / 3)
        self.speedx = 0

    def update(self):

#repetir
game = True
#ajuste de velocidade
tempo = pygame.time.Clock()
player = Dino(dino_img)

all_sprites = pygame.sprite.Group()
player = personagem_img()
all_sprites.add(player)

while game:
    tempo.tick(FPS)
    for i in pygame.event.get():
        if i.type == pygame.QUIT():
            game = False

    #Update
    all_sprites.uptade()


pygame.quit()