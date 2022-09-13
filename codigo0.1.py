import pygame
pygame.init()
# Todo o código deve fica aqui
largura_tela = 640
altura_tela = 480

tela = pygame.display.set_mode((largura_tela, altura_tela))

#---- game loop -----------------------
terminou = False
while not terminou:    
  # Checar os eventos do mouse aqui:
  for event in pygame.event.get():
          if event.type == pygame.QUIT:
              terminou = True

#---- game loop -----------------------
#
pygame.display.quit()
pygame.quit()