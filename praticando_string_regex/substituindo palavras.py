"""
Nathalia é uma escritora que está revisando um texto para publicação. Durante o processo,
ela percebeu que usou a palavra "bom" repetidamente, quando queria expressar algo mais forte, como "ótimo".
Para economizar tempo, Nathalia quer substituir automaticamente todas as ocorrências da palavra "bom" por "ótimo" no texto.

Ajude Nathalia a criar um programa que solicite um texto, a palavra que será substituída e a nova palavra. O programa deve exibir o texto com as alterações aplicadas.
"""
"""
texto = input("Digite o texto a ser revisado: ").strip().lower()
substituida = input("Digite a palavra que deseja substituir: ").strip().lower()
palavra = input("Digite a palavra que substituirá: ").strip().lower()

print(texto.replace(substituida, palavra))

O meu jeito substitui palavras que não são exatamente a procurada como: bom bomba, no bomba substituiria o bom e ficaria ótimo ótimoba!
"""

import re

texto = input("Digite o texto a ser revisado: ")
palavra_antiga = input("Qual palavra deseja substituir? ")
palavra_nova = input("Qual a nova palavra? ")

nova_frase = re.sub(rf'\b{palavra_antiga}\b', palavra_nova, texto)
print(nova_frase)