from os import path
import pygame

# Estabelece a pasta que contem as figuras e sons
IMG_DIR = path.join(path.dirname(__file__), 'Imagens')
SND_DIR = path.join(path.dirname(__file__), 'Sons')


# Dados gerais do jogo.
WIDTH = 600 # Largura da tela
HEIGHT = 900 # Altura da tela
FPS = 60 # Frames por segundo

# Define algumas variáveis com as cores básicas
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLUE = (0, 0, 255)
YELLOW = (255, 255, 0)

#imagens tela
personagem_width = 50
personagem_height = 100
cacto_width = 10
cacto_height = 15

INITIAL_BLOCKS = 6
TILE_SIZE = 80


# Estados para controle do fluxo da aplicação
INIT = 0
GAME = 1
END = 2
QUIT = 3

#gravidade 
GRAVIDADE = 1.6

#tamanho do pulo do jogador
TAM_PULO = 30

#distancia do pulo pro chao
CHAO = HEIGHT*5/4

#estados do jogador
PARADO = 0
PULANDO = 1
CAINDO = 2

#velocidade do mundo
world_speeds = -8

#cactos
INITIAL_BLOCKS = 2
TILE_SIZE = 80
