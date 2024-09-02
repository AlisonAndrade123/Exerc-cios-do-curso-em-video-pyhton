'''
dados = dict()
dados = {'nome':'Pedro', 'Idade':25}
print(dados['nome'])
print(dados['Idade'])
dados['sexo'] = 'M'
print(dados['sexo'])
del dados['Idade']
print(dados)
'''

'''
filme = {'titulo':'Star Wars', 'ano':1977, 'diretor':'George Lucas'}
print(filme.values())
print(filme.keys())
print(filme.items())
for k, v in filme.items():
    print(f'O {k} é {v}')
'''

'''
pessoas = {'nome': 'Gustavo', 'sexo': 'M', 'idade': 22}
#print(pessoas['nome'])
#print(f'O {pessoas["nome"]} tem {pessoas["idade"]} anos.')
#print(pessoas.keys())
#print(pessoas.values())
#print(pessoas.items())
#for k in pessoas.keys():
    #print(k)
#for k in pessoas.values():
    #print(k)
#del pessoas['sexo']
#pessoas['nome'] = 'Leandro'
pessoas['peso'] = 98.5
for k, v in pessoas.items():
    print(f'{k} = {v}')
'''
'''
brasil = []
estado1 = {'uf': 'Rio de janeiro', 'sigla': 'RJ'}
estado2 = {'uf': 'São Paulo', 'sigla': 'SP'}
brasil.append(estado1)
brasil.append(estado2)

print(brasil[0]['uf'])
'''

estado = dict()
brasil = list()
for c in range(0,3):
    estado['uf'] = str(input('Unidade Federativa: '))
    estado['sigla'] = str(input('Sigla do Estado: '))
    brasil.append(estado.copy())
print(brasil)
for e in brasil:
    for k, v in e.items():
        print(f'O campo {k} tem valor {v}')