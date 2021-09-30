from random import randint
from time import sleep

def titulo(msg = str):
    n = len(msg) + 4
    print('='*n)
    print('  {}'.format(msg))
    print('='*n)

def mostrar(lista = []):
    print('=-'*15)
    for coluna in range (3):
        for linha in range(3):
            print(f'[{lista[coluna][linha]:^5}]', end='')
        print()

def checar_Velha(lista = [], contador = 0):
    '''
    lista: matriz/tabuleiro do jogo
    alive: boolean que continua o jogo
    contador: contador que, ao chegar em 9 (total de espacos usados) acaba o jogo'''
    contador = 0
    global jogo
    for linha in range(3):
        for coluna in range(3):
            if lista[linha][coluna] != '':
                contador +=1
    if contador == 9:
        print('DEU VELHA')
        jogo = False
    # print(contador)

# CRIA O TABULEIRO
tabuleiro = []
for i in range(3):
    tabuleiro.append([])
    for j in range(3):
        tabuleiro[i].append('')

# VARIAVEIS GLOBAIS
jogo = True
jogador_linha = jogador_coluna = 0

# LOOP DO JOGO
titulo('JOGO DA VELHA')
while jogo == True:
    mostrar(tabuleiro)
    checar_Velha(tabuleiro)
    print(jogo)

    #JOGADA DO JOGADOR
    jogador_linha = int(input('Linha da sua jogada: '))
    jogador_coluna = int(input('Coluna da jogada: '))

    #CHECAR SE A POSICAO ESCOLHIDA PELO JOGADOR ESTA VAZIA
    while tabuleiro[jogador_linha-1][jogador_coluna-1] != '':
        print('A posicao que voce escolheu ja esta tomada. Tente de novo')
        jogador_linha = int(input('Linha da sua jogada: '))
        jogador_coluna = int(input('Coluna da jogada: '))
    tabuleiro[jogador_linha-1][jogador_coluna-1] = 'X'

    mostrar(tabuleiro)
    checar_Velha(tabuleiro)
    print(jogo)
    sleep(1)

    #JOGADA DO CPU
    cpu_linha = randint(0,2)
    cpu_coluna = randint(0,2)

    # CHECAR SE A POSICAO ESCOLHIDA PELO CPU ESTA VAZIA
    while tabuleiro[cpu_linha][cpu_coluna] != '':
        cpu_linha = randint(0,2)
        cpu_coluna = randint(0,2)
    tabuleiro[cpu_linha][cpu_coluna] = 'O'

print('Acabou')

# IDEIA PARA AMANHA: PARA ACABAR O JOGO POSSO TENTAR FAZER UM FOR LOOP QUE CHECA CADA ESPACO NO TABULEIRO POR 'XO', SE SIM CONTADOR +=1
# ATE CHEGAR EM 9. ISSO SIGNIFICA "VELHA"

# APOS ISSO FAREI OS IF-STATMENTS QUE CHECAM SE HA UM VENCEDOR