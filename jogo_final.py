while GAME:
        tempo.tick(FPS)
        for i in pygame.event.get():
            if i.type == pygame.QUIT():
                GAME = False
            
            if i.type == pygame.KEYDOWN:
                if i.key == pygame.K_SPACE or i.key == pygame.K_UP:
                    Dino.pulo()