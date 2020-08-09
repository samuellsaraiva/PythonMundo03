'''Aula 18 Mundo 03 // Listas Parte 02'''


''' Desafio 84
- Faça um programa que leia nome e peso de várias pessoas, guardando tudo em uma lista. No final,
mostre: 1) Quantas pessoas foram cadastradas; 2) Uma listagem com as pessoas mais pesadas; 3) Uma
listagem com as pessoas mais leves.
'''
# pessoas = []
# dados = []
# pesos = []
# maior = menor = qttde = 0
# while True:
#     nome = input('Nome: ')
#     peso = float(input('Peso: '))
#     dados.append(nome)
#     dados.append(peso)
#     pesos.append(peso)
#     pessoas.append(dados[:])
#     dados.clear()
#     qttde += 1
#     resp = input('Quer continuar: [S/N] ').strip().upper()[0]
#     while resp not in 'SN':
#         resp = input('Quer continuar: [S/N] ').strip().upper()[0]
#     if resp == 'N':
#         break
# print('-=-' * 15)
# print(f'Ao todo, você cadastrou {qttde} pessoas.')
# maxpesos = []
# minpesos = []
# for p in pessoas:
#     if p[1] == max(pesos):
#         maxpesos.append(p[0])
#     if p[1] == min(pesos):
#         minpesos.append(p[0])
# print(f'O maior peso foi de {max(pesos)}.Pesos de de {maxpesos}')
# print(f'O menor peso foi de {min(pesos)}.Pesos de de {minpesos}')



''' Desafio 85
- Crie um programa onde o usuário possa digitar sete valores numéricos e cadastre-os em uma lista
única que mantenha separados os valores pares e ímpares. No final, mostre os valores pares e
ímpares em ordem crescente.
'''
# numeros = [[], []]
# for c in range(7):
#     num = int(input(f'Digite o {c + 1}° valor: '))
#     if num % 2 == 0:
#         numeros[0].append(num)
#     else:
#         numeros[1].append(num)
# print('-=-' * 20)
# print(f'Os valores pares digitados foram: {sorted(numeros[0])}')
# print(f'Os valores ímpares digitados foram: {sorted(numeros[1])}')



''' Desafio 86
- Crie um programa que crie uma matriz de dimensão 3x3 e preencha com valores lidos pelo teclado.
No final, mostre a matriz na tela, com a formatação correta.
'''
# matriz = [[0, 0, 0], [0, 0, 0], [0, 0, 0]]
# for l in range(3):
#     for c in range(3):
#         matriz[l][c] = int(input(f'Digite um valor para [{l}, {c}]: '))
# print('-=-' * 15)
# for l in range(3):
#     for c in range(3):
#         print(f'[{matriz[l][c]}]', end='')
#     print()




''' Desafio 87
- Aprimore o desafio anterior, mostrando no final:
A) A soma de todos os valroes pares digitados;
B) A soma dos valores da terceira coluna;
C) O maior valor da segunda linha.
'''
# matriz = [[0, 0, 0], [0, 0, 0], [0, 0, 0]]
# pares = 0
# sumcoluna = 0
# for l in range(3):
#     for c in range(3):
#         matriz[l][c] = int(input(f'Digite um valor para [{l}, {c}]: '))
#         if matriz[l][c] % 2 == 0:
#             pares += matriz[l][c]
#         if c == 2:
#             sumcoluna += matriz[l][2]
# print('-=-' * 11)
# for l in range(3):
#     for c in range(3):
#         print(f'[{matriz[l][c]}]', end='')
#     print()
# print('-=-' * 11)
# print(f'A soma dos valores pares é de {pares}.')
# print(f'A soma dos valores da terceira coluna é {sumcoluna}.')
# print(f'O maior valor da segunda linha é {max(matriz[1])}.')



''' Desafio 88
- Faça um programa que ajude um jogador da MEGA SENA a criar palpites. O programa vai perguntar
quantos jogos serão gerados e vai sortear 6 números entre 1 e 60 para cada jogo, cadastrando tudo
em uma lista composta.
'''
# from random import randint
# print('-' * 40)
# print(f'{"JOGOS PARA MEGASENA":^40}')
# print('-' * 40)
# jogos = []
# auxiliar = []
# index = cont =  0
# qtdde = int(input('Quantos jogos  você quer que eu sorteie? '))
# print('-=-' * 3, end=' ')
# print(f'SORTEANDO {qtdde} JOGOS', end=' ')
# print('-=-' * 3)
# for c in range(qtdde):
#     cont = 0
#     print(f'JOGO {index + 1:<3}: ', end='')
#     while True:
#         num = randint(1, 61)
#         if num not in auxiliar:
#             auxiliar.append(randint(1, 60))
#             cont += 1
#         if cont == 6:
#             break
#     jogos = auxiliar
#     jogos.sort()
#     auxiliar = []
#     index += 1
#     print(jogos)



''' Desafio 89
- Crie um programa que leia nome e duas notas de vários alunos e guarde tudo em uma lista composta.
No final, mostre um boletim contendo a média de cada um e permita que o usuário possa mostrar as
notas de cada dado individualmente.
'''
# auxilio = []
# notas = []
# medias = []
# while True:
#     nome = input('Nome: ')
#     n1 = float(input('Nota 1: '))
#     n2 = float(input('Nota 2: '))
#     auxilio.append(nome)
#     auxilio.append(n1)
#     auxilio.append(n2)
#     notas.append(auxilio[:])
#     auxilio.clear()
#     resp = input('Deseja continuar? [S/N] ').strip().upper()[0]
#     if resp not in 'SN':
#         resp = input('Deseja continuar? [S/N] ').strip().upper()[0]
#     if resp == 'N':
#         break
# print('-=-' * 12)
# print(f'{"N°":<5}{"NOME":^15}{"MÉDIA":>15}')
# print('-' * 35)
# for i, c in enumerate(notas):
#     print(f'{i:<5}{c[0]:^15}{(c[1] + c[2]) / 2:>15.2f}')
# while True:
#     print('-' * 35)
#     notaaluno = int(input('Mostrar a nota de qual aluno? (999 interrompe): '))
#     for i, c in enumerate(notas):
#         if i == notaaluno:
#             print(f'Notas de  {c[0]} são {c[1:]}')
#     if notaaluno == 999:
#         break
# print('<<< VOLTE SEMPRE >>>')