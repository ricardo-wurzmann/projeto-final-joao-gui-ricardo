
from turtle import width
import pygame
from config import *
import gamescreen
import assets




# ----- Inicia estruturas de dados
running = True

# ----- Inicia assets
def telafinal(window):
    image = pygame.image.load(path.join(IMG_DIR,'gameover.png')).convert()
    image = pygame.transform.scale(image, (WIDTH, HEIGHT))
    print ('telafinal')

    clock = pygame.time.Clock()
    font = pygame.font.SysFont(None, 48)
    text = font.render( 'Para jogar novamente digite qualquer tecla', True, (255, 255, 255))
    window.blit(text, (20, 100))


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
          # Preenche com a cor branca
        window.blit(image, (0, 0))
        
        # Depois de desenhar tudo, inverte o display.
        pygame.display.flip()

    return state


