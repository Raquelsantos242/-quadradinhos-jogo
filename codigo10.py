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
def mostra_tempo(tempo, pontuacao):
    font = pygame.font.Font(None, 24)
    text = font.render("Tempo: " + str(tempo) + "s | Pontuação: " + str(pontos), 1, branco)
    textpos = text.get_rect(centerx=tela.get_width()/2)
    tela.blit(text, textpos)

lista = []
for i in range(0, quadrados_iniciais):
    q = Quadradinho()
    q.desenha(tela)
    lista.append(q)

# Variável para contar os pontos
pontos = 0

# Variavel para contar quantas esperas de 50Hz ou 0,02s
conta_clocks = 0

# Variavel para contar quantos segundos se passaram
conta_segundos = 0
mostra_tempo(conta_segundos, pontos)


while not terminou:

    # Checar os eventos do mouse aqui:
    for event in pygame.event.get():
        
        # Clicando...
        if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
            # Obtém as coordenadas do mouse na tela
            pos = pygame.mouse.get_pos()
            # Checa se clicou em algum dos quadrados
            for q in lista:
                if q.area.collidepoint(pos):
                    lista.remove(q)
                    pontos = pontos + 1
                      
        if event.type == pygame.QUIT:
            terminou = True

    conta_clocks = conta_clocks + 1

    # A cada 50 cont_clocks, temos 1s (0,02s x 50 = 1s)
    if conta_clocks == 50:
        conta_segundos = conta_segundos + 1
        conta_clocks = 0
        # Cria um novo quadradinho a cada segundo
        q = Quadradinho()
        lista.append(q)

    # Limpar tela para atualizar o texto
    tela.fill(preto)
    
    # Vamos desenhar os quadradinhos novamente
    for q in lista:
        q.desenha(tela)
 
    # Mostra o tempo e pontuação atualizados
    mostra_tempo(conta_segundos, pontos)

    # Atualiza o desenho na tela
    pygame.display.update()

    # Configura 50 atualizações de tela por segundo
    clock.tick(50) # 50 Hz ou 1/50s = 0,02s

# Finaliza a janela do jogo
pygame.display.quit()
# Finaliza o pygame
pygame.quit()

