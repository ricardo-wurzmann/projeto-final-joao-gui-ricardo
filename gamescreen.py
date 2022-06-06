#import bibliotecas
from tkinter import font
import pygame
from os import path
from config import *
from sprites import *
from assets import load_assets
import random
import traceback


    
def gamescreen(Screen):

    tempo = pygame.time.Clock()

    PLAYING = 0
    DONE = 1
    world_speeds = -8


    assets = load_assets(IMG_DIR)

    # Carrega o fundo do jogo
    background = assets['fundo']

    background = pygame.transform.scale(background, (WIDTH, HEIGHT))
    background_rect = background.get_rect()


    player = Dino(assets['dino'])
    all_sprites = pygame.sprite.Group()
    all_cactos = pygame.sprite.Group()
    all_player = pygame.sprite.Group()
    all_player.add(player)
    all_sprites.add(player)

    global incrementa
    incrementa = 0

    world_sprites = pygame.sprite.Group()
    t = 0
    # Cria blocos espalhados em posições aleatórias do mapa

 
    state = PLAYING
    GAME = True
    #ajuste de velocidade

    global score

    score = 1
    score_min = 45
    n_cactos = 0
    dif = 0
    lista = []
    i = 0

    while state not in [END, QUIT]:
        score = score + 1
        dif += score // 50
        if dif >= 3:
            dif = 3
        if len(world_sprites) == 0:
            n_cactos = random.randint(0, dif)
        if len(world_sprites) < n_cactos:
            block_x = WIDTH + randint(100, 300) 
            block_y = CHAO - tam_cact  
            block = Cacto(assets['cacto'], block_x, block_y, world_speeds)
            world_sprites.add(block)
            all_cactos.add(block)
            # Adiciona também no grupo de todos os sprites para serem atualizados e desenhados
            all_sprites.add(block)
            
            if block.rect.x - world_sprites.sprites()[-1].rect.x >= 10 and block.rect.x - world_sprites.sprites()[-1].rect.x <= 600:
                world_sprites.remove(block)
                

    
            

        tempo.tick(FPS)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                state = QUIT
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE or event.key == pygame.K_UP:
                    player.pulo()
                if event.key == pygame.K_RETURN:
                    start_time = pygame.time.get_ticks()


            
        #Update
        all_sprites.update()


        
                


        Screen.fill((BLACK))  # Preenche com a cor preta


        background_rect.x += world_speeds
        i = 0

        if score%10 == 0:
            if world_speeds >= (-63):
                world_speeds -= 1
                
            for cacto in world_sprites:
                cacto.speedx = world_speeds
        
            
            

        
        if background_rect.right < 0:
            background_rect.x += background_rect.width
            
        Screen.blit(background, background_rect)

        background_rect2 = background_rect.copy()
        background_rect2.x += background_rect2.width
        Screen.blit(background, background_rect2)


        #desenha score
        text_surface = assets['fonte'].render("{:08d}".format(score), True, BLACK)
        text_rect = text_surface.get_rect()
        text_rect.midtop = (WIDTH / 2,  10)
        Screen.blit(text_surface, text_rect)
        
        all_sprites.draw(Screen)
        
        
        colisao = pygame.sprite.spritecollide(player, world_sprites, True, pygame.sprite.collide_mask)
        if len(colisao) != 0:
            state = END
            player.kill()
        
        
        # Depois de desenhar tudo, inverte o display.
        pygame.display.flip()
        pygame.display.update()
        tempo.tick(60)
    
    return state





