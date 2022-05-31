from os import path
from random import randint
import pygame
import random

# Estabelece a pasta que contem as figuras e sons
IMG_DIR = path.join(path.dirname(__file__), 'Imagens')
SND_DIR = path.join(path.dirname(__file__), 'Sons')


# Dados gerais do jogo.
WIDTH = 600 # Largura da tela
HEIGHT = 300 # Altura da tela
FPS = 60 # Frames por segundo

# Define algumas variáveis com as cores básicas
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLUE = (0, 0, 255)
YELLOW = (255, 255, 0)

#imagens tela
personagem_width = 140
personagem_height = 100
cacto_width = 5
cacto_height = 7



# Estados para controle do fluxo da aplicação
INIT = 0
GAME = 1
END = 2
QUIT = 3

#gravidade 
GRAVIDADE = 1.6

#tamanho do pulo do jogador
TAM_PULO = 25

#distancia do pulo pro chao
CHAO = HEIGHT/1.3

#estados do jogador
PARADO = 0
PULANDO = 1
CAINDO = 2

#velocidade do mundo
world_speeds = -8

#tamanho cacto
tam_cact = random.randint(60, 125)

#cactos
INITIAL_BLOCKS = 1
TILE_SIZE = 80

#score
score = 1