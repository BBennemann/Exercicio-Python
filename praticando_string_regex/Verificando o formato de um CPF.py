"""
Sara trabalha no setor de atendimento de uma empresa e precisa verificar rapidamente se os clientes estão digitando
seus números de CPF no formato correto antes de registrar os dados no sistema.

O formato esperado do CPF é: três blocos de 3 dígitos separados por pontos (.), seguidos por um bloco de 2 dígitos separados por um traço (-).

Ajude Sara a criar um programa que solicite o CPF de um cliente e verifica se ele está no formato correto.
"""

import re

cpf = input("Digite o CPF no formato XXX.XXX.XXX-XX: ")

padrao = r'[0-9]{3}.[0-9]{3}.[0-9]{3}-[0-9]{2}'

if re.fullmatch(padrao, cpf):
    print("CPF válido!")
else:
    print("CPF inválido")