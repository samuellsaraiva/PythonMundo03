'''Aula 19 Mundo 03 // Dicionários'''


''' Desafio 90
- Faça um programa que leia nome e média de um aluno, guardando também a situação em um dicionário.
No final, mostre o conteúdo da estrutura na tela.
'''
# aluno = {}
# aluno['Nome'] = input('Nome: ')
# aluno['Media'] = float(input('Média: '))
# if aluno['Media'] > 5:
#     aluno['Situação'] = 'APROVADO'
# else:
#     aluno['Situação'] = 'REPROVADO'
# for k, v in aluno.items():
#     print(f'{k} é igual a {v}.')



''' Desafio 91
- Crie um programa onde 4 jogadores joguem um dado e tenham resultados aleatórios. Guarde esses
resultados em um dicionário. No final, coloque esse dicionário em ordem, sabendo que o vencedor
tirou o maior número no dado.
'''
# from random import randint
# from time import sleep
# from operator import itemgetter
# print('Valores sorteados:')
# sleep(0.8)
# jogadores = {'Jogador 01': randint(1, 6),
#              'Jogador 02': randint(1, 6),
#              'Jogador 03': randint(1, 6),
#              'Jogador 04': randint(1, 6)
#              }
# ranking = {}
# for k, v in jogadores.items():
#     print(f'{k} tirou {v} no dado.')
#     sleep(0.8)
# ranking = sorted(jogadores.items(), key=itemgetter(1), reverse=True)
# print()
# print('=== RANKING DOS JOGADORES ===')
# print(ranking)
# for x in range(0, len(ranking)):
#     if x == 0:
#         print(f'{contador}° Lugar: {ranking[x][0]} com {ranking[x][1]}.')
#     elif ranking[x][1] == ranking[x - 1][1]:
#         print(f'{contador}° Lugar: {ranking[x][0]} com {ranking[x][1]}.')
#     else:
#         contador += 1
#         print(f'{contador}° Lugar: {ranking[x][0]} com {ranking[x][1]}.')
#     sleep(0.8)



''' Desafio 92
- Crie um programa que leia nome, ano de nascimento e carteira de trabalho e cadastre-os 
(com idade) em um dicionário, se por acaso a CTPS for diferente de ZERO, o dicionário receberá
também o ano de contratação e o salário. Calcule e acrescente, além da idade, com quantos anos
a pessoa vai se aposentar.
'''
# from datetime import date
# trabalhador = {}
# trabalhador['Nome'] = input('Nome: ')
# ano = int(input('Ano de Nascimento: '))
# trabalhador['Idade'] = date.today().year - ano
# trabalhador['CTPS'] = int(input('Carteira de Trabalho (0 se não tiver): '))
# if trabalhador['CTPS'] != 0:
#     trabalhador['Contratação'] = int(input('Ano de Contratação: '))
#     trabalhador['Salario'] = float(input('Salário: R$ '))
#     trabalhador['Aposentadoria'] = (trabalhador['Contratação'] - ano) + 35
# print('-=-' * 30)
# for k, v in trabalhador.items():
#     print(f'- {k} tem o valor {v}.')



''' Desafio 93
- Crie um programa que gerencie o aproveitamento de um jogador de futebol. O programa vai ler o 
nome do jogador e quantas partidas ele jogou. Depois vai ler a quantidade de gols feitos em cada
partida. No final, tudo isso será guardado em um dicionário, incluindo o total de gols feitos
durante o campeonato.
'''
# jogador = {}
# jogador['Nome'] = input('Nome do Jogador: ')
# partidas = int(input(f'Quantas partidas {jogador["Nome"]} jogou: '))
# gols = []
# for c in range(partidas):
#     gol = int(input(f'Quantas gols na partida {c + 1}: '))
#     gols.append(gol)
# jogador['Gols'] = gols
# jogador['Total'] = sum(gols)
# print('-=-' * 18)
# print(jogador)
# print('-=-' * 18)
# for k, v in jogador.items():
#     print(f'O campo {k} tem o valor {v}.')
# print('-=-' * 18)
# print(f'O jogador {jogador["Nome"]} jogou {partidas} partidas.')
# for i, c in enumerate(jogador['Gols']):
#     print(f'=> Na partida {i + 1}, fez {c} gols.')
# print(f'Foi um total de {jogador["Total"]} gols.')



''' Desafio 94
- Crie um programa que leia nome, sexo e idade de várias pessoas, guardando os dados de cada
pessoa em um dicionário e todos os dicionários em uma lista. No final, mostre:
1) Quantas pessoas foram cadastradas; 2) A média de idade do grupo; 3) Uma lista com todas as
mulheres; 4) Uma lista com todas as pessoas com idade acima da média.
'''
# pessoas = []
# pessoa = {}
# while True:
#     pessoa['Nome'] = input('Nome: ')
#     pessoa['Sexo'] = input('Sexo: [M/F] ').strip().upper()[0]
#     while pessoa['Sexo'] not in 'MF':
#         print('ERRO! Por favor digite apenas M ou F.')
#         pessoa['Sexo'] = input('Sexo: [M/F] ').strip().upper()[0]
#     pessoa['Idade'] = int(input('Idade: '))
#     pessoas.append(pessoa.copy())
#     pessoa.clear()
#     resp = input('Quer continuar? [S/N] ').strip().upper()[0]
#     while resp not in 'SN':
#         print('ERRO! Por favor digite apenas S ou N.')
#         resp = input('Quer continuar? [S/N] ').strip().upper()[0]
#     if resp == 'N':
#         break
# idades = []
# for i, c in enumerate(pessoas):
#     idades.append(pessoas[i]['Idade'])
# media = sum(idades) / len(pessoas)
# print('-=-' * 18)
# print(f'A) Ao todo temos {len(pessoas)} pessoas cadastradas.')
# print(f'B) A média de idade é de {media:.2f} anos.')
# print(f'C) As mulheres cadastradas foram:', end=' ')
# for x in pessoas:
#     if x['Sexo'] == 'F':
#         print(x['Nome'], end='; ')
# print('\nD) Lista das pessoas que tem idade acima da média:')
# for x in pessoas:
#     if x['Idade'] > media:
#         print('   ', end='')
#         for k, v in x.items():
#             print(f'{k} = {v}; ',end='')
#         print()
# print('-=-' * 18)
# print('<<< ENCERRADO >>>')



''' Desafio 95
- Aprimore o DESAFIO 093 para que ele funcione com vários jogadores, incluindo um sistema de
visualização de detalhes do aproveitamento de cada jogador.
'''
# jogador = {}
# jogadores = []
# while True:
#     jogador['Nome'] = input('Nome do Jogador: ')
#     partidas = int(input(f'Quantas partidas {jogador["Nome"]} jogou: '))
#     gols = []
#     for c in range(partidas):
#         gol = int(input(f'Quantas gols na partida {c + 1}: '))
#         gols.append(gol)
#     jogador['Gols'] = gols
#     jogador['Total'] = sum(gols)
#     jogadores.append(jogador.copy())
#     resp = input('Quer continuar? [S/N] ').strip().upper()[0]
#     while resp not in 'SN':
#         resp = input('Quer continuar? [S/N] ').strip().upper()[0]
#     if resp == 'N':
#         break
# print('-=-' * 16)
# print(f'{"Cód.":<11}{"Nome":<15}{"Gols":<15}{"Total":<15}')
# print('-' *48)
# for k, v in enumerate(jogadores):
#     print(f'{k:<11}', end='')
#     for d in v.values():
#         print(f'{str(d):<15}', end='')
#     print()
# print('-' *48)
# while True:
#     busca = int(input('Mostrar dados de qual jogador? (999 para parar) '))
#     for k, v in enumerate(jogadores):
#         if busca == k:
#             print(f'LEVANTAMENTO DO JOGADOR: {v["Nome"]}')
#             jogo = 1
#             for d in v['Gols']:
#                 print(f'No jogo {jogo} fez {d} gols.')
#                 jogo += 1
#             print('-' * 48)
#     if busca == 999:
#         break
# print('-' *48)
# print('<<< TERMINADO >>>')