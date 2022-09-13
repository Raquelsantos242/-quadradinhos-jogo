import pygame

pygame.init()

#--definição de constantes
largura_tela = 800
altura_tela = 600
red = (255,0,0)
green = (0,255,0)
blue = (0,0,255)
darkBlue = (0,0,128)
white = (255,255,255)
black = (0,0,0)
pink = (255,200,200)

tela = pygame.display.set_mode((largura_tela, altura_tela))
#tela.fill(cor)

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

