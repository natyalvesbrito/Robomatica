import pygame
pygame.init()

#Configuração da Janela
largura = 800
altura = 600
janela = pygame.display.set_mode((largura, altura))
pygame.display.set_caption("Robomática")

#Imagens
capi = pygame.image.load('capivara.png')
robo = pygame.image.load('robo.png')
robo = pygame.transform.scale(robo,(largura/3,altura/2.3))
floresta = pygame.image.load('floresta.png')
floresta = pygame.transform.scale(floresta,(largura,altura))
coracao = pygame.image.load('coracao.png')
coracao = pygame.transform.scale(coracao,(20,20))

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
    
#Remover quebras de linha e espaços em branco extras
texto = [linha.strip() for linha in linhas]

#Texto Pygame
indice = 0
texto_atual_1 = fonte.render(texto[indice], True, (0, 0, 0))
texto_atual_2 = fonte.render(texto[indice], True, (0, 0, 0))

texto_correto = fonte.render('Correto!', True, (0, 0, 0))
texto_errado = fonte.render('Não está correto!', True, (0, 0, 0))

# Definindo a posição do texto
texto_x = 65
texto_y = 450

# Entrada de resposta
entrada = ''
caixa_entrada = pygame.Rect(100, 100, 140, 32)

# Vida
vida = 7
x_coracao = 15
y_coracao = 20

#Funções:
#função background
def fundo(local):
    if local == 'floresta':
        janela.blit(floresta,(0,0))
    '''elif local == 'torre':
        janela.blit()
    elif local == 'lago':
        janela.blit()
    elif local == 'boss':
        janela.blit()'''
#Função verificar resposta
def verificar_resposta(resposta_correta):
    global entrada, indice, texto_atual_1, texto_atual_2, vida
    if not entrada:  # Verifica se a entrada está vazia
        texto_atual_1 = fonte.render('Errado', True, (0, 0, 0))
        texto_atual_2 = fonte.render('  ', True, (0, 0, 0))
        vida -= 1
    if entrada == resposta_correta:
        texto_atual_1 = fonte.render('Correto', True, (0, 0, 0))
        texto_atual_2 = fonte.render('  ', True, (0, 0, 0))
    else:
        texto_atual_1 = fonte.render('Errado', True, (0, 0, 0))
        texto_atual_2 = fonte.render('  ', True, (0, 0, 0))
        vida -= 1
    entrada = ""
    

esperando_resposta = False
#Loop Principal
fundo('floresta')
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            quit()
        elif event.type == pygame.KEYDOWN and event.key == pygame.K_SPACE:
                fundo('floresta')
                # Atualiza o índice do texto
                indice += 1
                if indice >= len(texto):
                    pygame.quit()
                    #créditos finais print
                    quit()
                else:
                    # Atualiza o texto
                    if '$' in texto[indice]:
                        texto_atual_1, texto_atual_2 = texto[indice].split('$')
                        texto_atual_2 = fonte.render(texto_atual_2, True, (0, 0, 0))
                    else:
                        texto_atual_1 = texto[indice]
                        texto_atual_2 = ''
                    texto_atual_1 = fonte.render(texto_atual_1, True, (0, 0, 0))

                    #Janelas do robô sozinho
                    if indice in [3,4,5,6,7,8,9]:
                        janela.blit(robo, (260, 100))
                    #Janelas da coruja sozinha
                    #Janelas do mico-leão sozinho
                    #Janelas da harpia sozinha
                    #Janelas da onça filhote sozinho
                    #Janelas da onça mãe sozinha
                    #Janelas da gangue de saguis sozinho
                    #Janelas com mais de 2 personagens
        elif event.type == pygame.KEYDOWN:
            if indice in [12,24]:
                if event.key == pygame.K_RETURN:
                    if indice == 12:
                        verificar_resposta('70')
                    if indice == 24:
                        verificar_resposta('21')
                elif event.key == pygame.K_BACKSPACE:
                    entrada = entrada[:-1]
                else:
                    entrada += event.unicode

    #Retângulo do texto
    rect_texto = pygame.draw.rect(janela, 'white', (50, 400, 700, 150))

    # Desenhando o texto na janela
    janela.blit(texto_atual_1, (texto_x, texto_y)) 
    if not texto_atual_2:
        pass
    else:
        janela.blit(texto_atual_2, (texto_x - 5, texto_y+30))

    #Escondendo a segunda linha
    if indice == 0:
        rect = pygame.draw.rect(janela, 'white', (50, 470, 700, 50))

    # Entrada de texto
    if indice in [12,24]:
        pygame.draw.rect(janela, branco, caixa_entrada)
        texto_entrada = fonte.render(entrada, True, preto)
        janela.blit(texto_entrada, (caixa_entrada.x + 5, caixa_entrada.y + 5))
    
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
