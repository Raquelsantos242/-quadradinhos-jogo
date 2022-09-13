import pygame

pygame.init()
tela = pygame.display.set_mode((800, 600))

amarelo = (255, 255, 0)
vermelho = (255, 0, 0)
# Desenha um retângulo não preenchido com linha amarela
pygame.draw.rect(tela, amarelo, (10,10,200,100), 3)
# Desenha um retângulo todo preenchido de vermelho
pygame.draw.rect(tela, vermelho, (400,300,50,50))

terminou = False
while not terminou:
    # Atualiza o desenho na tela
    pygame.display.update()
    # Checar os eventos do mouse aqui:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            terminou = True

# Finaliza a janela do jogo
pygame.display.quit()
# Finaliza o pygame
pygame.quit()
