"""
Mariana é professora de língua portuguesa e quer um programa que conte quantas vogais há em um texto digitado pelos alunos.
Isso ajudará a analisar a estrutura das palavras utilizadas.

Crie um programa que peça um texto e exiba quantas vogais (a, e, i, o, u) ele contém.
"""

def Contar_vogais(texto):
    vogais = "aeiou"
    contador = 0

    for letra in texto:
        if letra in vogais:
            contador += 1

    return contador

texto = input("Escreva um texto sem acentuação: ").strip().lower()

print(f"Quantidade de vogais no texto: {Contar_vogais(texto)}")