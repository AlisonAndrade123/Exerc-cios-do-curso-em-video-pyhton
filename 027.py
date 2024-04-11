#Faça um programa que leia o nome completo de uma pessoa. Mostrando em seguida o primeiro e o último nome separadamente.
#Ex:Ana Maria de Souza
#primeiro = Ana
#último = Souza

n = str(input('Digite seu nome completo ')).strip()
nome = n.split()
print('Muito prazer em te conhecer!')
print(f'Seu primeiro nome é {nome[0]}')
print(f'Seu último nome é {nome[- 1]}')