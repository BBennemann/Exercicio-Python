"""
André está testando um novo recurso no backend do Buscante que processa dados em um loop.
Durante os testes, ele percebeu que o sistema parou de responder, e suspeita que o problema está em um loop infinito.

contador = 0

while contador < 10:
    print("Processando dados...")

Qual é o problema do código de André e como resolver?
"""

contador = 0

while contador < 10:
    contador += 1
    print("Processando dados...")

"""
O contador não estava sendo incrementado então nunca mudava e entrava em loop infinito. 
Colando uma linha para incrementar o contador o problema é resolvido
"""