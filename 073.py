#Crie uma tupla preenchida com os 20 primeiros colocados da tabela do Campeonato Brasileiro de Futebol, na ordem de colocação. Depois mostre:
#A) Os 5 primeiros
#B) Os últimos 4 colocados.
#C) Times em ordem alfabética.
#D) Em que posição está o time da Chapecoense.

times_brasileirao_2023 = ("Palmeiras", "Grêmio", "Atlético-MG", "Flamengo", "Botafogo", "RB Bragantino", "Fluminense", "Athletico-PR", "Internacional", "Fortaleza", "São Paulo", "Cuiabá", "Corinthians", "Cruzeiro", "Vasco", "Bahia", "Santos", "Goiás", "Coritiba", "América-MG"
)
print('-='* 15)
print(f'Lista de times do Brasileirão:{times_brasileirao_2023}')
print('-='* 15)
print(f'Os 5 primeiros são{times_brasileirao_2023[0:5]}')
print('-='* 15)
print(f'Os 4 últimos são: {times_brasileirao_2023[-4:]}')
print('-='* 15)
ordenado = sorted(times_brasileirao_2023)
print(f'Times em ordem alfabética:{ordenado}')
print(f'O Athletico-PR está na {times_brasileirao_2023.index('Athletico-PR')+1}° posição')

