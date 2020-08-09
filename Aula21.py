'''Aula 21 Mundo 03 // Funções Parte 02'''


''' Desafio 101
- Crie um programa que tenha uma função chamada voto() que vai receber como parâmetro o ano
de nascimento de uma pessoa, retornando um valor literal indicando se uma pessoa tem voto
NEGADO, OPCIONAL ou OBRIGATÓRIO nas eleições.
'''


# def vote(a):
#     from datetime import date
#     age = date.today().year - a
#     if age < 16:
#         print(f'Com {age} anos: NÃO VOTA.')
#     elif 16 <= age < 18:
#         print(f'Com {age} anos: VOTO OPCIONAL.')
#     elif 18 <= age < 65:
#         print(f'Com {age} anos: VOTO OBRIGATÓRIO.')
#     else:
#         print(f'Com {age} anos: VOTO OPCIONAL.')
#
#
# year = int(input('Em que ano você nasceu: '))
# vote(year)



''' Desafio 102
- Crie um programa que tenha uma função fatorial() que receba dois parâmetros: o primeiro
que indique o número a calcular e o outro chamado show, que será um valor lógico
(opcional) indicando se será mostrado ou não na tela o processo de cálculo do fatorial.
'''


# def fatorial(numero,show=0):
#     from math import factorial
#     fatorial_numero = factorial(numero)
#     print(f'O fatorial de {numero} é {fatorial_numero}.')
#
#     if show==1:
#         print('O cálculo desse fatorial é:')
#         for c in range(numero,0,-1):
#             print(f'{c}',end='')
#             if c > 1:
#                 print('.',end='')
#             else:
#                 print('=',end='')
#         print(fatorial_numero)
#     else:
#         print('Cálculo não exibido.')
#
#
# #Programa Principal
# numero = int(input('Informe um número inteiro para o cálculo de seu fatorial:'))
# show = int(input('Deseja ver o cálculo desse fatorial [0/1]?'))
# if show != 1 and show !=0:
#     show = int(input('Opção inválida.Deseja ver o cálculo desse fatorial [0/1]?'))
#
# fatorial(numero,show)



''' Desafio 103
- Faça um programa que tenha uma função chamada ficha(), que receba dois parâmetros opcionais:
o nome de um jogador e quantos gols ele marcou. O programa deverá ser capaz de mostrar a
ficha do jogador, mesmo que algum dado não tenha sido informado corretamente.
'''


# def ficha(nome = 'desconhecido', gol = 0):
#     if nome == '':
#         nome = '<desconhecido>'
#     if gol == '':
#         gol = '0'
#     return f'O jogador {nome} fez {gol} gols no campeonato'
#
# jogador = str(input('Nome do jogador: '))
# gols = str(input('Número de gols: '))
# print(ficha(jogador, gols))



''' Desafio 104
- Crie um programa que tenha a função leiaInt(), que vai funcionar de forma semelhante à
função input() do Python, só que fazendo a validação para aceitar apenas um valor numérico.
Ex: n = leiaInt('Digite um nº: ')
'''


# def leiaInt(msg='Enter a number:\t'):
#     """
#     -> Valida entradas numéricas do tipo inteiro.
#     :param msg: (opcional) Mensagem que será exibida na tela para entrada do valor numérico.
#     :return: O valor numérico recebido como caracter transformado em inteiro.
#     """
#     print('\n', '-' * 30, sep='')
#     while True:
#         num = input(msg)
#         if num.replace('-', '').isnumeric():  #.isdigit()
#             return int(num)
#             break
#         else:
#             print('\033[0;31mERRO! Digite um número inteiro válido.\033[m')
#
#
# # Programa Principal
# n = leiaInt()
# print(f'Você acabou de digitar o número {n}.')



''' Desafio 105
- Faça um programa que tenha uma função notas() que pode receber várias notas de alunos e vai
retornar um dicionário com as seguintes informações:
1) Quantidade de notas;
2) A maior nota;
3) A menor nota;
4) A média da turma;
5) A situação (opcional).
6) Adicione também as docstrings da função.
'''


# def notas(*ns, sit=False):
#     """
#     -> Analisa as notas e situação de vários alunos.
#     :param ns: uma ou mais notas dos alunos (aceita várias).
#     :param sit: valor opcional, indicando se deve ou não adicionar a situação.
#     :return: dicionário com várias informações sobre a situação da turma.
#     """
#
#     # Removendo True e False da lista caso tenha usado a função de maneira errada
#     ns = tuple(valor for valor in ns if bool(valor) != valor)
#
#     print('\n', '-' * 30, sep='')
#
#     dicio = dict()
#
#     dicio['total'] = len(ns)
#     dicio['maior'] = max(ns)
#     dicio['menor'] = min(ns)
#     dicio['média'] = round(sum(ns) / len(ns), 3)
#
#     if sit:
#         if dicio['média'] >= 7:
#             dicio['situação'] = 'BOA'
#         elif dicio['média'] >= 5:
#             dicio['situação'] = 'RAZOÁVEL'
#         else:
#             dicio['situação'] = 'RUIM'
#
#     return dicio
#
#
# # Programa Principal
# info = notas(5.5, 2.5, 1.5, sit=True)  # notas(3.5, 2, 6.5, 2, 7, 4)
# print(info)
# help(notas)



''' Desafio 106
- Faça um mini-sistema que utilize o Interactive Help do Python. O usuário vai digitar o
comando e o manual vai aparecer. Quando o usuário digitar a palavra 'FIM', o programa se
encerrará. OBS: use cores.
'''
# from time import sleep
#
#
# def ajuda(com):
#     """
#     -> Exibe a ajuda interativa de um "comando" do Python.
#     :param func: (Obrigatório) Função que será exibida a ajuda interativa do Python.
#     :return: Sem retorno.
#     """
#
#     título(f'Acessando o manual do comando \'{com}\'', cor='azul')
#     print(cores['branco'])
#     help(com)
#     print(end=cores['sem'])
#     sleep(2)
#
#
# def título(msg, cor='sem'):
#     """
#     -> Escreve um título com a cor desejada na tela.
#     :param msg: (obrigatório) A mensagem que será exibida na tela.
#     :param cor: (opcional) A cor em que o texto será exibido.
#     :return: Sem retorno.
#     """
#     tam = len(msg) + 6
#     print(end=cores[cor])
#     print('~' * tam)
#     print(f'|  {msg}  |')
#     print('~' * tam)
#     print(end=cores['sem'])
#     sleep(1)
#
#
# # Programa Principal
#
# # Definição de cores conforme o vídeo da solução, usando tuplas:
# '''
# c = ('\033[m',          # 0 - sem cores
#      '\033[0;30;41m',   # 1 - vermelho
#      '\033[0;30;42m',   # 2 - verde
#      '\033[0;30;43m',   # 3 - amarelo
#      '\033[0;30;44m',   # 4 - azul
#      '\033[0;3045m',    # 5 - roxo
#      '\033[7;30m'       # 6 - branco
#      )
# '''
#
# cores = {'sem': '\033[m',  # Limpa cor
#          'vermelho': '\033[1;41m',
#          'verde': '\033[1;42m',
#          'azul': '\033[1;44m',
#          'branco': '\033[7m'
#          }
#
# # As cores são feitas através do padrão ANSI, não precisando carregar bibliotecas.
#
# while True:
#     título('SISTEMA DE AJUDA PyHELP', cor='verde')
#     comando = input('Função ou Biblioteca > ')
#     if comando.upper() == 'FIM':
#         break
#     ajuda(comando)
#
# título('ATÉ LOGO!', cor='vermelho')