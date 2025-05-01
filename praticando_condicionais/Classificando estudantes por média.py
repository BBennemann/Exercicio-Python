n1 = float(input("Digite a primeira nota: "))
n2 = float(input("Digite a segunda nota: "))
n3 = float(input("Digite a terceira nota: "))

media = (n1 + n2 + n3) / 3
print(f"Média: {media}")

if media < 5:
    print("Reprovado!")
elif media < 7:
    print("Recuperção!")
else:
    print("Aprovado!")