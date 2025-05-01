"""
Ana está desenvolvendo um programa que precisa processar uma lista de 5 nomes de clientes para gerar relatórios mensais.
Para isso, ela precisa escrever um programa que percorra a lista de nomes e exiba cada cliente.

clientes = ["João", "Maria", "Carlos", "Ana", "Beatriz"]

Ajude Ana a decidir entre usar um laço for ou while.
Escreva o programa usando o laço que você acredita ser mais adequado para essa tarefa e explique por que escolheu esse laço.
"""

clientes = ["João", "Maria", "Carlos", "Ana", "Beatriz"]

for cliente in clientes:
    print(cliente)

"""
O uso do laço for é mais adequado pois com eles conseguimos passar a lista como um parametro 
e assim não precisamos criar um contador para um numero ja conhecido.
"""