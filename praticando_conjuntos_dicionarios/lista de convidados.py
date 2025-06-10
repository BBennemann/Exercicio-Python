"""
Ana está organizando uma festa de aniversário e precisa de uma lista de convidados que não tenha repetições ,
pois algumas pessoas foram convidadas mais de uma vez por engano. Ela gostaria que o programa solicitasse o nome dos convidados e,
ao final, exibisse a lista organizada sem repetições.

Escreva um programa que receba os nomes dos convidados até que o usuário digite 'sair', e ao final mostre a lista de convidados sem repetições.
"""

lista = set()

resposta = input("Digite o nome do convidado ou sair: ")
while resposta != 'sair':
    lista.add(resposta)
    resposta = input("Digite o nome do convidado ou sair: ").lower()

print(f'Convidados confirmados: {', '.join(lista)}')