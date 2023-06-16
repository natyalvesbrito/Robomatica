import pygame
pygame.init()
pygame.mixer.init()

#Carregar a música
pygame.mixer.music.load(r"sinnesloschen-beam-117362.mp3")

#Configuração da Janela
largura = 800
altura = 600
janela = pygame.display.set_mode((largura, altura))
pygame.display.set_caption("Robomática")

#Imagens
capi = pygame.image.load('capivara.png')
robo = pygame.image.load('robo.png')
floresta = pygame.image.load('floresta.png')
coracao = pygame.image.load('coracao.png')
coruja = pygame.image.load('coruja.png')
filhote = pygame.image.load('filhote.png')
harpia = pygame.image.load('harpia.png')
mico = pygame.image.load('micoleao.png')
onca = pygame.image.load('onca.png')
sagui = pygame.image.load('sagui.png')
torre = pygame.image.load('torre.png')
enter = pygame.image.load('enter.png')
menu = pygame.image.load('tela-inicial.png')
creditos = pygame.image.load('creditos.png')
lago = pygame.image.load('lago.png')
acai = pygame.image.load('acai.png')
teladificuldade = pygame.image.load('tela-dificuldade.png')

#Imagens Scale
alturaimg = 300
larguraimg = 300
robo = pygame.transform.scale(robo,(larguraimg,alturaimg))
capi = pygame.transform.scale(capi,(larguraimg,alturaimg))
coruja = pygame.transform.scale(coruja,(larguraimg,alturaimg))
filhote = pygame.transform.scale(filhote,(larguraimg,alturaimg))
harpia = pygame.transform.scale(harpia,(larguraimg+50,alturaimg+50))
mico = pygame.transform.scale(mico,(larguraimg,alturaimg))
onca = pygame.transform.scale(onca,(larguraimg,alturaimg))
sagui = pygame.transform.scale(sagui,(larguraimg,alturaimg))
torre = pygame.transform.scale(torre,(largura,altura))
floresta = pygame.transform.scale(floresta,(largura,altura))
coracao = pygame.transform.scale(coracao,(20,20))
enter = pygame.transform.scale(enter,(65,50))
menu = pygame.transform.scale(menu,(largura, altura))
creditos = pygame.transform.scale(creditos,(largura, altura))
lago = pygame.transform.scale(lago,(largura, altura))
acai = pygame.transform.scale(acai,(larguraimg,alturaimg))
teladificuldade = pygame.transform.scale(teladificuldade,(largura, altura))


#Cores
preto = (0, 0, 0)
branco = (255, 255, 255)
verde = (19, 214, 110)
verde_claro = (166, 247, 204)


#Fonte
tam_fonte = 25
fonte = pygame.font.Font(None, tam_fonte)
fonte_maior = pygame.font.Font(None, 30)

#Abrindo e salvando o arquivo História
with open('historia.txt', 'r', encoding='utf-8') as arquivo:
    linhas = arquivo.readlines()

#Texto Difícil
with open('historia-dificil.txt', 'r', encoding='utf-8') as arquivo:
    linhas2 = arquivo.readlines()
textodificil = [linha.strip() for linha in linhas2]
    
#Remover quebras de linha e espaços em branco extras
texto = [linha.strip() for linha in linhas]

#Texto Pygame
indice = 0
texto_atual_1 = fonte.render(texto[indice], True, (0, 0, 0))
texto_atual_2 = fonte.render('', True, (0, 0, 0))
texto_atual_3 = fonte.render('', True, (0, 0, 0))

texto_correto = fonte.render('Correto!', True, (0, 0, 0))
texto_errado = fonte.render('Não está correto!', True, (0, 0, 0))

# Definindo a posição do texto
texto_x = 65
texto_y = 435

# Entrada de resposta
entrada = ''
caixa_entrada = pygame.Rect(50, 150, 140, 45)

# Vida
vida = 7
x_coracao = 15
y_coracao = 20

#Funções:
#função background
def fundo(local = 'floresta'):
    if local == 'floresta':
        janela.blit(floresta,(0,0))
    elif local == 'torre':
        janela.blit(torre,(0,0))
    elif local == 'lago':
        janela.blit(lago,(0,0))

#Função verificar resposta
def verificar_resposta(resposta_correta):
    global entrada, indice, texto_atual_1, texto_atual_2, texto_atual_3, vida
    if not entrada or entrada == '':  # Verifica se a entrada está vazia
        texto_atual_1 = fonte.render('Não está correto', True, (0, 0, 0))
        texto_atual_2 = fonte.render('  ', True, (0, 0, 0))
        texto_atual_3 = fonte.render('  ', True, (0, 0, 0))
        vida -= 1
    elif entrada == resposta_correta:
        texto_atual_1 = fonte.render('Correto.', True, (0, 0, 0))
        texto_atual_2 = fonte.render('  ', True, (0, 0, 0))
        texto_atual_3 = fonte.render('  ', True, (0, 0, 0))
    else:
        texto_atual_1 = fonte.render('Não está correto.', True, (0, 0, 0))
        texto_atual_2 = fonte.render('  ', True, (0, 0, 0))
        texto_atual_3 = fonte.render('  ', True, (0, 0, 0))
        vida -= 1
    entrada = ''
#Função personagem na tela
ximg = 250
yimg = 80
def personagem(tela):
    if tela in [1,2,3,4,5,6,7,8,9,10,11,12,15,16,20,22,24,25,26,27,30,31,32,33,34,35,36,
                43,44,45,46,47,48,52,53,55, 56,57,59,60,63,64,65,69,70,71,72,75,77,82,89,
                90, 91]: 
        janela.blit(robo, (ximg, yimg))
    elif tela in [17,18,19]:
        janela.blit(coruja, (ximg, yimg))
    elif tela in [28,29,37,38,39,]:
        janela.blit(capi, (ximg, yimg))
    elif tela in [41,42]:
        janela.blit(mico, (ximg, yimg))
    elif tela in [50,51,54,61,62,]:
        janela.blit(harpia, (ximg-40, yimg-50))
    elif tela in [67,68,76,85,86,87]:
        janela.blit(filhote, (ximg, yimg))
    elif tela in [73,74,81,83,84,88]:
        janela.blit(sagui, (ximg, yimg))
    elif tela in [78,79,80]:
        janela.blit(onca, (ximg, yimg))
    elif tela == 92:
        janela.blit(acai, (ximg, yimg))

    
#Boss Fight
vidaboss = 7

#Tocando música
pygame.mixer.music.play(-1)



#Loop Menu
Menu = True
Dificuldade = False
janela.blit(menu, (0, 0))
while Menu:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            quit()
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE:
                janela.blit(teladificuldade,(0,0))
                Dificuldade = True
            if Dificuldade and (event.key == pygame.K_1):
                Menu = False
                dificil = False
            elif Dificuldade and (event.key == pygame.K_2):
                texto = textodificil
                dificil = True
                Menu = False 
    pygame.display.update()


#Loop Principal
resposta = False
fundo()
while True:
    Menu = False
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            quit()
        elif event.type == pygame.KEYDOWN and event.key == pygame.K_SPACE:
                fundo('floresta')
                if 49 <= indice <= 66:
                    fundo('torre')
                if 28 <= indice <= 48:
                    fundo('lago')
                # Atualiza o índice do texto
                indice += 1
                if indice >= len(texto):
                    janela.blit(creditos,(0,0))
                    pygame.display.update()
                    pygame.time.wait(10000)
                    pygame.quit()
                    quit()
                else:
                    # Atualiza o texto
                    if '$' in texto[indice]:
                        partes = texto[indice].split('$')
                        texto_atual_1 = partes[0]
                        texto_atual_2 = partes[1]
                        texto_atual_3 = partes[2] if len(partes) > 2 else ''
                        texto_atual_2 = fonte.render(texto_atual_2, True, (0, 0, 0))
                        texto_atual_3 = fonte.render(texto_atual_3, True, (0, 0, 0))
                    else:
                        texto_atual_1 = texto[indice]
                        texto_atual_2 = ''
                        texto_atual_3 = ''
                    texto_atual_1 = fonte.render(texto_atual_1, True, (0, 0, 0))

                    tela = indice
                    personagem(tela)

                    #Boss Fight
                    if indice == 75:
                        vidaboss = vida
                    if indice>76:
                        if vida == 0:
                            indice = 77
                            vida = vidaboss
                            texto_atual_1 = 'Perdeu todas as vidas... Vamos recomeçar!'
                            texto_atual_2 = ''
                            texto_atual_3 = ''
                            texto_atual_1 = fonte.render(texto_atual_1, True, (0, 0, 0))
                            texto_atual_2 = fonte.render(texto_atual_2, True, (0, 0, 0))
                            texto_atual_3 = fonte.render(texto_atual_3, True, (0, 0, 0))
                    if indice in [13,26,34,46,60,65,80,83,86]:
                        if not resposta:
                            vida -= 1
                    resposta = False
        elif event.type == pygame.KEYDOWN:
                if dificil == False:
                    if indice in [12,25,33,45,59,64,79,82,85] and resposta == False:
                        if (event.key == pygame.K_RETURN):
                            resposta = True
                            if indice == 12:
                                verificar_resposta('70')
                            if indice == 25:
                                verificar_resposta('21')
                            if indice == 33:
                                verificar_resposta('2000')
                            if indice == 45:
                                verificar_resposta('195')
                            if indice == 59:
                                verificar_resposta('307')
                            if indice == 64:
                                verificar_resposta('50')
                            if indice == 79:
                                verificar_resposta('13')
                            if indice == 82:
                                verificar_resposta('4')
                            if indice == 85:
                                verificar_resposta('3')
                else:
                    if indice in [12,25,33,45,59,64,79,82,85] and resposta == False:
                        if (event.key == pygame.K_RETURN):
                            resposta = True
                            if indice == 12:
                                verificar_resposta('287')
                            if indice == 25:
                                verificar_resposta('91')
                            if indice == 33:
                                verificar_resposta('2204')
                            if indice == 45:
                                verificar_resposta('213')
                            if indice == 59:
                                verificar_resposta('372')
                            if indice == 64:
                                verificar_resposta('71')
                            if indice == 79:
                                verificar_resposta('30')
                            if indice == 82:
                                verificar_resposta('13')
                            if indice == 85:
                                verificar_resposta('6')
                if event.key == pygame.K_BACKSPACE:
                    entrada = entrada[:-1]
                else:
                    if event.key != pygame.K_RETURN and event.key != pygame.K_BACKSPACE:
                        entrada += event.unicode

    #Retângulo do texto
    rect_texto = pygame.draw.rect(janela, 'white', (50, 400, 700, 150))

    # Desenhando o texto na janela
    janela.blit(texto_atual_1, (texto_x, texto_y)) 
    if not texto_atual_2:
        pass
    else:
        janela.blit(texto_atual_2, (texto_x - 5, texto_y+30))
    if not texto_atual_3:
        pass
    else:
        janela.blit(texto_atual_3, (texto_x - 5, texto_y+60))

    #Escondendo a segunda linha
    if indice == 0:
        rect = pygame.draw.rect(janela, 'white', (50, 470, 700, 50))

    # Entrada de texto
    if indice in [12,25,33,45,59,64,79,82,85]:
        pygame.draw.rect(janela, branco, caixa_entrada)
        texto_entrada = fonte_maior.render(entrada, True, preto)
        janela.blit(texto_entrada, (caixa_entrada.x + 5, caixa_entrada.y + 5))
        janela.blit(enter, (caixa_entrada.x+caixa_entrada.width,caixa_entrada.y))
    
    if vida >= 1:
        janela.blit(coracao, (x_coracao, y_coracao))
        if vida >= 2:
            janela.blit(coracao, (45, y_coracao))
            if vida >=3:
                janela.blit(coracao, (75, y_coracao))
                if vida >= 4:
                    janela.blit(coracao, (105, y_coracao))
                    if vida >= 5:
                        janela.blit(coracao, (135, y_coracao))
                        if vida >= 6:
                            janela.blit(coracao, (165, y_coracao))
                            if vida == 7:
                                janela.blit(coracao, (195, y_coracao))

    pygame.display.update()