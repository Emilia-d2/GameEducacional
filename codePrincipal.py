import pygame
import random
import time
pygame.init()

pygame.display.set_caption("Sítio da Mili Pika")
icone = pygame.image.load("icon.ico")
pygame.display.set_icon(icone)
largura = 800
altura = 600
display = pygame.display.set_mode((largura, altura))
emiliaImg = pygame.image.load('emilia.png')
cenario = pygame.image.load('cenario.jpg')
cucaImg = pygame.image.load('cuca.png')
pedrinhoImg = pygame.image.load('pedrinho.png')
narizinhoImg = pygame.image.load('narizinho.png')
viscondeImg = pygame.image.load('visconde.png')
risadaCuca = pygame.mixer.Sound("risadaCuca.mp3")
fundoMusical = pygame.mixer.Sound("fundo.mp3")
black = (0, 0, 0)
white = (255, 255, 255)


def mostrarEmilia(x, y):
  display.blit(emiliaImg, (x, y))

def texo_tela(texto, fonte):
  textoTela = fonte.render(texto, True, black)
  return textoTela, textoTela.get_rect()

def mensagem_tela(text):
  fonte = pygame.font.Font("freesansbold.ttf", 45)
  texto1, textRect = texo_tela(text, fonte)
  textRect.center = ((largura/2), (altura/2))
  display.blit(texto1, textRect)
  pygame.display.update()
  time.sleep(5)
  inicio_jogo()

def dead():
  pygame.mixer.Sound.play(risadaCuca)
  pygame.mixer.music.stop()
  mensagem_tela("A CUCA TE PEGOU HAHA!!")

def mostraAcertos(acertos):
  font = pygame.font.Font(None, 50)
  texto = font.render("Acertos:" +str(acertos), True, black)
  display.blit(texto, (0, 0))

def vitoria(acertos):
  pygame.mixer.music.stop()
  mensagem_tela("Parabés! Seu total esperado é " + str(acertos))

def arquivoTXT():
  usuario = input("Usuário:\n")
  login = input("E-mail:\n")
  arquivo = open('dados.txt', 'a')
  arquivo.write("E-mail: ")                                                                                                              
  arquivo.write(login)
  arquivo.write("\n")
  arquivo.write("Usuario: ")
  arquivo.write(usuario)
  arquivo.write("\n")
  arquivo.close()

def inicio_jogo():
  contadorNarizinho = 0
  contadorPedrinho = 0
  contadorVisconde = 0

  arquivoTXT()
  time = pygame.time.Clock()
  pygame.mixer.music.load('fundo.mp3')
  pygame.mixer.music.play(-1) 

  emiliaPosicaoX = (altura * 0.8)
  emiliaPosicaoY = (largura * 0.6)
  emiliaLargura = 120
  movimentaX = 0

  cucaLargura = 81
  cucaAltura = 123
  cucaPosicaoX = (largura * 0.8)
  cucaPosicaoY = -220

  narizinhoAltura = 101
  narizinhoLargura = 58
  narizinhoPosicaoX = (largura * 0.6)
  narizinhoPosicaoY = -220
  habilitaNarizinho = False

  pedrinhoAltura = 78
  pedrinhoLargura = 75
  pedrinhoPosicaoX = (largura * 0.25)
  pedrinhoPosicaoY = -220
  habilitaPedrinho = False

  viscondeAltura = 103
  viscondeLargura = 56
  viscondePosicaoX = (largura * 0.45)
  viscondePosicaoY = -220
  habilitaVisonde = False

  velocidadeCuca = 5
  velocidadeVisconde = 1
  velocidadeNarizinho = 2
  velocidadePedrinho = 7

  while True:
    for event in pygame.event.get():
      if event.type == pygame.QUIT:
        pygame.quit()

    if event.type == pygame.KEYDOWN:
      if event.key == pygame.K_LEFT:
        movimentaX = -3
      elif event.key == pygame.K_RIGHT:
        movimentaX = 3
    if event.type == pygame.KEYUP:
      if event.key == pygame.K_LEFT or event.key == pygame.K_RIGHT:
        movimentaX = 0

    display.fill(white)
    display.blit(cenario, (0, 0))
    emiliaPosicaoX = emiliaPosicaoX + movimentaX

    if emiliaPosicaoX < 0:
      emiliaPosicaoX = 0
    elif emiliaPosicaoX > 680:
      emiliaPosicaoX = 680

    mostrarEmilia(emiliaPosicaoX, emiliaPosicaoY)

    display.blit(cucaImg, (cucaPosicaoX, cucaPosicaoY))
    cucaPosicaoY = cucaPosicaoY + velocidadeCuca

    if cucaPosicaoY > altura:
      cucaPosicaoY = -220
      velocidadeCuca += +1
      cucaPosicaoX = random.randrange(0, largura)

    if narizinhoPosicaoY > altura:
      narizinhoPosicaoY = -220
      velocidadeNarizinho += +1
      narizinhoPosicaoX = random.randrange(0, largura)

    if pedrinhoPosicaoY > altura:
      pedrinhoPosicaoY = -220
      velocidadePedrinho += +1
      pedrinhoPosicaoX = random.randrange(0, largura)

    if viscondePosicaoY > altura:
      viscondePosicaoY = -220
      velocidadeVisconde += +1
      viscondePosicaoX = random.randrange(0, largura)

    if emiliaPosicaoY < cucaPosicaoY + cucaAltura:
      if emiliaPosicaoX < cucaPosicaoX and emiliaPosicaoX + emiliaLargura > cucaPosicaoX or cucaPosicaoX + cucaLargura > emiliaPosicaoX and cucaPosicaoX + cucaLargura < emiliaPosicaoX + emiliaLargura:
        dead()

    sorteia = random.randrange(0, 100)
    if sorteia == 90 and habilitaNarizinho == False:
      habilitaNarizinho = True
    if habilitaNarizinho == True:
      display.blit(narizinhoImg, (narizinhoPosicaoX, narizinhoPosicaoY))
      narizinhoPosicaoY = narizinhoPosicaoY + velocidadeNarizinho

    if emiliaPosicaoY < narizinhoPosicaoY + narizinhoAltura and habilitaNarizinho == True:
      if emiliaPosicaoX < narizinhoPosicaoX and emiliaPosicaoX+emiliaLargura > narizinhoPosicaoX or narizinhoPosicaoX+narizinhoLargura > emiliaPosicaoX and narizinhoPosicaoX+narizinhoLargura < emiliaPosicaoX+emiliaLargura:
        contadorNarizinho = contadorNarizinho + 1
        habilitaNarizinho = False  
        narizinhoPosicaoY = -220   
    
    if sorteia == 90 and habilitaPedrinho == False:
      habilitaPedrinho = True
    if habilitaPedrinho == True:
      display.blit(pedrinhoImg, (pedrinhoPosicaoX, pedrinhoPosicaoY))
      pedrinhoPosicaoY = pedrinhoPosicaoY + velocidadePedrinho

    if emiliaPosicaoY < pedrinhoPosicaoY + pedrinhoAltura and habilitaPedrinho == True:
      if emiliaPosicaoX < pedrinhoPosicaoX and emiliaPosicaoX+emiliaLargura > pedrinhoPosicaoX or pedrinhoPosicaoX+pedrinhoLargura > emiliaPosicaoX and pedrinhoPosicaoX+pedrinhoLargura < emiliaPosicaoX+emiliaLargura:
        contadorPedrinho = contadorPedrinho + 1
        habilitaPedrinho = False  
        pedrinhoPosicaoY = -220    

    if sorteia == 90 and habilitaVisonde == False:
      habilitaVisonde = True
    if habilitaVisonde == True:
      display.blit(viscondeImg, (viscondePosicaoX, viscondePosicaoY))
      viscondePosicaoY = viscondePosicaoY + velocidadeVisconde

    if emiliaPosicaoY < viscondePosicaoY + viscondeAltura and habilitaVisonde == True:
      if emiliaPosicaoX < viscondePosicaoX and emiliaPosicaoX+emiliaLargura > viscondePosicaoX or viscondePosicaoX+viscondeLargura > emiliaPosicaoX and viscondePosicaoX+viscondeLargura < emiliaPosicaoX+emiliaLargura:
        contadorVisconde = contadorVisconde + 1
        habilitaVisonde = False  
        viscondePosicaoY = -220    

    if contadorNarizinho == 5 and contadorPedrinho == 8 and contadorVisconde == 2:
      acertos = contadorNarizinho + contadorPedrinho + contadorVisconde
      vitoria(acertos)

    pygame.display.update()
    time.tick(60)


inicio_jogo()