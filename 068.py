#Faça um programa que joque par ou ímpar com o computador. O jogo só será interrompido quando o jogador PERDER, mostrando o total de vitórias consecutivas que ele conquistou no final do jogo.

from random import randint
v = 0
while True:
    jogador = int(input('Escolha um número entre 0 e 10: '))
    tipo = input('Par ou Ímpar? [P/I]: ').strip().upper()[0]
    while tipo not in ['P', 'I']:
        tipo = input('Por favor, escolha entre Par (P) ou Ímpar (I): ').strip().upper()[0]
    computador = randint(0, 10)
    total = jogador + computador
    print(f'Você jogou {jogador} e o computador {computador}. Total de {total}.')
    if tipo == 'P':
        if total % 2 == 0:
            print('Você VENCEU!')
            v += 1
        else:
            print('Você PERDEU!')
            break
    elif tipo == 'I':
        if total % 2 == 1:
            print('Você VENCEU!')
            v += 1
        else:
            print('Você PERDEU!')
            break
    print('Vamos jogar novamente...')
print(f'GAME OVER! Você venceu {v} vezes.')