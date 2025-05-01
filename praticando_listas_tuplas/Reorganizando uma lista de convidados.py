"""
Camila adora receber amigos para jantares temáticos. Para o próximo encontro,
ela quer garantir que a ordem de chegada seja respeitada, mas ainda precisa fazer ajustes na lista de convidados.
Camila quer adicionar novos nomes e organizá-los em posições específicas.

Como você criaria um programa que mostre a lista inicial, permita a inserção de um novo nome em uma posição escolhida e exiba a lista atualizada?
"""

lista_atual = ['Ana', 'Pedro', 'Carlos']

print(f"Lista atual: {lista_atual}")
nome = str(input("Digite o nome do novo convidado: "))
posicao = int(input("Em qual posição você quer coloca-lo: "))

lista_atual.insert(posicao-1, nome)
print(lista_atual)