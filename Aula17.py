'''Aula 17 Mundo 03 // Listas Parte 01'''


''' Desafio 78
- Faça um programa que leia 5 valores numéricos e guarde-os em uma lista.
No final, mostre qual foi o maior e o menor valor digitado e as suas respectivas posições na lista.
'''
# valores = []
# index = 0
# for c in range(0, 5):
#     valor = int(input(f'Digite um valor para a posição {index}: '))
#     valores.append(valor)
#     index += 1
# print('-=-' * 15)
# print(f'Você digitou os valores {valores}.')
# print(f'O maior valor digitado foi {max(valores)} nas posições ', end='')
# for i, v in enumerate(valores):
#     if v == max(valores):
#         print(f'{i}', end='.. ')
# print(f'\nO menor valor digitado foi {min(valores)} na posições ', end='')
# for i, v in enumerate(valores):
#     if v == min(valores):
#         print(f'{i}', end='.. ')

#Para achar o indice do maior valor poderia ser usado valores.index(max(valores))



''' Desafio 79
- Crie um programa onde o usuário possa digitar vários valores numéricos e cadastre-os em uma
lista. Caso o número já exista lá dentro, ele não será adicionado. No final, serão exibidos todos
os valores únicos digitados, em ordem crescente.
'''
# valores = []
# while True:
#     valor = int(input('Digite um valor: '))
#     if valor in valores:
#         print('Valor duplicado. Não vou adicionar!')
#     if valor not in valores:
#         print('Valor adicionado com sucesso!')
#         valores.append(valor)
#     resp = input('Quer continuar? [S/N] ').strip().upper()[0]
#     if resp not in 'SN':
#         resp = input('Quer continuar? [S/N] ').strip().upper()[0]
#     if resp == 'N':
#         break
# print(f'Você digitou os valores: {sorted(valores)}')



''' Desafio 80
- Crie um programa onde o usuário possa digitar cinco valores numéricos e cadastre-os em uma lista,
já na posição correta de inserção (sem usar o sort()). No final, mostre a lista ordenada na tela.
'''
# valores = []
# for v in range(5):
#     valor = int(input('Digite um valor: '))
#     if v == 0 or valor > max(valores):
#         valores.append(valor)
#         print('Valor adicionado ao final da lista.')
#     else:
#         for i, n in enumerate(valores):
#             if valor <= n:
#                 valores.insert(i, valor)
#                 print(f'Valor adicionado na posição {i} da lista.')
#                 break
# print(f'Os valores adicionados foram {valores}.')



''' Desafio 81
- Crie um programa que vai ler vários números e colocar em uma lista. Depois disso, mostre:
1) Quantos números foram digitados. 2) A lista de valores, ordenada de forma decrescente.
3) Se o valor 5 foi digitado e está ou não na lista.
'''
# valores = []
# cont = 0
# while True:
#     valor = int(input('Digite um valor: '))
#     valores.append(valor)
#     cont += 1
#     resposta = input('Você quer continuar? [S/N] ').strip().upper()[0]
#     if resposta not in 'SN':
#         resposta = input('Você quer continuar? [S/N] ').strip().upper()[0]
#     if resposta == 'N':
#         break
# print(f'Você digitou {cont} elementos.')
# print('Os valores em ordem decrescente são: ', end='')
# valores.sort(reverse=True)
# for c in valores:
#     print(c, end=' ')
# if 5 in valores:
#     print('\nO valor 5 faz parte da lista.')
# else:
#     print('\nO valor 5 não faz parte da lista.')



''' Desafio 82
- Crie um programa que vai ler vários números e colocar em uma lista.
Depois disso, crie duas listas extras que vão conter apenas os valores pares e os valores ímpares
digitados, respectivamente. Ao final, mostre o conteúdo doas três listas geradas.
'''
# numeros = []
# pares = []
# impares = []
# while True:
#     num = int(input('Digite um número: '))
#     numeros.append(num)
#     resp = input('Deseja continuar? [S/N] ').strip().upper()[0]
#     while resp not in 'SN':
#         resp = input('Deseja continuar? [S/N] ').strip().upper()[0]
#     if resp == 'N':
#         break
# for i in numeros:
#     if i % 2 == 0:
#         pares.append(i)
#     if i % 2 == 1:
#         impares.append(i)
# print('-=-' * 15)
# print(f'A lista completa é {numeros}.')
# print(f'A lista de pares é {pares}.')
# print(f'A lista de impares é {impares}.')



''' Desafio 83
- Crie um programa onde o usuário digite uma expressão qualquer que use parênteses. Seu aplicativo
deverá analisar se a expressão passada está com os parênteses abertos e fechados na ordem correta.
'''
# x = str(input('Digite uma expressão: ')).strip()
# cont1 = 0
# cont2 = 0
# for c in x:
#     if c == '(':
#         cont1 += 1
#     elif c == ')':
#         cont2 += 1
# if cont1 == cont2:
#     print('A expressão está correta!')
# else:
#     print('Sua expressão está errada!')