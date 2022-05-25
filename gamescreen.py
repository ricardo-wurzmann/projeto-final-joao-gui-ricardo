#import bibliotecas
import pygame
from os import path
from config import *
from sprites import *
import assets
import random


    
def gamescreen(Screen):

    tempo = pygame.time.Clock()

    PLAYING = 0
    DONE = 1


    assets = IMG_DIR

    background = assets[background]

    background = pygame.transform.scale(background, (WIDTH, HEIGHT))
    background_rect = background.get_rect()


    player = Dino(dino_img)
    all_sprites = pygame.sprite.Group()
    all_sprites.add(player)


    world_sprites = pygame.sprite.Group()
    # Cria blocos espalhados em posições aleatórias do mapa
    for i in range(INITIAL_BLOCKS):
        block_x = random.randint(0, WIDTH)
        block_y = random.randint(0, int(HEIGHT * 0.5))
        block = Cacto(assets[cacto_img], block_x, block_y, world_speeds)
        world_sprites.add(block)
        # Adiciona também no grupo de todos os sprites para serem atualizados e desenhados
        all_sprites.add(block)

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

        for block in world_sprites:
            if block.rect.right < 0:
                # Destrói o bloco e cria um novo no final da tela
                block.kill()
                block_x = random.randint(WIDTH, int(WIDTH * 1.5))
                block_y = random.randint(0, int(HEIGHT * 0.5))
                new_block = Cacto(assets[cacto_img], block_x, block_y, world_speeds)
                all_sprites.add(new_block)
                world_sprites.add(new_block)

        Screen.fill((BLACK))  # Preenche com a cor preta

        background_rect.x += world_speeds
        # Se o fundo saiu da janela, faz ele voltar para dentro.
        if background_rect.right < 0:
            background_rect.x += background_rect.width
        # Desenha o fundo e uma cópia para a direita.
        # Assumimos que a imagem selecionada ocupa pelo menos o tamanho da janela.
        # Além disso, ela deve ser cíclica, ou seja, o lado esquerdo deve ser continuação do direito.
        Screen.blit(background, background_rect)
        # Desenhamos a imagem novamente, mas deslocada da largura da imagem em x.
        background_rect2 = background_rect.copy()
        background_rect2.x += background_rect2.width
        Screen.blit(background, background_rect2)

        
        all_sprites.draw(Screen)
        
        # Depois de desenhar tudo, inverte o display.
        pygame.display.flip()
        pygame.display.update()





