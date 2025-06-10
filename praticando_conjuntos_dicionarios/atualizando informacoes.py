"""
Ana percebeu que, após o cadastro inicial dos produtos, precisa atualizar a quantidade de um item 
específico no estoque. Sua tarefa é criar um programa que solicite o nome do produto e a nova quantidade, 
atualizando essa informação no dicionário de estoque.
"""

estoque = {"Caderno universitário": 50, "Caneta azul": 120, "Borracha branca": 30 } 

print(f"Produtos: {', '.join(estoque.keys())}")

produto = input("Qual produto quer atualizar: ").capitalize().strip()

if produto in estoque:
    quantidade = int(input("Nova quantidade: "))
    estoque[produto] = quantidade
else: 
    print("O produto não existe no estoque!")

print(estoque)