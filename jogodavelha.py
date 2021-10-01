from random import randint
from time import sleep

def titulo(msg = str):
    n = len(msg) + 4
    print('='*n)
    print('  {}'.format(msg))
    print('='*n)

def mostrar(lista = []):
    print('=-'*15)
    print('   1       2      3')
    for coluna in range (3):
        print(f'{coluna + 1}',end='')
        for linha in range(3):
            print(f'[{lista[coluna][linha]:^5}]', end='')
        print()

def checar_Velha(lista = [], contador = 0):
    '''
    lista: matriz/tabuleiro do jogo
    alive: boolean que continua o jogo
    contador: contador que, ao chegar em 9 (total de espacos usados) acaba o jogo'''
    contador = 0
    global jogo_rodando
    for linha in range(3):
        for coluna in range(3):
            if lista[linha][coluna] != '':
                contador +=1
    if contador == 9:
        print('DEU VELHA')
        jogo_rodando = False

def checar_Vencedor(lista = []):
    global jogo_rodando
    jogador_venceu = False
    cpu_venceu = False
    for linha in range(3):
        for coluna in range(3):
            if lista[linha][0] == 'X' and lista[linha][1] == 'X' and lista[linha][2] == 'X':
                jogador_venceu = True
            elif lista[0][coluna] == 'X' and lista[1][coluna] == 'X' and lista[2][coluna] == 'X':
                jogador_venceu = True
            elif lista[linha][0] == 'O' and lista[linha][1] == 'O' and lista[linha][2] == 'O':
                cpu_venceu = True
            elif lista[0][coluna] == 'O' and lista[1][coluna] == 'O' and lista[2][coluna] == 'O':
                cpu_venceu = True

    if jogador_venceu == True:
        print('Jogador Vence!')
        jogo_rodando = False
    elif cpu_venceu == True:
        print('CPU venceu!')
        print('Voce perdeu :(')
        jogo_rodando = False

# CRIA O TABULEIRO
tabuleiro = []
for i in range(3):
    tabuleiro.append([])
    for j in range(3):
        tabuleiro[i].append('')

# VARIAVEIS GLOBAIS
jogo_rodando = True
jogador_linha = jogador_coluna = 0

# LOOP DO JOGO
titulo('JOGO DA VELHA')
while True:
    while jogo_rodando:
        mostrar(tabuleiro)
        checar_Vencedor(tabuleiro)
        if jogo_rodando == False:
            break
        checar_Velha(tabuleiro)
        #NAO SEI FAZER O JOGO ACABAR SEM ESSA DESGRACA
        if jogo_rodando == False:
            break

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
        checar_Vencedor(tabuleiro)
        if jogo_rodando == False:
            break
        checar_Velha(tabuleiro)
        #NAO SEI FAZER O JOGO ACABAR SEM ESSA DESGRACA
        if jogo_rodando == False:
            break
        sleep(1)

        #JOGADA DO CPU
        cpu_linha = randint(0,2)
        cpu_coluna = randint(0,2)

        # CHECAR SE A POSICAO ESCOLHIDA PELO CPU ESTA VAZIA
        while tabuleiro[cpu_linha][cpu_coluna] != '':
            cpu_linha = randint(0,2)
            cpu_coluna = randint(0,2)
        tabuleiro[cpu_linha][cpu_coluna] = 'O'

    resp = str(input('Jogar novamente? [S/N]: ')).upper()
    while resp not in 'SN':
        resp = str(input('Por favor, responda com [S/N]: ')).upper()
    if resp in 'N':
        break
    # else:
    #     tabuleiro.clear

print('Tenha um bom dia :)')

# TO DO: IF-STATMENTS QUE CHECAM SE HA UM VENCEDOR