'''Aula 16 Mundo 03 // Tuplas'''


''' Desafio 72
- Crie um programa que tenha uma tupla totalmente preenchida com uma contagem por extenso, de
zero até vinte. Seu programa deverá ler um número pelo teclado (entre 0 e 20) e mostrá-lo por 
extenso.
'''
# extensos = ('zero', 'um', 'dois', 'três','quatro', 'cinco', 'seis', 'sete', 'oito','nove',
#             'dez', 'onze', 'doze', 'treze', 'quatorze','quinze', 'dezesseis', 'dezessete',
#             'dezoito', 'dezenove', 'vinte')
# numero = int(input('Digite um numero de 0 a 20: '))
# while numero not in range(0,21):
#     numero = int(input('Tente novamente.Digite um numero de 0 a 20: '))
# print(f'Você digitou o numero {extensos[numero]}!')



''' Desafio 73
- Crie uma tupla com os 20 primeiros colocados da Tabela do Campeonato Brasileiro de Futebol, na 
ordem de colocação. Depois mostre: 1) Apenas os 5 primeiros colocados. 2) Os últimos 4 colocados
da tabela. 3) Uma lista com os times em ordem alfabética. 4) Em que posição na tabela está o
time da Chapecoense.
'''
# times = ('Palmeiras', 'Flamengo', 'Internacional', 'Grêmio', 'São Paulo', 'Atlético',
# 'Atlético-PR', 'Cruzeiro', 'Botafogo', 'Santos', 'Bahia', 'Fluminense', 'Corinthians',
# 'Chapecoense', 'Ceará SC', 'Vasco da Gama', 'Sport Recife', 'América-MG', 'EC Vitória', 'Paraná')
# print(f'Lista de Times do Brasileirão: {times}')
# print('-=-' * 20)
# print(f'Os 5 primeiros são: {times[:5]}')
# print('-=-' * 20)
# print(f'Os 4 últimos são: {times[-4:]}')
# print('-=-' * 20)
# times_ordenados = sorted(times)
# print(f'Times em ordem alfabética: {times_ordenados}')
# print('-=-' * 20)
# print(f'A Chapecoense terminou o campeonato na {times.index("Chapecoense") + 1}ª posição.')



''' Desafio 74
- Crie um programa que vai gerar cinco números aleatórios e colocar em uma tupla.
Depois disso, mostre a listagem de números gerados e também indique o menor e o maior valor que
estão na tupla.
'''
# from random import randint
# tupla = (randint(1, 10), randint(0, 11), randint(0, 11), randint(0, 11), randint(0, 11))
# print('Os valores sorteados foram: ', end= '')
# for c in tupla:
#     print(f'{c} ', end='')
# print(f'\nO maior valor digitado foi de {max(tupla)}')
# print(f'O menor valor digitado foi de {min(tupla)}')



''' Desafio 75
- Desenvolva um programa que leia quatro valores pelo teclado e guarde-os em uma tupla. No final,
mostre: 1) Quantas vezes apareceu o valor 9; 2) Em que posição foi digitado o primeiro valor 3;
3) Quais foram os números pares.
'''
# num1 = int(input('Digite um número: '))
# num2 = int(input('Digite outro número: '))
# num3 = int(input('Digite mais um número: '))
# num4 = int(input('Digite o último número: '))
# nums = (num1, num2, num3, num4)
# print(f'Você digitou os números: {nums}')
# if 9 not in nums:
#     print('O número 9 não apareceu nenhuma vez.')
# else:
#     print(f'O valor 9 apareceu {nums.count(9)} vezes.')
# if 3 not in nums:
#     print('O número 3 não apareceu em nenhuma posição.')
# else:
#     print(f'O número 3 apareceu na {nums.index(3) + 1}ª posição.')
# print('Os valores pares digitados foram: ', end='')
# for c in sorted(nums):
#     if c % 2 == 0:
#         print(c, end=' ')



''' Desafio 76
- Crie um programa que tenha uma tupla única com nomes de produtos e seus respectivos preços,
na sequência. No final, mostre uma listagem de preços, organizando os dados em forma tabular.
'''
# itens = ('Lápis', 1.75, 'Borracha', 2, 'Caderno', 15.9, 'Estojo', 25, 'Transferidor', 4.2,
#          'Compasso', 9.99, 'Mochila', 120, 'Canetas', 22.3, 'Livro', 34.9)
# print('-' * 48)
# print(f'{"Listagem de Compras":^50}')
# print('-' * 48)
# index = -1
# x = 0
# for c in itens:
#     index += 1
#     x += 1
#     if index % 2 == 0:
#         print(f'{itens[index]:.<38}R${itens[x]:>7.2f}')
# print('-' * 48)



''' Desafio 77
- Crie um programa que tenha uma tupla com várias palavras (não usar acentos). 
Depois disso, você deve mostrar, para cada palavra, quais são as suas vogais.
'''
# palavras = ('APRENDER', 'PROGRAMAR', 'LINGUAGEM', 'PYTHON', 'CURSO',
#             'GRATIS', 'ESTUDAR', 'PRATICAR', 'TRABALHAR', 'MERCADO',
#             'PROGRAMAR', 'FUTURO', 'AEIOU')
# for c in palavras:
#     print(f'\nNa palavra {c} temos as seguintes vogais:', end=' ')
#     for x in c: # x = letra
#         if x in 'AEIOUaeiou':
#             if x == 'A' or x == 'a':
#                 print(f'\33[0;33m{x.lower()}\033[m', end=' ')
#             if x == 'E' or x == 'e':
#                 print(f'\33[0;34m{x.lower()}\033[m', end=' ')
#             if x == 'I' or x == 'i':
#                 print(f'\33[0;35m{x.lower()}\033[m', end=' ')
#             if x == 'O' or x == 'o':
#                 print(f'\33[0;31m{x.lower()}\033[m', end=' ')
#             if x == 'U' or x == 'u':
#                 print(f'\33[0;36m{x.lower()}\033[m', end=' ')