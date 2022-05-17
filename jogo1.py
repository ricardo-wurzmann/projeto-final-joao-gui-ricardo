#import bibliotecas
import pygame
import random
import time

pygame.init()

#tela principal
WIDTH = 480
HEIGHT = 600
window = pygame.display.set_mode((WIDTH, HEIGHT))
personagem_width = 40
personagem_height = 35
font = pygame.font.SysFont(None, 48)
background = pygame.image.load('projeto-final-joao-gui-ricardo/fundo.png').convert()
personagem_img = pygame.image.load('projeto-final-joao-gui-ricardo/dino.png').convert_alpha()
meteor_img = pygame.transform.scale(personagem_img, (personagem_width, personagem_height))



#classes

#sprite for player


#background

#repetir