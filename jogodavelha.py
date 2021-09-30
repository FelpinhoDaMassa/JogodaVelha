from random import randint

def titulo(msg = str):
    n = len(msg) + 4
    print('='*n)
    print('  {}'.format(msg))
    print('='*n)

def mostrar(lista = []):
    print('=-'*15)
    for coluna in range (0, 3):
        for linha in range(0, 3):
            print(f'[{lista[coluna][linha]:^5}]', end='')
        print()


jogo = True
contador = 1
jogador_linha = jogador_coluna = 0

# CRIA O TABULEIRO
tabuleiro = []
for i in range(3):
    tabuleiro.append([])
    for j in range(3):
        tabuleiro[i].append('')


titulo('JOGO DA VELHA')
while jogo == True:
    if contador == 1:
        mostrar(tabuleiro)

    #JOGADA DO JOGADOR
    jogador_linha = int(input('Linha da sua jogada: '))
    jogador_coluna = int(input('Coluna da jogada: '))

    #CHECAR SE A POSICAO ESCOLHIDA PELO JOGADOR ESTA VAZIA
    while tabuleiro[jogador_linha-1][jogador_coluna-1] != '':
        print('A posicao que voce escolheu ja esta tomada. Tente de novo')
        jogador_linha = int(input('Linha da sua jogada: '))
        jogador_coluna = int(input('Coluna da jogada: '))
    tabuleiro[jogador_linha-1][jogador_coluna-1] = 'X'
    
    #JOGADA DO CPU
    #tabuleiro[cpu_linha][cpu_coluna] = 'O'
    cpu_linha = randint(0,2)
    cpu_coluna = randint(0,2)

    # CHECAR SE A POSICAO ESCOLHIDA PELO CPU ESTA VAZIA
    while tabuleiro[cpu_linha][cpu_coluna] != '':
        cpu_linha = randint(0,2)
        cpu_coluna = randint(0,2)
    tabuleiro[cpu_linha][cpu_coluna] = 'O'
    
    mostrar(tabuleiro)

print('Acabou')

# IDEIA PARA AMANHA: PARA ACABAR O JOGO POSSO TENTAR FAZER UM FOR LOOP QUE CHECA CADA ESPACO NO TABULEIRO POR 'XO', SE SIM CONTADOR +=1
# ATE CHEGAR EM 9. ISSO SIGNIFICA "VELHA"

# APOS ISSO FAREI OS IF-STATMENTS QUE CHECAM SE HA UM VENCEDOR