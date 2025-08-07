"""
João trabalha como garçom em um restaurante e precisa calcular a gorjeta que os clientes deixam ao pagar a conta.
O restaurante sugere uma gorjeta de 10%, mas alguns clientes podem escolher dar mais ou menos.

Para agilizar o processo, João quer um programa que receba o valor total da conta e a porcentagem de gorjeta desejada e exiba o valor final que o cliente deverá pagar.

Crie um programa que peça ao usuário o valor da conta e a porcentagem de gorjeta. O programa deve calcular e exibir o valor da gorjeta e o total a ser pago.
"""

conta = float(input("Digite o valor da conta: R$"))
porcentagem = float(input("Digite a porcentagem de gorjeta: "))

def calcula_gorjeta_e_total(conta, porcentagem):
    gorjeta = (porcentagem/100) * conta
    total = gorjeta + conta
    return gorjeta, total

gorjeta, total = calcula_gorjeta_e_total(conta, porcentagem)

print(f"Valor da gorjeta: R${gorjeta}")
print(f"Total a pagar: R${total}")