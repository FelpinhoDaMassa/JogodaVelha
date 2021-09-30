from random import randint

def titulo(msg = str):
    n = len(msg) + 4
    print('='*n)
    print('  {}'.format(msg))
    print('='*n)
contador = 0

cpu_linha = randint(0,2)
cpu_coluna = randint(0,2)

# CRIA O TABULEIRO
tabuleiro = []
for i in range(3):
    tabuleiro.append([])
    for j in range(3):
        tabuleiro[i].append('')
print(len(tabuleiro[0]) + len(tabuleiro[1]) + len(tabuleiro[2]))

# titulo('JOGO DA VELHA')
# while True:
#     tabuleiro[cpu_coluna][cpu_linha] = 'O'
#     while tabuleiro[cpu_coluna][cpu_linha] != '':
#         cpu_coluna = randint(0,2)
#         cpu_linha = randint(0,2)
#         tabuleiro[cpu_coluna][cpu_linha] = 'O'
    
#     # PRINTA O TABULEIRO FORMATADO
#     print('=-'*15)
#     for coluna in range (0, 3):
#         for linha in range(0, 3):
#             print(f'[{tabuleiro[coluna][linha]:^5}]', end='')
#         print()
            