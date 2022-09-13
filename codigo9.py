import pygame
import random

pygame.init()
largura_tela = 800
altura_tela = 600
quadrados_iniciais = 20
tela = pygame.display.set_mode((largura_tela, altura_tela))
terminou = False

# Cria relógio
clock = pygame.time.Clock()

preto = (0, 0, 0)
branco = (255, 255, 255)

# Vamos criar uma classe Quadradinho:
class Quadradinho():
    def __init__(self):
        self.largura = 30
        self.altura = 30
        self.x = random.randint(0, largura_tela-self.largura)
        self.y = random.randint(0, altura_tela-self.altura)
        self.area = pygame.Rect(self.x, self.y, self.largura, self.altura)
        self.cor = (random.randint(20, 255), random.randint(20, 255), random.randint(20, 255))

    def desenha(self, tela):
        pygame.draw.rect(tela, self.cor, self.area)

# Para imprimir o texto com o tempo
def mostra_tempo(tempo):
    font = pygame.font.Font(None, 24)
    text = font.render("Tempo: " + str(tempo) + "s", 1, branco)
    textpos = text.get_rect(centerx=tela.get_width()/2)
    tela.blit(text, textpos)

lista = []
for i in range(0, quadrados_iniciais):
    q = Quadradinho()
    q.desenha(tela)
    lista.append(q)

# Variavel para contar quantas esperas de 50Hz ou 0,02s
conta_clocks = 0

# Variavel para contar quantos segundos se passaram
conta_segundos = 0
mostra_tempo(conta_segundos)

while not terminou:

    # Checar os eventos do mouse aqui:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            terminou = True

    conta_clocks = conta_clocks + 1

    # A cada 50 cont_clocks, temos 1s (0,02s x 50 = 1s)
    if conta_clocks == 50:
        conta_segundos = conta_segundos + 1
        conta_clocks = 0
    
    # Limpar tela para atualizar o texto
    tela.fill(preto)

    # Já que toda tela foi apagada, desenhar quadradinhos novamente
    for i in lista:
        i.desenha(tela)
    
    # Mostra o tempo atualizado
    mostra_tempo(conta_segundos)

    # Atualiza o desenho na tela
    pygame.display.update()

    # Configura 50 atualizações de tela por segundo
    clock.tick(50) # 50 Hz ou 1/50s = 0,02s

# Finaliza a janela do jogo
pygame.display.quit()
# Finaliza o pygame
pygame.quit()
