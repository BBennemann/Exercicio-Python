"""
Sofia é revisora de textos e precisa identificar palavras muito longas em um parágrafo.
Textos mais fáceis de ler costumam ter palavras curtas, então ela quer um programa que encontre palavras que tenham mais de 10 letras e as exiba em destaque.

Crie um programa que receba um texto e exiba todas as palavras que possuem mais de 10 letras. Caso nenhuma palavra longa seja encontrada, o programa deve avisar o usuário.
"""

def Indentifica_palavras_grandes(texto):
    palavras_grandes = []
    for palavra in texto:
        if len(palavra) > 10:
            palavras_grandes.append(palavra)

    if not palavras_grandes:
        return "O texto não possui nenhuma palavra grande!"

    return f"Palavras grandes encontradas: {palavras_grandes}"

texto = input("Escreva um texto: ").strip().lower().split()

print(Indentifica_palavras_grandes(texto))
