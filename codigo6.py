import pygame
import random

pygame.init()
largura_tela = 800
altura_tela = 600
tela = pygame.display.set_mode((largura_tela, altura_tela))
terminou = False

# Cria relógio
clock = pygame.time.Clock()

cor = (random.randint(20, 255), random.randint(20, 255), random.randint(20, 255))
area = (random.randint(0, largura_tela-30), random.randint(0, altura_tela-30), 30, 30)
pygame.draw.rect(tela, cor, area)

cor = (random.randint(20, 255), random.randint(20, 255), random.randint(20, 255))
area = (random.randint(0, largura_tela-30), random.randint(0, altura_tela-30), 30, 30)
pygame.draw.rect(tela, cor, area)

while not terminou:

    # Checar os eventos do mouse aqui:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            terminou = True

    # Atualiza o desenho na tela
    pygame.display.update()

    # Configura 50 atualizações de tela por segundo
    clock.tick(50)

# Finaliza a janela do jogo
pygame.display.quit()
# Finaliza o pygame
pygame.quit()
