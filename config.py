from os import path
import pygame

# Estabelece a pasta que contem as figuras e sons.


IMG_DIR = path.join(path.dirname(__file__), 'Imagens')
SND_DIR = path.join(path.dirname(__file__), 'Sons')



# Dados gerais do jogo.
WIDTH = 300 # Largura da tela
HEIGHT = 600 # Altura da tela
FPS = 60 # Frames por segundo

# Define tamanhos
METEOR_WIDTH = 50
METEOR_HEIGHT = 38
SHIP_WIDTH = 50
SHIP_HEIGHT = 38

# Define algumas variáveis com as cores básicas
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLUE = (0, 0, 255)
YELLOW = (255, 255, 0)

# Estados para controle do fluxo da aplicação
INIT = 0
GAME = 1
QUIT = 2

#gravidade 
GRAVIDADE = 2

#tamanho do pulo do jogador
tam_pulo = 3

#distancia do pulo pro chao
CHAO = HEIGHT*5/4

#estados do jogador
PARADO = 0
PULANDO = 1
CAINDO = 2