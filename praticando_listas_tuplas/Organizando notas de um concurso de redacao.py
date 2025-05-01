"""
Uma escola realizou um concurso de redação, e o próximo passo é organizar as notas dos participantes para definir a ordem de premiação.
Para garantir transparência, as notas precisam ser classificadas em ordem crescente, do menor para o maior valor.

Com base nisso, desenvolva um programa que receba como entrada uma lista contendo as notas de todos os participantes e exiba, ao final, essa lista ordenada em ordem crescente.
"""

notas = [100, 80, 90, 95, 72, 83, 60, 52, 62, 12, 34]
print(f"Notas originais: {notas}")

notas.sort(reverse=False)
print(f"Notas em ordem crescente: {notas}")