
from turtle import width
import pygame
from config import IMG_DIR, BLACK, FPS, GAME, INIT, QUIT
import gamescreen


pygame.init()

# ----- Gera tela principal
WIDTH = 600
HEIGHT = 300
window = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption('Jogo do Dinossauro')

# ----- Inicia estruturas de dados
running = True

# ----- Inicia assets
def telafinal(tela):
    clock = pygame.time.Clock()
    image = pygame.image.load(IMG_DIR,'gameover.png').convert()
    image = pygame.transform.scale(image, (WIDTH, HEIGHT))

    font = pygame.font.SysFont(None, 48)
    text = font.render( 'Para jogar novamente digite qualquer tecla', True, (255, 255, 255))
    window.blit(text, (20, 100))
    image.blit(text,(20,100))

    inicial = True
    # ===== Loop principal =====
    while inicial:
        clock.tick(FPS)
        # ----- Trata eventos
        for event in pygame.event.get():
            # ----- Verifica consequências
            if event.type == pygame.QUIT:
                state = QUIT
                inicial = False
            #Para entrar no jogo
            if event.type == pygame.KEYUP:
                state = INIT
                inicial = False

        #falta play again


        # ----- Gera saídas
        window.fill((BLACK))  # Preenche com a cor branca
        window.blit(image, (0, 0))
        
        # Depois de desenhar tudo, inverte o display.
        pygame.display.flip()

    return state

screen = pygame.display.set_mode((600, 300))

gamescreen.gamescreen(screen)

# ===== Finalização =====
pygame.quit()  