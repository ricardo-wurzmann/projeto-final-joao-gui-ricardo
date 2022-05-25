import pygame
from os import path
from config import *
from gamescreen import gamescreen
from telainicial import telainicial

pygame.init()

# ----- Gera tela principal
window = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption('Jogo do Dinossauro')

state = INIT
while state != QUIT:
    if state == INIT:
        state = telainicial(window)
    if state == GAME:
        state = gamescreen(window)

pygame.quit()