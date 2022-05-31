#import bibliotecas
from curses import window
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

    assets = load_assets(IMG_DIR)

    # Carrega o fundo do jogo
    background = assets['fundo']

    background = pygame.transform.scale(background, (WIDTH, HEIGHT))
    background_rect = background.get_rect()


    player = Dino(assets['dino'])
    all_sprites = pygame.sprite.Group()
    all_player = pygame.sprite.Group()
    all_player.add(player)
    all_sprites.add(player)


    world_sprites = pygame.sprite.Group()
    t = 0
    # Cria blocos espalhados em posições aleatórias do mapa
    for i in range(INITIAL_BLOCKS):
        block_x = random.randint(0, WIDTH)
        block_y = random.randint(0, int(HEIGHT * 0.5))
        block = Cacto(assets['cacto'], block_x, block_y, world_speeds)
        world_sprites.add(block)
        # Adiciona também no grupo de todos os sprites para serem atualizados e desenhados
        all_sprites.add(block)

#repetir
    
    state = PLAYING
    GAME = True
    #ajuste de velocidade

    while state not in [END, QUIT]:
        t += 1
#        score = score * 1.8
        


        tempo.tick(FPS)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                state = QUIT
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE or event.key == pygame.K_UP:
                    player.pulo()
                if event.key == pygame.K_RETURN:
                    start_time = pygame.time.get_ticks()


                
        pygame.display.update()


        #desenha score
        '''text_surface = assets[score].render("{:08d}".format(score), True, YELLOW)
        text_rect = text_surface.get_rect()
        text_rect.midtop = (WIDTH / 2,  10)
        window.blit(text_surface, text_rect)'''

            
        #Update
        all_sprites.update()

        for block in world_sprites:
            if block.rect.right < 0:
                # Destrói o bloco e cria um novo no final da tela
                block.kill()
                block_x = random.randint(WIDTH, int(WIDTH * 3))
                block_y = CHAO-tam_cact
                new_block = Cacto(assets['cacto'], block_x, block_y, world_speeds)
                all_sprites.add(new_block)
                world_sprites.add(new_block)


        Screen.fill((BLACK))  # Preenche com a cor preta

        background_rect.x += world_speeds
        
        if background_rect.right < 0:
            background_rect.x += background_rect.width
            
        Screen.blit(background, background_rect)

        background_rect2 = background_rect.copy()
        background_rect2.x += background_rect2.width
        Screen.blit(background, background_rect2)
        
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





