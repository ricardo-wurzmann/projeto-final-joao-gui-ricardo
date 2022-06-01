
from turtle import width
import pygame
from os import path
from config import IMG_DIR, BLACK, FPS, GAME, QUIT, WIDTH, HEIGHT

# ----- Inicia assets
def telainicial(window):
    clock = pygame.time.Clock()
    image = pygame.image.load(path.join(IMG_DIR,'fundo_inicial.png')).convert()
    image = pygame.transform.scale(image, (WIDTH, HEIGHT))


    font = pygame.font.SysFont(None, 48)
    text = font.render( 'Aperte Qualquer Tecla para Jogar', True, (255, 255, 255))

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
                state = GAME
                inicial = False


        # ----- Gera saídas
        #image.blit(text,(20,100))
        window.blit(image, (0, 0))
        window.blit(text, (WIDTH/4, HEIGHT/2))
        
       
        
        # Depois de desenhar tudo, inverte o display.
        pygame.display.flip()
        pygame.display.update()

    return state
