"""
Lucas é voluntário na organização de uma maratona e recebeu a lista de participantes com suas respectivas 
idades. Agora, ele precisa de um programa que apresente três informações:

    Os nomes de todos os participantes.
    As idades de todos os participantes.
    Uma relação completa com o nome e a idade de cada um.

Sua tarefa é criar esse programa com base nas informações fornecidas. 
"""

participantes = {"Mariana": 25, "Carlos": 32, "Beatriz": 28, "Rafael": 35 } 

print(f"Nome dos participantes: {", ".join(participantes.keys())}")
print(f"Idade dos participantes: {", ".join(str(idade) for idade in participantes.values())}")

for nome, idade in participantes.items():
    print(f'- {nome}: {idade} anos')