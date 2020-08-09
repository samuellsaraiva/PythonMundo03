'''Aula 23 Mundo 03 // Tratamento de Erros e Exceções'''

'''
try():
    operação
except():
    falhou
'''

# try: #execute →
#     a = int(input('Informe um número:\t'))
#     b = int(input('Informe um número:\t'))
#     r = a / b
#
# except: #e se der problema, faça →
#     print(f'Infelizmente tivemos um problema')
#
# else: #porém, se não der problema / se deu certo a execução, faça →
#     print(f'O resultado da divisão é: {r:.2f}')
#
# finally: #vai rodar independentemente se deu certo a execução ou se deu erro na execução
#     print(f'Volte sempre, muito obrigado!')


'''AS CLÁUSULAS [ELSE] E [FINALLY] SÃO OPCIONAIS'''


# try:
#     a = int(input('Informe um número:\t'))
#     b = int(input('Informe um número:\t'))
#     r = a / b
#
# except Exception as erro: #Tratando o erro
#     # print(f'Infelizmente tivemos um problema')
#     # print(f'O problema encontrado foi → {erro}') #vai informar o erro / o "titulo" do erro
#     #print(f'O problema encontrado foi → {erro.__class__}') #vai informar a classe do erro
#
# else:
#     print(f'O resultado da divisão é: {r:.2f}')
#
# finally:
#     print(f'Volte sempre, muito obrigado!')


'''TODO [TRY] PODE TER INÚMEROS [EXCEPT]'''

# try:
#     a = int(input('Informe um número:\t'))
#     b = int(input('Informe um número:\t'))
#     r = a / b
#
# except (ValueError, TypeError):
#     print('Tivemos um problema com os dados que você digitou')
#
# except ZeroDivisionError:
#     print('O denominador não pode ser igual a 0')
#
# except KeyboardInterrupt:
#     print('O usuário preferiu não informar os dados')
#
# except Exception as erro:
#     print(f'O erro encontrado foi {erro.__cause__}') #vai mostrar a causa do erro
#
# else:
#     print(f'O resultado da divisão é: {r:.2f}')
#
# finally:
#     print(f'Volte sempre, muito obrigado!')


''' Desafio 113
- Reescreva a função leiaInt() que fizemos no desafio 104, incluindo agora a possibilidade da
digitação de um número de tipo inválido. Aproveite e crie também uma função leiaFloat() com a
mesma funcionalidade.
'''
# def readint(msg='Enter a number:\t'):
#     while True:
#         try:
#             num = int(input(msg))
#         except(ValueError, TypeError):
#             print(f'\033[31mEnter a Integer number!!!\033[m')
#             continue #ficará jogando diretamente pro while até dar certo o que se deseja
#         except(KeyboardInterrupt):
#             print('Input was interrupted by the user.')
#             return ''
#         else:
#             print(f'\n\033[35mEntered number → {num}\033[m')
#             print('-'*25)
#             return num
#
#
# def readfloat(msg='Enter a number:\t'):
#     while True:
#         try:
#             num = float(input(msg))
#         except(ValueError, TypeError):
#             print(f'\033[31mEnter a Float number!!!\033[m')
#             continue
#         except(KeyboardInterrupt):
#             print('Input was interrupted by the user.')
#             return ''
#         else:
#             print(f'\n\033[33mEntered number → {num}\033[m')
#             print('-'*25)
#             return num
#
#
# num0 = readint()
# num1 = readfloat()


''' Desafio 114
- Crie um código em Python que teste se o site Pudim está acessível pelo computador usado.
'''
# import urllib
# import urllib.request
#
# try:
#     site = urllib.request.urlopen('http://www.pudim.com.br')
# except: #pode-se colocar também [except urllib.error.URLError:]
#     print('Deu erro')
# else:
#     print('Tudo OK')
#     print(site.read()) #bonus extre para ler o conteudo do site inteiro



''' Desafio 115
- Crie um pequeno sistema modularizado que permita cadastrar pessoas pelo seu nome e idade em
um arquivo de texto simples. O sistema só vai ter 2 opções: cadastrar uma nova pessoa e listar
todas as pessoas cadastradas.
'''
from EX115 import sistema