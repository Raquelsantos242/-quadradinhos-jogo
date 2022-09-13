import pygame

pygame.init()
tela = pygame.display.set_mode((800, 600))

terminou = False
while not terminou:
    # Checar os eventos do mouse aqui:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            terminou = True

    # Fazemos a atualização aqui!

    # Atualiza o desenho na tela
    pygame.display.update()

# Finaliza a janela do jogo
pygame.display.quit()
# Finaliza o pygame
pygame.quit()
  
