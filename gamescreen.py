#import bibliotecas
import pygame
from os import path
from config import IMG_DIR, BLACK, FPS, GAME, QUIT, WIDTH, HEIGHT, PARADO, PULANDO, CAINDO, GRAVIDADE, CHAO, TAM_PULO
from sprites import Dino
    
def gamescreen(Screen):

    personagem_width = 80
    personagem_height = 140
    background = pygame.image.load(path.join(IMG_DIR,'fundo1.png')).convert()
    personagem_img = pygame.image.load(path.join(IMG_DIR,'dino.png')).convert_alpha()
    dino_img = pygame.transform.scale(personagem_img, (personagem_width, personagem_height))
    background = pygame.transform.scale(background, (WIDTH, HEIGHT))


    tempo = pygame.time.Clock()
    player = Dino(dino_img)
    all_sprites = pygame.sprite.Group()
    all_sprites.add(player)

    PLAYING = 0
    DONE = 1

#repetir
    
    state = PLAYING
    GAME = True
    #ajuste de velocidade

    while state not in [DONE, QUIT]:
        tempo.tick(FPS)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                state = QUIT
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE or event.key == pygame.K_UP:
                    player.pulo()
            
        #Update
        all_sprites.update()
        Screen.fill((BLACK))  # Preenche com a cor preta
        all_sprites.draw(Screen)
        
        # Depois de desenhar tudo, inverte o display.
        pygame.display.flip()
        pygame.display.update()
        
    return state
