"""
Carlos trabalha em um comércio e precisa saber o valor total de vendas realizadas no dia. As vendas são informadas em uma única linha separadas por espaços.

Sua tarefa é criar um programa que receba essa linha, converta os valores para números e exiba o total.
"""

lista = input("Digite os valores das vendas: ").split(' ')

def Soma(lista):
    s = 0
    for x in lista:
        x = float(x)
        s += x

    return s

print(f"O total de vendas foi: {Soma(lista)}")