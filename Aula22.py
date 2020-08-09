'''Aula 22 Mundo 03 // Módulos e Pacotes'''

''' → MÓDULOS ← '''


'''Para importar um módulo (ou seja, um .py), basta utilizar o comando import'''
# import Aula22_Uteis

'''Para importar "exclusivamente" alguma função, basta: '''
# from Aula22_Uteis import fatorial, dobro #e assim sucessivamente de acordo com a necessidade

# num = int(input('Digite um número:\t'))
# x = Aula22_Uteis.fatorial(num)
# y = Aula22_Uteis.dobro(num)
# z = Aula22_Uteis.triplo(num)
# print(f'O Dobro de {num} é → {y}')
# print(f'O triplo de {num} é → {z}')
# print(f'O fatorial de {num} é → {x}')

'''Ou, pode-se fazer da seguinte maneira: '''

# import Aula22_Uteis

# num = int(input('Digite um número:\t'))
# print(f'O Dobro de {num} é → {Aula22_Uteis.dobro(num)}')
# print(f'O triplo de {num} é → {Aula22_Uteis.triplo(num)}')
# print(f'O fatorial de {num} é → {Aula22_Uteis.fatorial(num)}')



'''VANTAGENS DE MÓDULOS
1) Organização do Código
2) Facilidade na Manutenção
3) Ocultação de Código Detalhado
4) Reutilização em Outros Projetos'''




''' → PACOTES ← '''


#Se os Módulos ficarem bastante sobrecarregados de funções / códigos, há a alternativa de
#subdividir os Módulos dentro de um Pacote para ficar mais legível e organizado, logo:

'''1) Clicar com o botão direito do mouse em cima do diretório [PythonMundo03]
2) New > Python Package
3) Dar o nome para a pasta > Criar
4) Criar outros pacotes dentro de [Aula22_PacoteUteis]
5) Já com as subpastas criadas: Datas, Strings e Números, migrar o necessário para elas
6) Para utilização, basta utilizar o comando [from Aula22_PacoteUteis import Números]'''

# from Aula22_PacoteUteis import Números

# num = int(input('Digite um número:\t'))
# print(f'O Dobro de {num} é → {Números.dobro(num)}')
# print(f'O triplo de {num} é → {Números.triplo(num)}')
# print(f'O fatorial de {num} é → {Números.fatorial(num)}')






''' Desafio 107
- Crie um módulo chamado moeda.py que tenha as funções incorporadas aumentar(), diminuir(),
dobro() e metade(). Faça também um programa que importe esse módulo e use algumas dessas
funções.
'''
# import EX107Moeda
# num = int(input('Enter a number:\t'))
# print(f'Increase → {EX107Moeda.increase(num)}')
# print(f'Decrease → {EX107Moeda.decrease(num)}')
# print(f'Double → {EX107Moeda.double(num)}')
# print(f'Half → {EX107Moeda.half(num)}')


''' Desafio 108 ASSISTIR VIDEO AULA DO EXERCICIO PARA A COMPREENSAO DA DEF MOEDA()
- Adapte o código do desafio 107, criando uma função adicional chamada moeda() que consiga
mostrar os valores como um valor monetário formatado.
'''
# import EX108Moeda
# num = int(input('Enter a number:\t'))
# print(f'{EX108Moeda.moeda(num)} ← Increase 10% → {EX108Moeda.increase(num, 10)}')
# print(f'{EX108Moeda.moeda(num)} ← Decrease 15% → {EX108Moeda.decrease(num, 15)}')
# print(f'{EX108Moeda.moeda(num)} ← Double → {EX108Moeda.double(num)}')
# print(f'{EX108Moeda.moeda(num)} ← Half → {EX108Moeda.half(num)}')


''' Desafio 109
- Modifique as funções que foram criadas no desafio 107 para que elas aceitem um parâmetro
a mais, informando se o valor retornado por elas vai ser ou não formatado pela função
moeda(), desenvolvida no desafio 108.
'''
# import EX109Moeda
# num = int(input('Enter a number:\t'))
# print(f'{EX109Moeda.moeda(num)} ← Increase 10% → {EX109Moeda.increase(num, 10, True)}')
# print(f'{EX109Moeda.moeda(num)} ← Decrease 15% → {EX109Moeda.decrease(num, 15, True)}')
# print(f'{EX109Moeda.moeda(num)} ← Double → {EX109Moeda.double(num, True)}')
# print(f'{EX109Moeda.moeda(num)} ← Half → {EX109Moeda.half(num, True)}')


''' Desafio 110
- Adicione ao módulo moeda.py criado nos desafios anteriores, uma função chamada resumo(),
que mostre na tela algumas informações geradas pelas funções que já temos no módulo criado
até aqui.
'''
# from EX110Moeda import resume
# num = float(input('Enter a number:\t'))
# print(resume(num, 20, 12))


''' Desafio 111
- Crie um pacote chamado UtilidadesCeV que tenha dois módulos internos chamados moeda e
dado. Transfira todas as funções utilizadas nos desafios 107, 108, 109 e 110 para o
primeiro pacote e mantenha tudo funcionando.
'''
# import EX111Utilidades


''' Desafio 112
- Dentro do pacote UtilidadesCeV que criamos no desafio 111, temos um módulo chamado dado.
Crie uma função chamada leiaDinheiro() que seja capaz de funcionar como a função input(),
mas com uma validação de dados para aceitar apenas valore monetários.
'''
# import EX112Utilidades