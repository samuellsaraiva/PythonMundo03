'''Aula 20 Mundo 03 // Funções Parte 01'''


''' Desafio 96
- Faça um programa que tenha uma função chamada área(), que receba as dimensões de um
terreno retangular (largura e comprimento) e mostre a área do terreno.
'''


# def area():
#     print('Controle de Terrenos')
#     print('-' * 20)
#     l = float(input('LARGURA (m): '))
#     c = float(input('COMPRIMENTO (m): '))
#     print(f'A área de um terreno de {l:.2f} x {c:.2f} é de {l * c:.2f}m².')
#
#
# area()



''' Desafio 97
- Faça um programa que tenha uma função chamada escreva(), que receba um texto qualquer como
parâmetro e mostre uma mensagem com tamanho adptável.
'''


# def texto(msg):
#     print('~' * (len(msg) + 4))
#     print(f'  {msg}  ')
#     print('~' * (len(msg) + 4))
#
#
# #PROGRAMA PRINCIPAL
# texto('Samuel')
# texto('Futuro Programador em Python')
# texto('Em breve')



''' Desafio 98
- Faça um programa que tenha uma função chamada contador(), que receba três parâmetros: início,
fim e passo e realize a contagem. Seu programa tem que realizar três contagens através da
função criada: 1) De 1 até 10, de 1 em 1; 2) De 10 até 0, de 2 em 2; 3) Uma contagem personalizada.
'''
# from time import sleep
#
#
# def contagem(a, b, c):
#     print('-=-' * 12)
#     print(f'Contagem de {a} até {b} de {c} em {c}:')
#     if c < 0:
#         c *= -1
#     if a < b:
#         while b >= a:
#             print(a, end=' ')
#             sleep(0.35)
#             a += c
#     else:
#         while a >= b:
#             print(a, end=' ')
#             sleep(0.35)
#             a -= c
#     print('FIM!')
#
#
# contagem(0, 10, 1)
# contagem(10, 0, 2)
# print('-=-' * 12)
# print('Agora é sua vez de personalizar a contagem.')
# i = int(input('Inicio: '))
# f = int(input('Fim: '))
# p = int(input('Passo: '))
# contagem(i, f, p)



''' Desafio 99
- Faça um programa que tenha uma função chamada maior(), que receba vários parâmetros com valores
inteiros. Seu programa tem que analisar todos os valores e dizer qual deles é o maior.
'''
# from time import sleep
#
#
# def maior(*valor):
#     print('-=-' * 12)
#     print('Analisando os valores passados:')
#     sleep(1)
#     for c in valor:
#         print(c, end=' ')
#         sleep(0.3)
#     print(f'\nForam informados {len(valor)} valores.')
#     sleep(1)
#     print(f'O maior valor informado foi {max(valor)}.')
#     sleep(1)
#
#
# maior(2, 9, 4, 5, 7, 1)
# maior(4, 7, 0)
# maior(1, 2)
# maior(6)
# maior(0)



''' Desafio 100
- Faça um programa que tenha uma lista chamada números e duas funções chamdas sorteia() e 
somaPar(). A primeira função vai sortear 5 números e vai colocá-los dentro da lista e a segunda
função vai mostrar a soma entre todos os valores PARES sorteados pela função anterior.
'''
# from random import randint
# from time import sleep
#
# values = []
# pairs = []
#
#
# def sort():
#     print('Sorteando 5 valores da lista: ', end='')
#     for c in range(5):
#         values.append(randint(1, 9))
#     for x in values:
#         print(x, end=' ')
#         sleep(0.5)
#     print()
#
# def sum_pairs():
#     for c in values:
#         if c % 2 == 0:
#             pairs.append(c)
#     print(f'Somando os valores pares de {values}, temos o total de {sum(pairs)}.')
#
#
# sort()
# sum_pairs()