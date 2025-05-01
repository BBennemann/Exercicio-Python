"""
Rafaela trabalha na área de marketing e quer criar mensagens personalizadas para os clientes.
Ela precisa de um programa que permita exibir saudações baseadas no nome do cliente e na cidade onde ele mora.

Crie um programa que solicite o nome e a cidade de um cliente e exiba uma mensagem de boas-vindas personalizada.
"""

nome = input("Digite o nome do cliente: ").strip().capitalize()
cidade = input("Digite a cidade do cliente: ").strip().capitalize()

print(f"Olá, {nome}! Bem-vinda ao sistema da cidade de {cidade}")