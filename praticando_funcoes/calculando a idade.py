"""
Julia é professora e precisa de um programa para ajudar seus alunos a calcularem suas idades com base no ano de nascimento.
Sua tarefa é criar uma função que receba o ano de nascimento e o ano atual e retorne à idade correspondente.
"""

def Idade(anoNasc, anoAtual):
    idade = anoAtual - anoNasc
    print(f"Você tem {idade} anos")

anoNasc = int(input("Digite seu ano de Nascimento: "))
anoAtual = int(input("Digite o ano em que estamos: "))

Idade(anoNasc, anoAtual)