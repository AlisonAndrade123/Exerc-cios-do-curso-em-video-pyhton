#Crie um programa que leia uma frase qualquer e diga se ela é um palindromo, desconsiderando os espaços.
#Ex
#APOS A SOPA
#A SACADA DA CASA 
#A TORRE DA DERROTA
#ANOTARAM A DATA DA MARATONA

'''
frase = str(input('Digite uma frase ')).strip().upper() #Nesta linha, o programa solicita ao usuário que digite uma frase e armazena essa frase na variável frase. O método strip() remove espaços em branco extras no início e no final da entrada, enquanto upper() converte a frase para letras maiúsculas. Isso garante que não haja discrepâncias na comparação de letras maiúsculas e minúsculas posteriormente.
palavras = frase.split()#Essa linha divide a frase em uma lista de palavras usando o método split(). Por padrão, o método split() divide a string em palavras separadas por espaços em branco.
junto = ''.join(palavras)#Aqui, todas as palavras são unidas em uma única string novamente, sem espaços entre elas. Isso é feito usando o método join() com uma string vazia como separador.
inverso = ''#Inicializa a variável inverso como uma string vazia. Essa variável será usada para armazenar a versão invertida da frase.
for letra in range(len(junto)-1, -1, -1):
    inverso += junto[letra]
#Este bloco de código itera sobre cada letra da string junto de trás para frente, construindo a string inverso, que é a frase ao contrário.
if inverso == junto:
    print('Temos um palíndromo!')
else:
    print('A frase digitada não é um palíndromo')
#Aqui, o programa verifica se a string inverso é igual à string junto. Se forem iguais, significa que a frase é um palíndromo e imprime a mensagem correspondente. Caso contrário, imprime que a frase não é um palíndromo.
'''


frase = str(input('Digite uma frase ')).strip().upper()
palavras = frase.split()
junto = ''.join(palavras)
inverso = ''
for letra in range(len(junto)-1, -1, -1):
    inverso += junto[letra]
print(f'O inverso de {junto} é {inverso}')
if inverso == junto:
    print('Temos um palíndromo!')
else:
    print('A frase digitada não é um palíndromo')