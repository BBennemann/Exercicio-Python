prod1 = int(input("Digite a quantidade vendida de produto1: "))
prod2 = int(input("Digite a quantidade vendida de produto2: "))

if prod1 > prod2:
    print("O produto1 teve mais vendas")
elif prod2 > prod1:
    print("O produto2 teve mais vendas")
else:
    print("Os 2 produtos venderam a mesma quantidade.")

