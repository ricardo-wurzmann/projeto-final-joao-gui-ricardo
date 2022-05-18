
from turtle import width
import pygame

pygame.init()

# ----- Gera tela principal
WIDTH = 600
HEIGHT = 300
window = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption('Jogo do Dinossauro')

# ----- Inicia estruturas de dados
running = True

# ----- Inicia assets
def telainical(tela):
    clock = pygame.time.Clock()
    image = pygame.image.load('projeto-final-joao-gui-ricardo/fundo1.png').convert()
    image = pygame.transform.scale(image, (WIDTH, HEIGHT))

    inicial = True

    font = pygame.font.SysFont(None, 48)
    text = font.render( 'Aperte Qualquer Tecla para Jogar', True, (255, 255, 255))
    window.blit(text, (20, 100))
    image.blit(text,(20,100))

    # ===== Loop principal =====
    while inicial:
        clock.tick(45)
        # ----- Trata eventos
        for event in pygame.event.get():
            # ----- Verifica consequências
            if event.type == pygame.QUIT:
                state = QUIT
                inicial = False
            if event.type == pygame.KEYUP:
                state = GAME
                inicial = False


        # ----- Gera saídas
        window.fill((0, 0, 0))  # Preenche com a cor branca
        window.blit(image, (10, 10))

        # ----- Atualiza estado do jogo
        pygame.display.update()  # Mostra o novo frame para o jogador

# ===== Finalização =====
pygame.quit()  