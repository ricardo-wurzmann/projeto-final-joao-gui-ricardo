#import bibliotecas
import pygame
import random


pygame.init()

#tela principal
WIDTH = 480
HEIGHT = 600
FPS = 40
tempo = pygame.time.Clock()

window = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption('Jogo do Dino')
personagem_width = 40
personagem_height = 35
font = pygame.font.SysFont(None, 48)
background = pygame.image.load('projeto-final-joao-gui-ricardo/fundo1.png').convert()
personagem_img = pygame.image.load('projeto-final-joao-gui-ricardo/dino.png').convert_alpha()
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
        self.rect.x += self.speedx

#repetir
game = True
#ajuste de velocidade
tempo = pygame.time.clock()
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