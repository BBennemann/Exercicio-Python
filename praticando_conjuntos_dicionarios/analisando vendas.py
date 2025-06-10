"""
Nathalia é gerente de uma loja virtual e precisa de um sistema que receba os registros de vendas 
organizados por categoria de produto. Cada categoria contém uma lista de dicionários representando 
as vendas individuais, com informações sobre o produto, a quantidade vendida e o valor unitário. 
Sua tarefa é criar um programa que exiba o total de vendas por categoria. 
"""

vendas = { 
    "Eletrônicos": [ 
        {"produto": "Smartphone", "quantidade": 5, "valor_unitario": 2000}, 
        {"produto": "Tablet", "quantidade": 3, "valor_unitario": 1500} 
    ], 
    "Eletrodomésticos": [ 
        {"produto": "Geladeira", "quantidade": 2, "valor_unitario": 3000}, 
        {"produto": "Micro-ondas", "quantidade": 4, "valor_unitario": 800} 
    ], 
    "Livros": [ 
        {"produto": "Livro A", "quantidade": 10, "valor_unitario": 50}, 
        {"produto": "Livro B", "quantidade": 5, "valor_unitario": 100} 
    ] 
} 

for categoria, produto in vendas.items():
    soma = 0
    for x in produto:
        soma += x['valor_unitario'] * x['quantidade']
    print(f'- {categoria}: R${soma}')