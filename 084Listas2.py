'''
teste = list()
teste.append('Gustavo')
teste.append(40)
print(teste)

galera = list()
galera.append(teste[:])
teste[0] = 'Maria'
teste[1] = 22
galera.append(teste[:])
print(teste)
print(galera)
'''

'''
galera = [['João', 19],['Ana', 33],['Joaquim', 13],['Maria', 45]]
#print(galera)
#print(galera[0])
#print(galera[0][0])
for p in galera:
    #print(p)
    print(f'{p[0]} tem {p[1]} anos de idade.')
'''

galera = list()
dado = list()
totmai = totme = 0
for c in range(0, 3):
    dado.append(str(input('Nome: ')))
    dado.append(int(input('Idade:')))
    galera.append(dado[:])
    dado.clear()

#print(galera)

for p in galera:
    if p[1] >= 21:
        print(f'{p[0]} é maior de idade.')
        totmai += 1
    else:
        print(f'{p[0]} é menor de idade.')
        totme += 1
print(f'Temos {totmai} maiores e {totme} menores de idade.')