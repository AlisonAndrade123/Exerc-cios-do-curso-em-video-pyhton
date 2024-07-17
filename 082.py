#Crie um programa que vai ler vários números e colocar em uma lista. Depois disso, crie duas listas extras que vão conter apenas os valores pares e os valores ímpares digitados, respectivamente. Ao final, mostre o conteúdo das três listas geradas.

lista = []
listapar = []
listaimpar = []
while True:
    lista.append(int(input('Digite um valor: ')))
    r = str(input('Quer continuar? [S/N]'))
    if r in 'Nn':
        break
for numero in lista:
    if numero % 2 == 0:
        listapar.append(numero)
    else:
        listaimpar.append(numero)
print('-=' * 30)
print(f'A lista completa é {lista}')
print(f"A lista de pares é {listapar}")
print(f"A lista de ímpares é {listaimpar}")