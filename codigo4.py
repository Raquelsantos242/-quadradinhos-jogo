import pygame

pygame.init()
tela = pygame.display.set_mode((800, 600))

terminou = False

clock = pygame.time.Clock()

while not terminou:
    # Checar os eventos do mouse aqui:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            terminou = True

    # Fazemos a atualização aqui!

    # Atualiza o desenho na tela
    pygame.display.update()

    # Configura 50 atualizações de tela por segundo
    clock.tick(50)

# Finaliza a janela do jogo
pygame.display.quit()
# Finaliza o pygame
pygame.quit()
    
