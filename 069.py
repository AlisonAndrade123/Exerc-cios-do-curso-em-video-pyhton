#Crie um programa que leia a idade e o sexo de várias pessoas. A cada pessoa cadastrada, o programa deverá perguntar se o usuário quer ou não continuar. No final, mostre:
#A) Quantas pessoas tem mais de 18 anos.
#B) Quantos homens foram cadastrados.
#C) Quantas mulheres tem menos de 20 anos.

total_mais_18 = homem = mulher_menos_20 = 0
while True:
    print('-' * 30)
    print(f'{'CADASTRE UMA PESSOA': ^30}')
    print('-' * 30)
    idade = int(input('Informe a idade: '))
    if idade >= 18:
        total_mais_18 += 1
    sexo = input('Informe o sexo: [M/F]: ').strip().upper()[0]
    while sexo not in ['M', 'F']:
        sexo = input('Por favor, escolha entre masculino (M) ou feminino (F): ').strip().upper()[0]
    print('-' * 30)
    if sexo == 'M':
        homem += 1
    if sexo == 'F' and idade < 20:
        mulher_menos_20 += 1
    continua = str(input('Quer continuar? [S/N]: ')).strip().upper()[0]
    while continua not in ['S', 'N']:
        continua = input('Por favor, escolha entre sim (S) ou não (N): ').strip().upper()[0]
    if continua == 'N':
        break
print(f'Total de pessoas com  mais de 18 anos: {total_mais_18}')
print(f'Ao todo temos {homem} homens cadastrados')
print(f'E temos {mulher_menos_20} mulheres com menos de 20 anos')


