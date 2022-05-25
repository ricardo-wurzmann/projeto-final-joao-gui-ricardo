# -*- coding: utf-8 -*-
#exemplo github
'''

class Cacto(pygame.sprite.Sprite):

    # Construtor da classe.
    def __init__(self, Cacto_img, x, y, speedx):
        pygame.sprite.Sprite.__init__(self)
        tile_img = pygame.transform.scale(tile_img, (TILE_SIZE, TILE_SIZE))
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y
        self.speedx = speedx

    def update(self):
        self.rect.x += self.speedx




def game_screen(screen):
    # Variável para o ajuste de velocidade
    clock = pygame.time.Clock()

    # Carrega assets
    assets = load_assets(img_dir)





        # Atualiza a posição da imagem de fundo.
        
        all_sprites.draw(screen)

        # Depois de desenhar tudo, inverte o display.
        pygame.display.flip()


# Inicialização do Pygame.
pygame.init()
pygame.mixer.init()

# Tamanho da tela.
screen = pygame.display.set_mode((WIDTH, HEIGHT))

# Nome do jogo
pygame.display.set_caption(TITULO)

# Imprime instruções
print('*' * len(TITULO))
print(TITULO.upper())
print('*' * len(TITULO))
print('Este exemplo não é interativo.')

# Comando para evitar travamentos.
try:
    game_screen(screen)
finally:
    pygame.quit()'''