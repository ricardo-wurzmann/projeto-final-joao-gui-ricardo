
from turtle import width
import pygame

pygame.init()

# ----- Gera tela principal
WIDTH = 600
HEIGHT = 300
window = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption('Jogo do Dinossauro')

# ----- Inicia estruturas de dados
game = True

# ----- Inicia assets
image = pygame.image.load('projeto-final-joao-gui-ricardo/fundo1.png').convert()
image = pygame.transform.scale(image, (WIDTH, HEIGHT))

inicial = True

font = pygame.font.SysFont(None, 48)
text = font.render( 'Aperte Qualquer Tecla para Jogar', True, (255, 255, 255))
window.blit(text, (20, 100))
image.blit(text,(20,100))

# ===== Loop principal =====
while inicial:
    # ----- Trata eventos
    for event in pygame.event.get():
        # ----- Verifica consequências
        if event.type == pygame.KEYUP:
            inicial = False

    # ----- Gera saídas
    window.fill((0, 0, 0))  # Preenche com a cor branca
    window.blit(image, (10, 10))

    # ----- Atualiza estado do jogo
    pygame.display.update()  # Mostra o novo frame para o jogador

# ===== Finalização =====
pygame.quit()  