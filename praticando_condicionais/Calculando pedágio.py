dist = int(input("Digite a distancia a ser percorrida (Km): "))

if dist >= 200:
    print("Valor do pedágio: R$30,00")
elif dist >= 100:
    print("Valor do pedágio: R$20,00")
else:
    print("Valor do pedágio: R$10,00")