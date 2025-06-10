"""
Laura e Ana resolveram fazer compras juntas, mas criaram duas listas diferentes. 
Elas querem um programa que mostre:

    Quais itens apareceram nas duas listas
    Quais foram exclusivos de Laura
    Quais foram exclusivos da Ana

Escreva um programa que solicite as listas e mostre os resultados dessas comparações. 
"""

lista1 = set(input("Lista 1: ").lower().split(sep=', '))
lista2 = set(input("Lista 2: ").lower().split(sep=', '))

intersecao = lista1.intersection(lista2)

print(f'Itens em ambas as listas: {', '.join(intersecao)}')
print(f'Itens exclusivos da lista 1: {', '.join(lista1.difference(lista2))}')
print(f'Itens exclusivos da lista 1: {', '.join(lista2.difference(lista1))}')