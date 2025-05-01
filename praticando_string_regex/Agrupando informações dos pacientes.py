"""
Carlos é analista de dados em um hospital e está organizando informações de pacientes em um banco de dados.
Ele recebe os dados no formato: "PrimeiroNome Sobrenome - Ano". Por exemplo, “Monalisa Silva - 1994”.

Carlos precisa de um programa que leia as informações, capture cada parte separadamente, nome, o sobrenome e o ano de nascimento para preencher os campos do sistema.

Ajude Carlos criando um programa que solicite o nome completo e o ano de nascimento de um paciente e exiba-os separadamente.
"""

import re

completo = input("Digite o nome completo e o ano de nascimento do paciente: ")
padrao = r'(\w+) (\w+) - (\d{4})'

resultado = re.search(padrao, completo)

if resultado:
    nome = resultado.group(1)
    sobrenome = resultado.group(2)
    ano = resultado.group(3)

    print(f"Primeiro Nome: {nome}")
    print(f"Sobrenome: {sobrenome}")
    print(f"Ano de Nascimento: {ano}")
else:
    print("Formato inválido!")
