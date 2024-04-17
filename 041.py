#A confederação nacional de natação precisa de um programa que leia o ano de nascimento de um atleta e mostra sua categoria. de acordo com a idade:
#Até 9 anos: MIRIM
#Até 14 anos: INFANTIL
#Até 19 anos: JUNIOR
#Até 25 anos: SÊNIOR
#Acima: MASTER

from datetime import date
atual = date.today().year
anon = int(input('Ano de nascimento: '))

idade = atual - anon

print(f'O atleta tem {idade} anos.')

if idade <= 9:
    print('Classificação: MIRIM')
elif 9 < idade <= 14:
    print('Classificação: INFANTIL')
elif 14 < idade <= 19:
    print('Classificação: JUNIOR')
elif 19 < idade <= 25:
    print('Classificação: SÊNIOR')
else:
    print('Classificação: MASTER')