renda = float(input("Digite o valor da sua renda mensal: "))
parcela = float(input("Digite o valor da parcela desejada: "))

if parcela <= renda * 0.3 and renda >= 2000:
    print("Empréstimo liberado!")
elif parcela > renda * 0.3:
    print("Empréstimo negado: parcela acima de 30% da renda")
else:
    print("Empréstimo negado: renda insuficiente!")
