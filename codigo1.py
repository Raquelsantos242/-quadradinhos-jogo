import pygame

pygame.init()
largura_tela = 800
altura_tela = 600
tela = pygame.display.set_mode((largura_tela, altura_tela))

#---- game loop -----------------------
terminou = False
while not terminou:

    # Atualiza o desenho na tela
    pygame.display.update()

    # Checar os eventos do mouse aqui:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            terminou = True

#---- fim do game loop -----------------------

# Finaliza a janela do jogo
pygame.display.quit()
# Finaliza o pygame
pygame.quit()
